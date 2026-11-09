# R7 / REF-WP0-A: hostile referee of returns/R6/WP0-v2.md (URF architecture, v2)

Referee: isolated, brief R7/REF-WP0-A. Read: WP0-v2.md, code/WP0-v2/checks.py, CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS.
checks.py re-run: 44/44 PASS (13 s). Own sympy checks: scratchpad `ref_checks.py` (< 5 s), called REF-Sn below.
Full texts fetched and read (then deleted): 2101.08263, 2110.01587, 2608.05282.

## Verdict table
| # | Claim | Verdict | One-line reason |
|---|---|---|---|
| V1 | Master rate (3.3), bookkeeping, anchor (2.2) | STANDS | Golden-rule algebra re-derived; σ̄_e ↔ \|𝒱_{n_e}\|² anchor exact |
| V2 | (3.4), (7.3) written as tr[𝔇S] | STANDS WITH CORRECTION | Index order: (3.3) is Σ_ab 𝔇_abS_ab = tr[𝔇ᵀS] ≠ tr[𝔇S] when Im-antisymmetric parts exist |
| V3 | 16-operator basis is complete for every Fitzpatrick 𝒪_i | STANDS WITH CORRECTION | False for 𝒪₂ = (v^⊥)² (quadratic in v_s); complete for 𝒪₁, 𝒪₃–𝒪₁₅ |
| V4 | Breit–Pauli: "only mass-velocity changes the f-sum", (4.6′) | STANDS WITH CORRECTION | The orbit–orbit Breit term is left out of H_rel and contributes ≈ −(4/3)E_ee/(N_e m_e) ≈ 25–30% of δ_rel [E] |
| V5 | FDT, KK, detailed balance, positivity (4.1)–(4.4) | STANDS WITH CORRECTION | (4.2) R^∞_jj = 𝓃/m contradicts (3.2), whose R is purely spectral; the diamagnetic term is a separate contact term |
| V6 | f-sum rules (4.6)(a)–(e), π normalisation | STANDS | Re-derived; (e) also needs the hyperfine term dropped (it does not commute with s^z) |
| V7 | (4.7) mixed third moment, exact operator form | STANDS | Re-derived in 3D (and C4d in 1D), sign and prefactor included |
| V8 | (4.7) q → 0 contact limit "fixed by contact densities" | STANDS WITH CORRECTION | Leaves out the long-range ℓ = 2 (G = 0) term: correct form ∝ 𝓃_e(R_κ) + 2𝓃̄_e (REF-S2) |
| V9 | (4.8) Ward identity, acoustic sum rule, g_nn(k,0) = 0 | STANDS | Re-derived |
| V10 | (4.9) soft acoustic limit = X1 | STANDS (imported) | Denominators and contact term re-derived; C12 only checks equivalence of forms; the content rests on X1 |
| V11 | Screening (5.1)–(5.4), coupling-vector rules | STANDS | Dyson/Sherman–Morrison re-derived; Bohm–Staver line misuses the symbol ε_e (notation) |
| V12 | (5.5) four Coulomb-line classes, topological proof | STANDS WITH CORRECTION | The "ionic" class is a phonon line, not a Coulomb line, and violates "one phonon line"; the proof mixes amplitude and cut-diagram levels: [D, sketch] |
| V13 | (5.6)–(5.7), (5.7′) | STANDS | (4π/Ω)⟨⟨·⟩⟩ normalisation re-derived; C7a,b verified; 𝔗 is a pointer to X2, not given |
| V14 | CC-1 (out-state retarded (ε̃^{-1})_{G0} general; in-state conjugated) | STANDS | Both factorisations re-derived; the out-state reading is confirmed by TDH and by ⟨ψ^{(−)}\| |
| V15 | Theorem D (i)–(iii) | STANDS WITH CORRECTION | SAPT parameter is ε = κ_BO², not κ_BO; per-sector PSD of GS/X holds only up to leakage; the real gap is uniformity in N, not Coulomb |
| V16 | Theorem D (iv′)/(iv″), Γ/δ bound, d1–d11 | STANDS (imported, not derived) | DC split re-derived from the Lorentzian expansion; b_λ, 𝒞_adm, δω undefined in a "standalone" text; (6.3) missing its 1/V and spin factor |
| V17 | L0 §9.1 | STANDS | (9.2) re-derived; 2101.08263 Eq. (1) and (S.9) CONFIRMED in full text |
| V18 | L17 §9.2 | STANDS WITH CORRECTION | (iii) is false for ch = e with a relaxed lattice (ε_e^{-1}(q,0) < 0 possible); (ii) "ε₀ vs ε_∞" wrong; one miscitation |

Rubric (c): WP0-v2 claims no published paper is wrong. The source formulas I checked are CONFIRMED: 2101.08263 Eq. (1), (S.9);
2110.01587 Eqs. (1), (4); 2608.05282 Eqs. (1), (6), (8), (9).

---
## 1. Master formula and basis (V1–V3)
**V1.** With ⟨p−q|H_int|p⟩ = V^{-1}Σ_a𝒱_aO_a: Γ = 2πΣ_{p′,f}p_i|·|²δ = V∫d³q/(2π)³·2πV^{-2}Σ_ab𝒱_a*𝒱_b⟨i|O_a†|f⟩⟨f|O_b|i⟩δ = ∫d³q/(2π)³Σ_ab𝔇_abS_ab. ✔
Anchor: πσ̄_eF²/μ² = |c₁|²F²/(16m_χ²m_e²) = |𝒱_{n_e}|². ✔ The 𝒪₃, 𝒪₇, 𝒪₈ matchings were re-expanded and are correct.

**V2 (correction).** (3.4), (7.3), and CONVENTIONS §8, which copies them, write tr[𝔇S] = Σ_ab𝔇_abS_**ba**. Pairing 𝒱_a* with O_a† requires
Σ_ab𝔇_abS_ab = tr[𝔇ᵀS] = tr[𝔇S*]. Write S = S_R + iS_I (S_R symmetric, S_I antisymmetric, both real by Hermiticity), and likewise 𝔇. Then
tr[𝔇S] − tr[𝔇ᵀS] = −2 tr[𝔇_I S_I] ≠ 0 in general (REF-S4: a 2×2 Hermitian example gives 3 against 11). Symmetry makes S_I ≠ 0 for
j^α–s^β rows with SOC (∝ ε_{αβγ}q^γ in P,T-even targets), and 𝔇_I ≠ 0 for 𝒪₃-type couplings (explicit i). **Fix:** define 𝔇_ab ≡
Σ𝒱_a𝒱_b* or write tr[𝔇ᵀS] in (3.4), (7.3), P(N_eh|q,ω) and CONVENTIONS §8. (4.4) is unaffected (λ_max(𝔇)tr Sᵀ = λ_max tr S).

**V3 (correction).** "Every Fitzpatrick operator is at most linear in 𝐒_s and in v_s" is false for 𝒪₂ = (v^⊥)² in 1203.3542, which is
quadratic in v_s and needs a v_s⊗v_s (kinetic/stress) row. Either restrict to i ∈ {1, 3…15}, consistent with CONVENTIONS §7 "i = 1…15" only if
𝒪₂ is explicitly excluded, or add the row (cf. the 𝒯_e row already added for absorption).

## 2. Exact relations (V4–V9)
**V4 (correction).** The H_rel listed in (1.2) has mass-velocity, Darwin, SOC, SOO and SSO, but **no orbit–orbit term**
H_oo = −(α/2m_e²)Σ_{i<j}[p_i·p_j + r̂_ij·(r̂_ij·p_i)p_j]/r_ij, which is part of Breit–Pauli. Derivation: [p_i, e^{iq·r_i}] = qe^{iq·r_i} and
[e^{−iq·r_j}, p_j] = qe^{−iq·r_j}, so [n†,[H_oo,n]] = Σ_{i<j}2(q·K_ij·q)cos(q·r_ij), with K_ij = −(α/2m²)(1 + r̂r̂)/r_ij. The angular average
⟨1 + cos²⟩ = 4/3 (REF-S3) gives, at q r_core ≪ 1,
  δ_oo = −(4/3)E_ee/(N_e m_e),   E_ee = ⟨Σ_{i<j}α/r_ij⟩.
Thomas–Fermi gives E_ee ≈ T_tot/3, so δ_oo/δ_mv ≈ (4/5)(1/3) ≈ 0.27 [E]: Ge −0.58% → ≈ −0.73%, Si −0.18% → ≈ −0.23%. Then "only the
mass-velocity term changes the f-sum" is false for Breit–Pauli, and (4.6′) and (1.2) must either add δ_oo or state that H_rel
omits orbit–orbit. The SOC/Darwin/Dirac statements (C4h, linear-in-p argument) are correct. The (5/3)⟨T⟩/m coefficient was re-derived:
F(p±q) expansion with ⟨(p·q)²⟩ = p²q²/3, valid for cubic targets as well as closed shells.

**V5 (correction).** (3.2) defines R by the commutator only, so its spectral representation (4.2) has R^∞ ≡ 0 for **every** operator.
Writing "R^∞_jj = +δ_{αβ}𝓃/m" silently redefines R_jj as the physical (para + dia) response. CONVENTIONS §6 (Π^γ_T = e²(R_jTjT + 𝓃/m))
uses the paramagnetic R. Replace with: "R^{phys}_{jj} = R_jj + δ_{αβ}𝓃_s/m_s; gauge invariance R^L_jj(q,0) = −𝓃/m". FDT, detailed
balance (re-derived by i↔f relabelling) and PSD are correct. Note Γ_χ ≥ 0 uses tr[𝔇Sᵀ] (V2).

**V6.** (4.6) re-derived: ∫_ℝωS = π𝓜¹ requires S[O†] = S, i.e. inversion, as stated. (e) needs, besides SOC = 0, the hyperfine contact
term dropped: s·𝐈δ³ does not commute with s^z(q) (a negligible but unstated term).

**V7.** (4.7) re-derived in 3D: [H, n_κ] = q·j_κ; [V, q·j_κ] = (i/M_κ)e^{iq·R}q·∇_RV; [n_e†,H] = q·j_e(−q); the only surviving commutator is
(i/M)(i/m)e^{iq·(R−r)}(q·∇)²V = (1/mM)e^{iq·(R−r)}(q·∇)²U, with V = −U. ✔ The moment interpretation also holds:
⟨[A,B]⟩ = V∫(dω/2π)ω³(S_eκ[O] + S_eκ[O†]) by the same steps as (4.5). The text should say this, since (4.7) only names the commutator.

**V8 (correction, focus item).** The qualifier "(q → 0, qa ≪ 1): ⟨(q·∇)²(−U_κ)⟩ → (q²/3)Z_κe²δ³" is wrong. ∂_i∂_j(1/r) has a PV part
∝ (3r̂_ir̂_j − δ_ij)/r³ that is *conditionally convergent*, and the electron–nucleus pair density g_eκ(r) → 𝓃̄_e at large r. In Fourier
space, FT[(q·∇)²U](k) = −(q·k)²Z e²/k². Take g(r) = Σ_G n_Ge^{iG·r} (origin on the nucleus). Then
  ∫d³r g(r)e^{−iq·r}(q·∇)²U = −Ze²Σ_G n_G (q·(q−G))²/|q−G|²  →(q→0, cubic site)  −Ze²q²[𝓃̄_e + (1/3)Σ_{G≠0}n_G] = −(q²/3)Ze²[𝓃_e(R_κ) + 2𝓃̄_e].
The G = 0 term is non-analytic: it survives for every q ≫ 1/L, so the ℓ = 2 part does *not* vanish as q → 0. A model with an isotropic Gaussian
plus a uniform background confirms the difference exactly, −(2/3)q²Ze²𝓃̄_e (REF-S2). **Correct statement:**
  𝓜³_eκ(q → 0) = −q²Z_κe²𝓃_κ[𝓃_e(R_κ) + 2𝓃̄_e]/(3m_eM_κ)   (point nuclei, cubic sites).
The added term is the e–ion "plasma" cross term (∝ ω_{p,e}²Ω_{p,κ}²/(Z_κe²)). It is numerically small in all-electron Si
(2𝓃̄_e/𝓃_e(R) ≈ 1×10⁻⁴; ≈ 5×10⁻³ in diamond [E]), but the sentence "fixed by contact densities" is an overclaim. F4's
"consistent with the qualified (4.7)" (WP3-v2 J8) must be rechecked against the corrected form.

**V9.** [H, ρ_M] = q·𝐠 ✔ (C4f). g_mn(k,0) = (ε_n − ε_m)(−iℓê·p_mn) re-derived from ∇V = −i[H, p]. ✔

## 3. Soft limit (V10)
At Q → 0, the c-line denominator ε_c(k+q+Q) − ε_c(k+q) + ω_Q ≈ |Q|(Q̂·v^g_c + c_ν) (upper sign) and the v-line (Q̂·v^g_v ± c_ν), with a relative minus sign,
reproduce the (4.9) structure. The contact term iℓê·qρ comes from e^{iq·u}. The remainder O(|Q|^{1/2}) is consistent with ℓ_Q ∝ |Q|^{-1/2}.
C7d holds trivially (ρ_cv(k,q) = O(q)). C12 checks only lab ↔ comoving equivalence and the v1 difference. The numerators (Q̂·D^n·ê ∓ c_νê·p_nn)
rest on X1 and are not derived in WP0-v2, so the tag should read "[D in X1]". |D|/c_ν ≈ 10 eV/3×10⁻⁵ ≈ 300 keV ✔.

## 4. Screening (V11–V13)
**V11.** R = R̃ + R̃Zᵀv_CZR ⇒ (5.3) (C2). (5.4) gives S_zz = −2v_C^{-1}Im(ε^{-1})_00/(1−e^{−βω}) ✔. (5.5) gives n_e = −n_z + ΣZ_κn_κ ✔. j_L follows from (q·j)_fi = ω_fi n_fi ✔.
The transverse-photon estimate (16.6/4000)² ≈ 2×10⁻⁵ ✔. *Notation:* "Bohm–Staver ω² = Ω²_{p,ion}/ε_e(q,0)" needs the **clamped electronic**
ε(q,0) (= ε_∞(q)). ε_e is NOTATION's relaxed electron channel 1 + v_CR_ee (V18 shows the two differ in sign in polar targets).

**V12 (correction).** (i) At amplitude level the emitted phonon is an external leg, so "removing the phonon line leaves a tree; it closes one
cycle" only makes sense for the cut S diagram. There the external vertex appears twice and the cut runs through the cycle. The argument is
right in outline: lines adjacent to an ion vertex carry Q+G by momentum conservation, and lines between the q-injection points carry P.
But it is a sketch: the case where both injection points lie on the same arc, and the frequency assignment, are not written out.
(ii) The "ionic" class (a phonon at q mod G inside ε(q,ω)) is a **second phonon line**, which contradicts the hypothesis "one phonon line".
It is a phonon-line insertion in the external chain, not a Coulomb-line class. Restate: "three Coulomb-line classes at O(g²) with one phonon
line, plus the ionic insertion at O(g²·Z*²/M) in the external channel". Tag: [D, sketch]. (iii) "ε̃ even in ν below E_g" needs TR
(R(Q,−ν) = R(−Q,ν)* and R(Q) = R(−Q)). It fails for magnetic references, so state it.

**V13.** S = (2π/V)·2·Σ_{kQ}|M|²/N·δ = (4π/Ω)N^{-2}Σ_{kQ}|M|²δ ✔. Sign of ±ω_Q ✔. ε₂^{PA}(q,ω) = O(g²) inside the window, so
"non-absorptive" means "to O(g²)". The claim "exact to O(g⁴)" is then consistent. ε(P,ω_f) **is** absorptive (the final pair is on shell), and that is
handled by C7a. (e): 𝔗 (X2 (2.1)) is not given, so the specification of the computation is a pointer, not standalone.

## 5. CC-1 (V14): out-state vs in-state weight, STANDS
R = R⁰(1+fR), R† = (1+R†f)R⁰† ⇒ (1+R†f)(R⁰−R⁰†)(1+fR) = R − R†. With R⁰_{GG′} = Σρ_G*ρ_{G′}g (the (3.2) order), the 00 element gives
Σ_pair|Σ_G(1+fR)_{G0}ρ_G|²Im g, because (1+R†f)_{0G} = [(1+fR)_{G0}]*. The second factorisation gives w^in_G = [(1+Rf)_{0G}]*. Both are re-derived.
Physical reading, checked independently: δ⟨n(q+G)†⟩ = R_{G0}φ_ext. This is a density modulation ∝ e^{+i(q+G)·r}, so V_tot(q+G) =
(δ + v_CR)_{G0}φ_ext and the amplitude to a bare pair is Σ_GV_tot(G)ρ_cv(q+G). Equivalently, ⟨ψ_f^{(−)}| = ⟨φ_f|(1 + VG^{(+)}) brings in
retarded R. So (7.2) is the out-state form without inversion. WP1 [E2] needs ρ → ρ* (C10f, C10g reproduce this). Caveats: (a) the
"exact factorisations for any target" sentence in §7.2 must carry "at RPA/TDDFT" (it does in §10); (b) in the PAER window R(q,ω) is
Hermitian only to O(g²), so the in/out difference there is O(g⁴) in the rate. That is harmless, but "coincide" should read "coincide to O(g²)".

## 6. Theorem D (V15–V16)
**V15 (corrections).** (a) In space-adiabatic perturbation theory (math-ph/0201055) the small parameter is ε = (m_e/M)^{1/2} = κ_BO², so
𝒫_⊥U_n†HU_n𝒫₀ = O(κ_BO^{2(n+1)}). Writing O(κ_BO^{n+1}) is loose. It is not false, but it mislabels the cited result. Note that the source is
read only as [ABS]. (b) Inserting Π_GS + Π_X = 1 next to δ(ω − H) gives sectors that sum exactly but are PSD only up to O(ε^{n+1})
leakage. Using Π δ(ω−H) Π gives PSD sectors that sum only up to that leakage. Since both are distributions, either statement holds
only against test functions smooth on the leakage scale. So "(i) each PSD, no double counting, nothing omitted" needs the same "bins"
qualifier already given for X0/X+. (c) "Coulomb singularities assumed harmless [C]": for finite molecules this is handled in the literature
by Hunziker-type distortions (Klein–Martinez–Seiler–Wang; Panati–Spohn–Teufel's time-dependent BO paper; from memory, [UNVERIFIED]).
The genuine gap is that the SAPT constants are not uniform in the number of nuclei (crystal limit, gapless acoustic branch). §6.2(iv)
lists this only as a rigour item, but (i) is tagged "[D given U_n]" as if U_n were available for a crystal. (d) "𝔉 = 0 for Si, Ge,
diamond [D, sketch]": the PT-real-gauge argument works at SOC = 0. Ge has SOC (PT² = −1, Kramers doublets, no real gauge), so it needs a
doublet-summed argument. (e) Boost amplitude (m_eq/M)⟨n|Σr|0⟩ and δM = N_em_e (TRK) re-derived ✔. Note the identity
⟨n|Σ∇_iV_eN|0⟩ = m(E_n−E_0)²⟨n|Σr|0⟩ uses Σ_i∇_iV_ee = 0 and a single nucleus, as stated.

**V16.** Expanding |gρ/(δω + iΓ/2) + a^off|² gives (2π/Γ)|gρ|²δ + |gρ|²fp(1/δω²) + 2Re(a^{off*}gρ)PV(1/δω) + Fano δ-term + O(Γ). This
reproduces (6.3) and the 𝔉 term. The T3a/b double-counting orders (Lorentzian tail = fp sideband → O(g²); resummed → O(1)) re-derived ✔.
The Γ/δ bound (1.1 + b_λ), 𝒞_adm(ℓ_win), δω and d1–d11 are imported from O4 with b_λ and 𝒞_adm undefined in this "standalone" text.
Rubric (e): this is a restatement, not a specification. (6.3) as printed lacks the (2/V) (spin, volume) factor of (3.1)/(7.2). With Si
Γ/δ up to 0.6, the bound is O(1) near the edge, which is consistent with the stated restriction to totals there.

## 7. L0 and L17 (V17–V18)
**V17.** δ(ω−ω_q) = δ(q̂·v − v_min)/q and ∫dΩ_q gives 2πΘ/(qv), so 𝒢 = η/(2q) after the 4π average. Then
dℛ/dω = (ρ_χσ̄_e/(4πm_χρ_Tμ²))∫q dqF²ηS̄ ✔. Inserting S̄ = 2q²W/e² and |V|² = πσ̄F²/μ² gives Hochberg 2101.08263 (S.9),
ρ_χ/(2π²e²ρ_Tm_χ)∫dq q³|V|²Wη. **CONFIRMED in full text.** Eq. (1) is quoted correctly (T = 0 form). Validity (a)–(d) and corrections (α)–(δ) are sound.
Hypothesis (I) is honestly an approximation unless the target or f_χ is isotropic.

**V18 (corrections, L17).** (9.3)–(9.6) re-derived. ∫_ℝωL = πω_p² follows from −(1/π)∫ωIm R = 𝓜¹ at any T. Hölder for −1 ≤ n ≤ 1 (C5).
2608.05282 Eq. (8) = (9.6) **CONFIRMED** (K_n of their Eq. (6) starts at 0). 2110.01587 Eq. (1) **CONFIRMED**.
(a) **(iii) is false for ch = e when the lattice relaxes.** In WP0-v2's own (5.3) with a two-fluid proper response (R̃_eκ = 0), write
a ≡ −v_Cχ_e = ε_∞ − 1 and b ≡ −v_CZ²χ_ion = ε₀ − ε_∞. Then (REF-S1)
  ε_e^{-1}(q→0, 0) = 1 + v_CR_ee = (1 + b − ab)/(1 + a + b),   ε^{-1} = 1/(1 + a + b) = 1/ε₀.
GaAs-like a = 9.9, b = 2.0 gives ε_e^{-1} = −1.30. The ions over-screen through positive feedback, so 1 − ε_e^{-1}(q,0) = 2.3 > 1 and the
"conservative step" fails by ×2.3 for an electron-only coupling with ω_th below the phonon band. WP1 [E3] (RPA, clamped or total ε) does
not cover ε_e with a relaxed lattice. **Fix:** (iii) holds for ch = c, and for ch = e only at clamped nuclei or with the (iv) tightening
(ω_th above the phonon band, ε_∞). For polar targets at ω_th < ω_max, use K_{−1} ≤ (π/2)(1 − ε_e^{-1}(q,0)) with the computed ε_e.
(b) (ii) "differing by the ionic static polarisation (ε₀ vs ε_∞)" is wrong: the total channel gives ε₀, and the electron channel gives
ε₀/(1 + b − ab), which is neither ε_∞ nor ε₀. (c) "inserted in (3.4)… gives… 2110.01587 Eq. (4)": their Eq. (4) is the positive-range
bound. The rate bound is their Eqs. (8)–(9) (n = −1). (d) (iii) needs ε_ch^{-1}(q,0) ≥ 0 for "≤ 1" and ε_ch ≥ 1 for "≥ 0". The text conflates the two.
The L17 status should read "DERIVED at RPA+LFE for ch = c and for clamped ch = e; ch = e relaxed: computed ε_e required".

## 8. Rubric (d), (e) and minor items
- (d) Interfaces: V2 propagates into CONVENTIONS §8 (tr[𝔇S]) and WP6 seeding. ε_e is misused in the Bohm–Staver line. "No deviations
  from NOTATION v4" (§15) is therefore not quite true.
- (e) Gap closures in WP0-v2 itself: (5.6)–(5.7) specify the computation only through X2 (2.1). (iv″) only through O4 (b_λ, d1–d11). F4 "closed"
  rests on the uncorrected (4.7) limit (V8). O5 is closed only for ch = c (V18).
- (a) Steps tagged [D] that are imported: (4.9) (X1), (iv″a–d) (O4), (4.6c) split (WP3 J7), the (iii) δM_κ moment (WP3 J3). Retag "[D in Xn]".
- (4.6)(c) "Re S_eκ changes sign in ω" follows at T = 0. At T > 0 the zero first moment over ℝ does not force a sign change on ω > 0.
- (5.6): T ≪ E_g "otherwise divide L^{PA} by (1 − e^{−βω})" is fine. F7 is consistent.
- Numbers re-checked: (Zα)² Ge = 0.0545 ✔; δ_mv Si/Ge from virial T: 0.18%/0.58% ✔; ω_{p,c} nuclear part 2.7×10⁻⁴ (Si) ✔; DFPT error
  (60 meV/1.1 eV)² ≈ 3×10⁻³ ✔ (conservative; the direct gap gives 3×10⁻⁴).

## 9. Required corrections (summary)
1. (3.4), (7.3), P(N_eh), CONVENTIONS §8: tr[𝔇S] → tr[𝔇ᵀS] (or redefine 𝔇). [S]
2. §2: exclude 𝒪₂ or add a v_s⊗v_s row. [W]
3. (1.2), (4.6′): add the Breit orbit–orbit term, δ_oo = −(4/3)E_ee/(N_em_e) at q r_core ≪ 1 (≈ 27% of δ_mv) [E], or restrict H_rel explicitly. [S]
4. (4.2): R^∞ ≡ 0 for (3.2)'s R; physical current response = R + 𝓃/m. [W]
5. (4.7): q → 0 limit −q²Z_κe²𝓃_κ[𝓃_e(R_κ) + 2𝓃̄_e]/(3m_eM_κ); drop "fixed by contact densities"; recheck F4/WP3-v2 J8. [S]
6. (5.5): ionic insertion is not a Coulomb-line class under the one-phonon hypothesis; tag [D, sketch]; TR for evenness. [W]
7. Theorem D: ε = κ_BO² order; sector PSD/sum only up to leakage; the gap is N-uniformity; Ge 𝔉 needs a doublet argument. [W]
8. (6.3): restore the (2/V) normalisation; define b_λ, 𝒞_adm, δω or mark the result imported. [W]
9. L17 (iii)/(ii): electron channel with relaxed lattice not covered (counterexample ε_e^{-1} = −1.3, GaAs-like); fix the status and the ε₀/ε_∞ sentence;
   2110.01587 Eq. (4) → Eqs. (8)–(9). [S]
10. Bohm–Staver: ε_e → clamped electronic ε(q,0). [N]
