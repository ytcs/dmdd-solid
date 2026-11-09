# R16 referee report VER-CW5 (hostile, isolated) on returns/R16/CW5.md

Referee: VER-CW5, brief briefs/R16/VER-CW5.md. Read: returns/R16/CW5.md, code/CW5/ (checks.py, LE-128/, LE-137/), returns/R14/WP5-AUD.md, returns/R14/GAP-EF.md
(EF9 lines), returns/R13/WP5-v4.md (greps), returns/R12/WP7-E-v3.md (§3.2 (B-a)–(B-d)), LIMITS.md (L23, L30, L32, L36–L38), NOTATION.md (greps), CONVENTIONS.md §12.
Not read: referees/R16/*, other returns/R16 files, briefs/*, log/LAUNCHES, and referees/R14/* (not in the read list), so the REF-A/B inputs quoted in CW5 §1
were checked only against WP5-AUD and by recomputation.
**Rerun:** `python3 code/CW5/checks.py` → **21/21 PASS in 19.0 s** (all numbers as quoted). **Own checks** (sympy/numpy/scipy, < 5 s, scratchpad, not committed):
V1 L38 bound with X^{oth}_ER of either sign; V2 signed-sampler variance; V3 bimolecular *formation* against r_g; V4 trajectory count for 6%; V5 σ conversion
range; V6 HV FOM at 220 eV (1σ) and C7l at ⟨𝔮⟩ = 0.873; V7 spin counting of α_ohm = 4K (by hand, golden rule against Leggett's normalisation).
**Literature [FT]** (lit.py → literature/papers-r16-VER-CW5/, PDFs deleted afterwards): 1805.09942, cond-mat/0310283, 2009.03804 (main text and suppl.),
0802.2404, cond-mat/0507622, 1705.01108. Crossref API: both Andreev–Lifshitz review DOIs resolved (authors, journal, volume, issue, page as quoted).

## 0. Verdict table (scope 1–3)
| # | Item | Verdict | Reason (short) |
|---|---|---|---|
| 1 | OC-1 / §1.2 D-1: exact zero-field ratio (CW5-3), 1.407 vs 0.280 | STANDS | (1 − 𝔶𝒢)/(1 − 𝒢) = 1.4072 at 𝒢 = 1.17/3.75, 𝔶 = 0.102; first-order (1 − 𝔶)𝒢 = 0.280; C1b reduction checked |
| 2 | OC-1 drift sentence "Si and Ge data both biased; 1 µs at 4 V/cm" | STANDS WITH CORRECTION (N) | 1805.09942 biases ±2 V [FT p. 2] ✓, but the Ge iZIP field is ≈ 1.6 V/cm (assuming a 25 mm crystal; thickness not read here), not 4 V/cm; state the Ge field |
| 3 | OC-2 (D-2 guard sentence) | STANDS | consistent with WP5-AUD D-2; "≤ 0.25 eV per carrier" is [E] and should carry the tag |
| 4 | OC-3 (B-1 five-part split, E_s^{(0)} = ω_s/2, ΔZPE excluded) | STANDS (not independently checked) | internally consistent; REF-A/B text not in my read list |
| 5 | OC-4 (B-2) | STANDS WITH CORRECTION (N) | √(2/(n−1)+2/n) ≤ 0.06 needs **n ≥ 1112** (V4); 1100 gives 6.03%. "≥ 100 at 1 keV" ✓ (100.1) |
| 6 | OC-5 / L38 DERIVED (C3 proof) | STANDS WITH CORRECTION (W) | proof correct for X^{oth}_ER ≥ 0, but X includes ΔZPE "of either sign" (WP7-E-v3 (B-c)); at r_coll = 1, f₀ = X·E_st/ω exactly (V1), so the bound fails by O(X d′) for X < 0. Add X^{oth}_ER ≥ 0 to Validity, or state "to O(X^{oth}_ER E_st/ω)" |
| 7 | OC-6 roundings/tags | STANDS | 0.4748 → ≲ 0.47 ✓; 272–543 ✓ |
| 8 | OC-7 / §1.3 D-7: (c) HV NO-GO → CONDITIONAL; 2.014, 1.763, 2.015, F_NR* | STANDS | C2 reproduced; V6: C7l "up to 2.40" reproduced (2.397 at ε 3.75, 2.415 at ε 3.8, Y = 0.12, F_ER 0.119, ⟨𝔮⟩ 0.873); "firm at ≲ 220 eV (1σ)" holds **at 220 eV**: 1.70–1.87 for Y ∈ [0.085, 0.10], F_NR = 0.4 (not in C2; add); 100 eV not checked here |
| 9 | OC-7 / L42 source tag "[FT, via REF-WP5-AUD-A/B]" | STANDS WITH CORRECTION (N) | contradicts OC-6's own rule; write "[FT] (2303.02196, as read by REF-WP5-AUD-A/B)" |
| 10 | OC-8 σ_ln(r_coll) = 0.1 [E] | STANDS | literal reading; ruling matches the evidence quoted in WP5-AUD |
| 11 | OC-9 / §2.1 signed seed sampler | STANDS WITH CORRECTION (W) | unbiasedness ✓. "Variance larger by at most (Σ\|K\|/K_tot)²" is **false**: the factor is exact for the **second moment** relative to the \|K\|-law; for f ≡ 1 the \|K\|-variance is 0 and the signed one 0.21 (V2). Also: if \|Im(a*B)\| ≤ \|B\|²/2η holds in every q bin, every K_i ≥ 0 and the signed sampler is unnecessary; it matters exactly where the condition fails, and there CW5 has not shown Σ_iK_iP_i(N_eh) ≥ 0 for every N_eh |
| 12 | OC-10 / §2.7 renewal leading term → DERIVED | STANDS WITH CORRECTION (W) | (CW5-5) is exact (checked: N_ev = 2x − 1). The limit step invokes "the renewal theorem in ln x" for a walk that is only *asymptotically* stationary with killing; that is a Markov-renewal/coupling result, not the textbook theorem. Add (r4′): the approach to the scale-free law is summable along the lineage (O(E_g/x) suffices), cite the theorem used. Notation: "E N(E)" mixes energy E and expectation 𝔼 |
| 13 | OC-11 / §3.6 Andreev–Lifshitz | STANDS | cond-mat/0310283 ref. [11] = ZhETF 56, 2057 (1969) [FT p. 14] ✓; T dependence "predicted [16, 17]" (Pushkarov) [FT p. 3] ✓; Crossref DOIs ✓ |
| 14 | OC-12 / §3.9 tanδ₀ table | STANDS WITH CORRECTION (W) | all values ✓ [FT]; but cond-mat/0507622's "CVD SiO₂" is **plasma-enhanced CVD** (PDF p. 7: "deposited with plasma enhanced CVD … SiH₄ and O₂"), so "CVD 5×10⁻³ vs PECVD 2.7–2.9×10⁻³" are two PECVD films; relabel |
| 15 | §2.2 LE-138 size "≤ 2.7%" (table) | STANDS WITH CORRECTION (W) | d ln ε/d ln λ_ph = β(ε/E_g − c₀)/(ε/E_g) = 0.1196 from (EF9) ✓; 2.7% is the Z_qp = 0.8 value, not a bound (W vs W_R untreated; EF9 is an observed fit, L43). Write "≈ 2.7% for the Z part [E]" |
| 16 | §2.3 (CW5-1) memory bound | STANDS WITH CORRECTION (W) | algebra ✓ given (H-BGK); "θ_{R-k} is then bounded, not estimated" overclaims: the bound is conditional on (H-BGK), which is itself a relaxation-time form of (R-k) |
| 17 | §2.5 Theorem CW5-G (linear kinetics, asymptotic split) | STANDS WITH CORRECTION (N) | ✓ (C6 exact). Add: M diagonalisable (else t^m e^{−γt} terms); w_k may be negative; BX decay assumed non-radiative (hypothesis, state it) |
| 18 | §2.5 (ii) "bimolecular formation ⇒ r_g = 1/(1 + t/t₀)"; "r_g^{NR} ≠ r_g^{ER} derived" | **FALLS as stated** | F → X formation moves gap energy from E_pairs to E_X, both inside r_g; with C_X n² formation and slow X decay r_g stays 0.9997/0.992/0.909 at t/t₀ = 1/10/100 while n_F = 1/(1+t/t₀) (V3). C6b only checks n_F. Two fixes: (a) state the hypothesis k_X↓ ≫ C_Xn(t) (formation rate-limiting, r_g ≈ n_F), and then the formula stands; or (b) use a bimolecular **energy-loss** channel (X–X annihilation ∝ n_X², or Auger ∝ n³ → (1 + 2t/t₀)^{−1/2}). The NR ≠ ER conclusion survives either way; OC-1's "bimolecular tail" wording must follow |
| 19 | §2.5 excitons carry E_g − E_x^b; ≤ 1.3% | STANDS | 14.7/1170 = 1.26% [UNVERIFIED E_x^b] |
| 20 | §3.1 (CW5-6) α_ohm = (1/2π²)Σ_σΣ_ν δ̃² | STANDS ([D, sketch] kept) | X-ray-edge time exponent Σ(δ/π)² = 2α ⇒ (CW5-6); reduces to WP7-T's Σ(2l+1)Δδ²/π² with two spins ✓; C8 exponents ✓ |
| 21 | §3.1 Born limit α_ohm = 4K, per-spin n₀ | STANDS WITH CORRECTION (N) | 2009.03804 Eq. (4) and K = (n₀VΩ)² [FT p. 4], K = 0.07 and 0.11 [FT p. 5], n₀ "single-spin DoS" [FT suppl. p. 14] ✓; V7: Black's 4πK is the spin-summed golden rule and α = 4K ✓. The pitfall "with a both-spin n₀ the factor becomes 2" is wrong: K_both = (2N_σVΩ)² gives α = K_both (factor **1**) |
| 22 | §3.2 S_HR,k, E_reorg, λ_eff, 𝒮_inst = 2λ_eff | STANDS | standard harmonic definitions; 384 SCFs per Hessian (64·3·2) ✓ |
| 23 | §3.3 conditional frozen verdicts | STANDS WITH CORRECTION (N) | 47.2, 23.6, 33.6, 6.8, 166 meV Å², 27.5 ✓; "≥ 14%" ✓ (14.2%); Al: 23.6/25 → **≥ 5.6%**, not 6% |
| 24 | §3.4 P̄_STM bracket; σ ≈ 10²/(µm³GHz) = 2.4×10¹⁹ /(eV cm³) | STANDS WITH CORRECTION (N) | tanδ₀ = πP̄p²/(3ε_rε₀) and 2.37×10²¹–6.6×10¹⁹ ✓. 1705.01108 does say "≈ 10²" [FT p. 13], but 0.4–0.5 per µm² over 2–3 nm is 1.3–2.5×10² (V5): quote **(3.2–6.0)×10¹⁹ /(eV cm³)** |
| 25 | §3.5 (a) spectral diffusion; (b) max-ent E_slope; (c) Borel | STANDS WITH CORRECTION (N) | (a)–(c) ✓. "(b) is exactly the type-T tilt θ_𝒦 of WP6" is unsupported here (no derivation); drop or cite |
| 26 | §3.7 L30 T⁻⁹ → DERIVED | STANDS WITH CORRECTION (N) | second-difference cancellation re-derived by hand (1/(ω−d₁) − 1/(ω′+d₂) → [ε(k+q)+ε(k−q′)−ε(k)−ε(k+q−q′)]/ω²) ✓; ω⁶n_B → T⁷, ×(qa)² → T⁹ ✓; source Eqs. (12) p. 3, (49) p. 7, (53)–(61) p. 8 ✓ and the "3 + 4 + 2" reading is the source's own (p. 8). DERIVED applies to the **exponent**; prefactor stays source [FT]. "For T < Δ_dfn the source's Eq. (55) applies": (55) is the phonon-wavevector change in the effective-mass regime, not a D law; cite (55)–(57) as kinematics only |
| 27 | §3.8 S_pol(T), W_r | STANDS | S_pol(0) = J₀ω_D²/2π and ΔS = πJ₀T²/3 re-derived ✓ |
| 28 | §4.1 (CW5-8) ionic ledger | STANDS | bookkeeping identity; Pooley–Hersh premise [UNVERIFIED] correctly tagged |
| 29 | §4.2 (i)–(iii) LEE structure (CW5-9) | STANDS WITH CORRECTION (W) | 1/t and ln sum rule ✓ (C13). Prediction 4 (time-independent shape) is hypothesis (H-L3), not a prediction; τ_av = 3/2 is the size law in releases s, energy only if per-release energy has finite mean (state). 2208.02790/2202.05097 quotes not re-read (tagged so) |
| 30 | §4.3 (CW5-10) f_A = C_Aλ²/(12π²D_ar₀²) | STANDS | ∫n³dA = λ³/(3π²s²), ∫dt/s² = 1/(4D_ar₀²) re-derived ✓ |
| 31 | §4.4 (CW5-11) Poisson tail | STANDS | T = 0 displaced oscillator ✓ (C12) |
| 32 | §4.6 (CW5-12) TV bound | STANDS WITH CORRECTION (W) | bound ✓ for 𝒫_det ∈ [0,1] with TV = ½L¹. "Exact **iff** marks are sufficient" overclaims: sufficiency ⇒ zero residual; the converse fails (the detector may ignore the extra features). Write "if" |
| 33 | §4.7 LE-150 UNRESOLVED → resolved (model-conditional) | STANDS | all four 1805.09942 quotes verbatim [FT p. 5]; ±2 V [p. 2]; 2.06σ and "charge collection efficiency (electrons vs. electron-holes)" [pp. 5–6] ✓; paper names only "a solid mass of pure Ge with a thin layer of GeO₂" and "simple potentials … tuned parameters", no TRIM output or binding energies: omission CONFIRMED |
| 34 | §2.4, §2.6, §3.10, §4.5 compute-formulate specs | §3.10 STANDS WITH CORRECTION (W); others STANDS | LE-137 Method B input: ph.x with `K_POINTS gamma` (scf.in) is not supported (Γ-trick wavefunctions; use `automatic 1 1 1 0 0 0` or phcg.x); and xq = G_sc is equivalent to q = Γ of the supercell, so 𝔣(q) at G_sc comes from the G-components of one Γ response, not one ph.x run per G_sc |

Scope 2 (claims that a published paper is wrong or misprinted): **none is made.** The attribution and omission claims are rated in rows 13, 21, 33
(CONFIRMED). The definitional point in D-7 (2303.02196 uses ε = 3.8 eV) is quoted via WP5-AUD and the referee reports. 2303.02196 was not fetched here: UNRESOLVED by me,
not disputed.

## 1. Detail on the load-bearing corrections
**1.1 L38 (row 6).** With f ≡ (1 − e − η)S_ER, S_ER = 1 − X + rg (X ≡ X^{oth}_ER), sympy gives ∂f/∂x = (1+g)(1−δ), ∂f/∂δ = (1+g)(1 − d′_NR) (✓, C3), and
f(x = δ = 0) = f₀(e), linear in e, with f₀(0) = g(r−1)(1−y)(1 − X/(1+rg)) and f₀(1−y) = (1−y)X(1+g)/(1+rg). **f₀|_{r=1} = X·e exactly.** C3 samples X ∈ [0, 1] only.
Since WP7-E-v3 (B-c) and LIMITS L36 state that X contains ΔZPE "of either sign", the exact bound needs X^{oth}_ER ≥ 0. Counterexample: g = 1.047, r = 1.1, y = 0.3,
X = −0.01: f₀ = +0.067 at e = 0.06 but −0.0055 at e = 0.69. In the physical region (e ≲ 0.06, |X| ≪ 1) the violation is O(|X|e) ≲ 10⁻³, so the bounds 0.055/0.064 are
unaffected. **Owed text (OC-5 Validity):** append "X^{oth}_ER ≥ 0 (else the bound holds to O(|X^{oth}_ER|E_st/ω))".

**1.2 Signed sampler (row 11).** Let R ≡ Σ|K|/ΣK. Normalised by ΣK, the signed estimator's second moment is R²·𝔼_{|K|}[f²], exactly R² times that of the
|K|-weighted estimator. Its variance is R²𝔼_{|K|}f² − ⟨f⟩²_K, which is not bounded by R²·Var_{|K|}f (counterexample f ≡ 1: 0 → R² − 1 = 0.21). **Owed text (OC-9):**
"report the second-moment factor (Σ|K|/ΣK)²" in place of "variance factor", and "only the class sum Σ_iK_iP_i(N_eh) must be non-negative for every N_eh".

**1.3 Bimolecular tail (row 18).** Under (CW5-2), r_g counts E_pairs + E_X. A formation step F + F → X moves E_g − E_x^b from E_pairs to E_X and releases only
E_x^b. V3 (C_X n₀ = 1, k_X↓ = 10⁻³/t₀): n_F(t) = 1/(1 + t/t₀) to 10⁻⁶, but r_g = 0.9997, 0.992, 0.909 at t/t₀ = 1, 10, 100, i.e. r_g ≈ e^{−k_X↓t}.
**Corrected (ii), either:** (a) add the hypothesis k_X↓ ≫ C_Xn(t), so that formation is rate-limiting, r_g ≈ n_F and CW5's formula stands; **or** (b) "If the gap-energy *loss* is bimolecular (exciton–exciton annihilation, dn_X/dt = −γ_XXn_X²), then r_g ≈ 1/(1 + t/t₀), t₀ = 1/(γ_XXn₀); Auger
(C_An³) gives (1 + 2t/t₀)^{−1/2}. Bimolecular formation alone does not change r_g." The D-1 tail becomes 𝔶𝒢_gap t₀/t_win (annihilation) or 𝔶𝒢_gap(t₀/2t_win)^{1/2}
(Auger). The conclusion that NR ≠ ER because of track density survives. Check C6b must be replaced by one that integrates r_g, not n_F.

**1.4 Renewal (row 12).** (CW5-5) is an exact many-to-one identity. The step "entrance law into [E_g, x*] converges" needs: (a) a Markov chain in ln x whose
kernel converges to a stationary non-lattice kernel; (b) a summable perturbation (Σ_j sup|K_{x_j} − K_∞| < ∞ a.s.); (c) a finite mean of the killing time in the
threshold region. (a) and (c) are (r1′)–(r3′). (b) is missing; it holds for O(E_g/x) corrections because x_j decreases geometrically. With (r4′) = (b) stated and
a cited Markov-renewal theorem (for example Kesten 1974, or Alsmeyer's Markov renewal theorem), the [D] tag is acceptable. Without them, keep [D, sketch]. The LIMITS
"new (renewal)" row's "DERIVED (CW5-C5)" must not cite C5 as evidence: C5 tests toys (gamma(2), lattice, uniform fragmentation), not the branching limit.

**1.5 α_ohm spin counting (row 21).** For H_int = σ_zΣ_{kq,η}VΩc†c, S_X(ω) = 2π·2·(N_σVΩ)²ω/(1 − e^{−βω}). Leggett's X = ½ΣCx has S_X = J/2 = παω. So
α = 4(N_σVΩ)² = 4K, and Γ₁ = (Δ₀/E)²[S(E) + S(−E)] = 4πKΔ₀²coth/E, Black's form. 2009.03804's suppl. (S034) sums over η and (S035) uses the single-spin n₀.
(CW5-6) gives the same 4K. A both-spin K_both ≡ (n_bothVΩ)² = 4K gives α = K_both: the factor is 1, not 2.

## 2. CLOSED-AS-EXACT-GAP rows (scope 4)
Criteria: (1) the single missing step is truly single and truly missing; (2) the spec states what is computed, the approximation level, the method and convergence, and the pitfalls.
| Row | (1) single missing step | (2) spec: what / level / method+convergence / pitfalls | Ruling |
|---|---|---|---|
| LE-138 | ✓ ζ(E) on 50 meV bins | ✓ / G0W0 + SOSEX ✓ / parameters but **no convergence target** / ✓ (Z once) | ADEQUATE WITH ADDITION: state the tolerance (e.g. ζ(E) to 2% under N_G 250→350, bands 200→400) |
| LE-139 | ✓ osc_k m_k(E) | what ✓ / (H-BGK) / **no convergence**, **no pitfalls** (2 lines) | INSUFFICIENT: add k-sample size per bin, the EPW/GW rate source for Γ_k vs Γ_E, and the pitfall that (H-BGK) is itself an (R-k)-type closure |
| LE-141 | a **set** of 6 rates + n₀; acceptable as "the rate set" | (a)–(d) ✓ / effective-mass+BSE ✓ / **no convergence** / pitfalls only via measurement | INSUFFICIENT: add convergence (k-mesh/BSE bands for exciton levels, central-cell cell size), the pitfall from row 18 (which bimolecular channel), and the T-dependence at 10–50 mK |
| LE-129 | ✓ λ_eff, E_reorg/ε^{hop} to ±5% | via §3.2 (convergence 30/40/50 Ry, 64→216 atoms, pitfalls ✓) | ADEQUATE |
| LE-130 | ✓ independent P̄ or p | measurement proposal (3 observables) ✓; a-WSi CANNOT-CLOSE stated | ADEQUATE (measurement) |
| LE-131 | ✓ b_br | KMC, 10⁶ seeds / rates Γ_ij(t;Φ_ph) **not specified** (how Φ_ph is computed, which phonon transport) / no pitfalls | INSUFFICIENT: add the ballistic-phonon flux model, triggering-volume definition, finite-size and catalogue-completeness pitfalls |
| LE-144 | **two** (p_FH(T), p_surv) | ΔSCF hybrid + surface hopping ✓ / **no convergence, no pitfalls** | INSUFFICIENT: add cell-size and hybrid-fraction convergence; pitfalls: STE localisation depends on the hybrid fraction; decoherence correction in surface hopping |
| LE-145 | **three** (U_rel, (Γ_min, Γ_max), b_br) | FEM + MLIP-MD + fit / **no MLIP for epoxy specified, no convergence**, no pitfalls | INSUFFICIENT and not single; at most "U_rel spectrum and b_br" as two steps |
| LE-147 | ✓ (S_HR,R, ω_R, E_bar of the real defect) | by reference to §3.2 + ΔSCF; charged-defect pitfalls in §3.2 ✓ | ADEQUATE |
| LE-149 | ✓ the residual for omitted features | the run measures ΔP directly (good) but **no sample size/convergence**; TV itself is not computed (high-dimensional), so (CW5-12) is not what is evaluated | ADEQUATE WITH ADDITION: say the spec estimates ΔP, not TV, and give n_traj for a target ΔP |
| LE-151 | **two** (p_q·p_surv·f_opt; p_FH(T→0)) | computation "unchanged" (WP7-B2-v2 §9–§10) + measurement proposals ✓ | ADEQUATE as a measurement gap; "single" is wrong (two) |
| LE-22 (part) / LE-127 / LE-128 / LE-133 | not exact-gap rows | — | — |

## 3. Proposed LIMITS rows (scope 5)
| Row | Source quote (full text) | Validity / leading correction | Ruling |
|---|---|---|---|
| L30 ✎ | cond-mat/0310283 Eqs. (12) p. 3, (49) p. 7, (54), (61) p. 8 ✓; the "three + four + two" decomposition is the source's own sentence (p. 8) | Δ ≪ T ≪ θ_p ✓ (Eq. (53) condition); leading corrections ✓ except the Eq. (55) citation (row 26) | STANDS WITH CORRECTION: "DERIVED (exponent; prefactor [FT] Eq. (61))" |
| L32 ✎ | 0802.2404 Table I p. 2 and text p. 3 ✓; cond-mat/0507622 pp. 3, 6–7, 10 ✓ | low power ✓ ("single photon", "low-voltage"); OH ✓ | STANDS WITH CORRECTION: PECVD relabel (row 14); bulk-quartz relation is the source's secondary quote (its refs 13, 22), at PDF pp. 6–7 |
| L36 ✎ | 1805.09942 p. 5 quotes verbatim ✓ | model-conditional ✓ | STANDS |
| L37 ✎ | — | r_g𝒢_gap ≪ 1 ✓; "(CW5-4)" as correction ✓ | STANDS; once row 18 is applied, cite the annihilation/Auger tail as well |
| L38 ✎ | 1803.02903 (not re-read; prior [FT]) | (B-a), (B-b), (B-d), (B-c) with κ_cal(r) | STANDS WITH CORRECTION: add X^{oth}_ER ≥ 0 (§1.1). "REFEREED" should be recorded by the coordinator only after this R16 round, since OC-5 is a single-agent text |
| L42 ✎ | 2303.02196 not fetched here | 1σ bands; ⟨𝔮⟩ [E] | STANDS WITH CORRECTION: tag format (row 9) |
| new (α_ohm) | 2009.03804 Eq. (4) p. 4 ✓; K values p. 5 ✓; per-spin n₀ suppl. p. 14 ✓ | weak coupling ✓ (K ≪ 1: the source says it lets one "neglect Kondo-type strong coupling corrections") | STANDS WITH CORRECTION: the pitfall factor is 1, not 2 (row 21) |
| new (renewal) | key renewal theorem: correct for the single line ((σ²+μ²)/2μ² counts the crossing loss) | (r1′)–(r3′) + **(r4′)** missing | STANDS WITH CORRECTION (§1.4); do not cite C5 as evidence |
| new (gap release) | — | linear part ✓; "bimolecular → 1/(1 + t/t₀)" wrong mechanism | STANDS WITH CORRECTION (§1.3) |

## 4. Minor (N)
- §1.2 B-2 and OC-4: "≥ 1100" → "≥ 1112" (row 5). §3.3 Al "6%" → "5.6%". §3.4 σ conversion (row 24).
- §2.2 closure-table cell "size ≤ 2.7%" → "≈ 2.7% (Z part) [E]".
- §2.5 (CW5-4): "Σ_kw_k = 1" holds; the w_k are not positive in general (sequential F → X → B).
- §3.5(b), last sentence: unsupported identification with WP6's θ_𝒦; either derive or delete.
- §4.2 Prediction 4 restates (H-L3).
- C6b and C18 are tautological or bookkeeping checks; C6b should be replaced (row 18). C3 should sample X^{oth}_ER < 0 as well.
- §6 table row "C7 … variance factor" should say "second-moment factor".

## 5. Overall
Most of CW5 stands. The D-7 re-ruling (CONDITIONAL HV verdict), the D-1 exact form, the LE-150 resolution, the Andreev–Lifshitz flag, the α_ohm eigenphase
formula with its Born limit, and the T⁻⁹ exponent are confirmed by recomputation and by full text. **One sub-claim falls:** §2.5 (ii), "bimolecular
formation gives r_g = 1/(1 + t/t₀)". It needs either k_X↓ ≫ C_Xn or a bimolecular energy-loss channel; the qualitative NR ≠ ER conclusion survives. Three status upgrades need
an added hypothesis or a narrowed scope before they carry DERIVED: L38 (X^{oth}_ER ≥ 0), renewal (r4′), and L30 (exponent only). The signed-sampler variance
statement is false as worded and is easily fixed. Of the eleven exact-gap rows, five specs are insufficient on convergence or pitfalls (LE-139, 141, 131, 144,
145). LE-145, 144 and 151 also name more than one missing step.
