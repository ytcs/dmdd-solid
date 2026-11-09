# R16 / CW5: closure of the defect, TLS, cascade and low-energy-excess loose ends (WP7-T, WP7-E, WP5), with the GAP-LEE scope

Closure agent CW5, brief briefs/R16/CW5.md. Rows: state/LOOSE-ENDS.md §2 row CW5 (26 rows) plus the queued GAP-LEE scope (row "GAP-LEE" below).
Read: LOOSE-ENDS §1, §1b, §2, §3; returns/R14/WP5-AUD.md, referees/R14/REF-WP5-AUD-A.md and -B.md (cited by the brief), returns/R14/GAP-EF.md,
returns/R13/WP5-v4.md (§1–§6, §8, §9, §11, R8.1, IF-R13-4), returns/R12/WP7-T-v2.md, returns/R12/WP7-E-v3.md, returns/R12/WP7-B2-v2.md §9–§11,
returns/R13/WP8-F.md (4.2), returns/R13/WP8-R.md (G-R2 lines only), LIMITS.md (rows cited), CONVENTIONS.md (incl. R8/R13 amendments), NOTATION.md
(greps), CONTROLS.md, code/ENV.md, state/CORRECTIONS.md §18 (renames applied when quoting WP7 returns: δ → δ_coll, r → r_coll, g → g_Luke, y → y_ion,
κ → κ_cal, 𝔵 → 𝔮, d → d_tun, ε_ij → ε^{hop}_ij, c → 𝔠). No other referee report was read.
**Checks:** code/CW5/checks.py (sympy + numpy + scipy), **21/21 PASS in 19 s**, cited CW5-Cn. WP5-AUD's FOM function is copied (not imported).
**Literature** (lit.py into literature/papers-CW5/; PDF pages; PDFs deleted at the end, arXiv API records kept, CW5-C18): 0802.2404 (O'Connell et al.),
cond-mat/0507622 (Martinis et al.), 1805.09942 (SuperCDMS, ²⁰⁶Pb), 2009.03804 (Maillet et al.), 1705.01108 (Müller–Cole–Lisenfeld), cond-mat/0310283
(Pushkarov), all [FT]. Crossref for Andreev–Lifshitz. **No heavy computation was run**; no value here is [CALC]. Tags per CONVENTIONS §12.
Labels introduced here carry the prefix CW5- (CONVENTIONS §14). Status: CLAIMED (one agent), pending R×2.

## 0. Closure table
| Row | Item (short) | Status | Where |
|---|---|---|---|
| LE-22 | R×2 on WP5-AUD: consolidated rulings and corrections | CLOSED (corrections owed; WP5-AUD REFEREED once applied) | §1 |
| LE-23 | signed seed sampler extended to defect seeds; never clip | CLOSED (algorithm text owed to WP5) | §2.1 |
| LE-138 | R1: ii rate beyond first order in W | CLOSED-AS-EXACT-GAP (size ≤ 2.7% on ε_eh, absorbed by calibration) | §2.2 |
| LE-139 | R2: (R-k)/(R-k′) error | CLOSED-AS-EXACT-GAP (bound derived under a relaxation-time hypothesis) | §2.3 |
| LE-140 | R3: TDDFT close-collision kernel | CLOSED (spec with θ_LZ nuisance) | §2.4 |
| LE-141 | R6 / G-E10: excitons, shallow trapping, luminescence; zero-field gap-energy release law (GAP-LEE part a) | CLOSED-AS-EXACT-GAP | §2.5 |
| LE-142 | R8: dense tracks (θ_dense), thermal spikes | CLOSED (MD/EMC spec) | §2.6 |
| LE-143 | renewal asymptotics [D, sketch] | CLOSED: leading term DERIVED; b_N and variance stay [D, sketch] | §2.7 |
| LE-127 | G-T1 first-principles α_ohm | CLOSED (formula derived [D, sketch], Born limit = 2009.03804 [FT]; spec) | §3.1 |
| LE-128 | G-T2 S_HR,k, barrier, λ_P of eV-release paths | CLOSED (derivation + spec; 64-atom NEB pilot formulated) | §3.2 |
| LE-129 | "frozen" verdicts OPEN | CLOSED-AS-EXACT-GAP (conditional verdict table; single missing number) | §3.3 |
| LE-130 | G-T3 P̄_STM, γ^{def}, 𝐩^{def} of films | CLOSED-AS-EXACT-GAP ([FT] table; separation P̄ vs p missing) | §3.4 |
| LE-131 | G-T4 interacting TLS, spectral diffusion, avalanches; WP5 R4 | CLOSED-AS-EXACT-GAP | §3.5 |
| LE-132 | G-T5 Andreev–Lifshitz original | CLOSED (citation verified and flagged; original not read) | §3.6 |
| LE-133 | L30 D_T ∝ T⁻⁹ [D, sketch] | CLOSED: DERIVED | §3.7 |
| LE-134 | G-T6 crowdion polaron narrowing, Al SIA, L31 | CLOSED (formula + spec) | §3.8 |
| LE-136 | tanδ₀ of a-SiO₂ | CLOSED ([FT] values) | §3.9 |
| LE-137 | DM–TLS core: DFPT δρ_κ of a-SiO₂ TLS cores | CLOSED (spec, rtsc layout) | §3.10 |
| LE-144 | G-E1 ionic targets (E_el → E_st) | CLOSED-AS-EXACT-GAP | §4.1 |
| LE-145 + GAP-LEE (b) | G-E2/G-F3 predictive LEE model | CLOSED-AS-EXACT-GAP (bound + structure derived; p(E) and U_rel missing) | §4.2 |
| LE-146 | G-E5 track recombination, plasma phase | CLOSED (formula + spec) | §4.3 |
| LE-147 | G-E7 carrier-driven defect reactions | CLOSED-AS-EXACT-GAP | §4.4 |
| LE-148 | G-E8 pocket size distribution | CLOSED (MD spec) | §4.5 |
| LE-149 | G-E9 (H-E6) residual | CLOSED-AS-EXACT-GAP (exact criterion + TV bound) | §4.6 |
| LE-150 | L36 TRIM inference UNRESOLVED | CLOSED ([FT]: the inference is model-conditional) | §4.7 |
| LE-151 | D2/D5 colour-centre and bond-breaking yields | CLOSED-AS-EXACT-GAP (no [FT] values; measurement proposal) | §5 |
| GAP-LEE | queued scope: (a) zero-field gap-energy release law; (b) predictive LEE | (a) in §2.5, (b) in §4.2 | §2.5, §4.2 |

---
## 1. LE-22: the two referee reports on WP5-AUD, reconciled
**Item.** REF-WP5-AUD-A and -B (both hostile, isolated; both re-ran AUD-C1…C11, 27/27) rule on WP5-AUD's 17 defects. They agree on most rulings and
disagree on three load-bearing points. Each disagreement is ruled here by a check, not by a vote. CW5 cannot edit WP5-AUD or WP5-v4, so "corrections
applied" means: the exact replacement texts are listed (Owed corrections, rows OC-1…OC-12) and the coordinator applies them.

**1.1 Rulings that both referees accept (STANDS):** A-1…A-16 applied faithfully; IF-R13-2 and (AUD-1) (independently re-derived by both with sympy);
IF-R13-3 quench protocol (138 eV per 4096-atom cell); D-5 (θ_𝒦 interior condition); WP8-F rulings F-a…F-i; WP8-R (a) NO-GO and (d) CONDITIONAL
(ζ_O,min 0.13/0.24/0.44). These need no correction.

**1.2 Points corrected by both, with the merged text.**
- **D-1 size (S).** Both: the omission of E_pairs(t_win) + E_X(t_win) from D′ is real, but "+0.28" is the first-order term of a deficit that is not
  small. CW5-C1: with 𝒢_gap ≡ E_g/ε_eh = 0.312 and 𝔶 = 0.102, Y_H(r_g = 1)/Y_H(r_g = 0) = (1 − 𝔶𝒢_gap)/(1 − 𝒢_gap) = **1.407** (1.400 with the source's
  ε = 3.8 eV); the first-order term is 0.280. Merged fix: keep E_pairs + E_X inside D′ of the **exact** ratio, split the release fraction by recoil type,
  and charge excitons E_g − E_x^b each (OC-1). §2.5 derives the law for r_g(t) and corrects the definition of P_g.
- **"L36–L38 unaffected" (W).** Both: unsourced. Merged: tag [E] with a drift-time estimate, t_drift ≈ 1 cm/(10⁶ cm s⁻¹) = 1 µs at 4 V/cm (v_d from
  WP7-E-v3 C15) against phonon windows ≳ 100 µs [E]; the Ge datum (1805.09942) is also biased, ±2 V iZIP [FT, PDF p. 2], so the same estimate applies.
- **D-2 (W → N).** Both: (E7) already counts 𝒲_bias(t_pr) once, inside NTL heat; AUD-C3e is a tautology. B adds that "weighted by ϵ_NTL" is
  unsupported. Merged guard sentence for A-12 only (OC-2).
- **B-1 (S).** A: parts (i)–(iv) leave [ω_op, E_th^{ii}] unassigned and omit ℋ_nuc. B: E_s^{(0)} must be the end-state zero-point level ω_s/2, not the
  projection of the t = 0 configuration (which contains the configurational E_st); ΔZPE must be excluded. Both apply (OC-3).
- **B-2 (W).** Both: N_eh ≤ 30 truncates the 0.89 keV distribution (⟨N_eh⟩ = 29.7, σ = 10.5; CW5-C17); the 6% variance error is Gaussian-only
  (√(2/(n − 1) + κ_ex/n): 9.0% at κ_ex = 2, n = 500; ≥ 1100 trajectories for 6%); E_r in 2303.02196 is kinematic, not the 0 V phonon energy (OC-4).
- **L38 status (W).** A: (B-b) r_coll ≥ 1 must be a stated hypothesis. B: the C2b scan is "observed"; its closed-form proof makes the bound DERIVED.
  CW5-C3 encodes B's proof in sympy: with f ≡ (1 − E_st/ω − η^φ_NR)(1 − X^{oth}_ER + r_collg_Luke), ∂f/∂x = (1 + g_Luke)(1 − δ_coll) ≥ 0,
  ∂f/∂δ_coll = (1 + g_Luke)(1 − d′_NR) ≥ 0, and at x = δ_coll = 0 f is linear in E_st/ω with non-negative end values. **DERIVED** for r_coll ≥ 1 (OC-5).
- **Roundings and tags (N).** D-12: one rounding, N_a ≳ 272–543. D-13: p_surv ≲ 0.47 (0.4748), not 0.475. §7 tags: g_Luke [FT], y_ion [E], κ_cal and
  r_coll [D] on [E] inputs; "[FT via X]" → "[FT] (source, as read by X)"; the 300 eV Y/F bracket is constructed [E]. C3c, C3e are consistency
  identities, not derivations (OC-6).

**1.3 The three disagreements, ruled.**
| Point | REF-A | REF-B | Check | Ruling |
|---|---|---|---|---|
| D-7: WP8-R (c) HV NO-GO "ceiling ≤ 1.999" | FALLS: with the source ε = 3.8 eV the 1σ corner gives 2.014 > 2; Table II bands are 1σ | SWC: 1.999 holds only at ⟨𝔮⟩ = 0.873 (unstated); 1.763 at ⟨𝔮⟩ = 1; interpolated 300 eV point 1.44 | CW5-C2 reproduces 1.9986 (ε 3.75), **2.0136** (ε 3.8), 1.7626 (⟨𝔮⟩ = 1), 2.015 (220 eV, joint 2σ), F_NR* = 0.275/0.399/0.498 (ε 3.75) and 0.282/0.408/0.508 (ε 3.8) at ⟨𝔮⟩ = 1/0.873/0.8 | Both are right on different inputs. The **robustness claim falls**; the **(c) verdict becomes CONDITIONAL**, firm at central values and at E_R ≲ 220 eV (1σ). Merged text OC-7 |
| C7c′ "C7l fails: 2.18" | energy-matched Y(300) = 0.12: 1.993 / 2.008 | 1.99 (WP8-R's F_ER, ⟨𝔮⟩ = 1) to 2.40 (F_ER 0.119, ⟨𝔮⟩ 0.873) | CW5-C2: 1.9926 / 2.0076 | "fails" → "marginal" (OC-7) |
| D-4: r_coll prior width | σ_ln 0.1 (the WP8-R bound "≲ 0.2" read as 2σ); "sign open" contradicts (B-b) | 0.1 is the literal reading; 0.2 needs a stated reason; state the C8b conditions | none needed: both agree the literal reading is 0.1; no derivation of 0.2 exists | **σ_ln = 0.1 [E]**; sign open in the profiled object (i); the conditional bound (ii) is reported on the r_coll ≥ 1 branch only; C8b conditions stated (OC-8) |
**Status.** With OC-1…OC-8 applied, WP5-AUD is REFEREED (R×2). Its rulings 2 (IF-R13-2), 3 and 3′(c) stand unchanged. WP5-v4 then carries "audited (R14)
+ audit refereed (R14)"; the coordinator records WP5-v4 as REFEREED after IF-AUD-1…8 and OC-1…OC-8 are applied (IF-CW5-9).

---
## 2. WP5 rows
### 2.1 LE-23: signed seed weights at phonon poles, extended to defect seeds [D]
**Item.** WP7-T-v2 IF-T9 exports the seed weight (π|B|²/η_pole)δ(x) − 2πIm(a*B)δ(x) of WP7-T-v2 (1.3) to the cascade. Its second term has no sign.
WP5-v4 §1.5 already samples signed K_ν for the Fano term; IF-R13-4 asks that defect seeds use the same rule. **Derivation.** For weights K_i of any sign
over seed classes i, with Σ_iK_i = K_tot > 0, draw i with probability |K_i|/Σ|K| and score w_i = sign(K_i)Σ_j|K_j|. Then E[w f(i)] = Σ_iK_if(i) for every
observable f: the estimator is **unbiased**, and its variance is larger by at most (Σ|K|/K_tot)² (CW5-C7: exact 1.550, signed 1.547, factor 1.21).
Clipping negative weights and renormalising gives 1.952 in the same toy, a bias of +26%. The physical constraint is on the total, not on each class:
P(N_eh|Λ) = Σ_iK_iP_i(N_eh) must be non-negative, and it is whenever |Im(a*B)| ≤ |B|²/(2η_pole) per q bin. **Owed text** (OC-9) for WP5 §1.5 and §3.1.
**Book note.** Interference terms in a response are signed; only the sum over all classes is a probability. A Monte Carlo that clips them is biased.

### 2.2 LE-138: R1, the ii rate beyond first order in W [exact gap]
**Strongest derived statement.** The two rate definitions of 0812.2923 differ by the residue Z_qp (a global factor ≈ 0.8, θ_Z) and by W versus W_R.
GAP-EF's reduced cascade puts the whole ii rate into λ_ph ∝ 1/Γ_ii (IF-EF2). Hence any global factor ζ on Γ_ii shifts ε_eh by
d ln ε_eh/d ln λ_ph · ln(1/ζ). From GAP-EF (EF9), d ln ε_eh/d ln λ_ph = c₁βu/(ε_eh/E_g) = **0.12** for Si (CW5-C10), so Z_qp = 0.8 moves ε_eh by
**+2.7%** before calibration. Because 𝒜_ph is calibrated on Si ε_eh, the global part is absorbed. Only the **material dependence** of the R1 factor
survives, and it enters every other material as ±0.12·|Δ ln ζ| [E]. **Missing step.** The energy dependence of the ratio
Γ_ii^{NEGF}(E)/Γ_ii^{(W1)}(E) between E_th^{ii} and ≈ 10 eV. A constant ratio is absorbed; a varying ratio changes F_eh through (EF7). **Spec.** Si: G0W0
(BerkeleyGW) Im Σ_nk with and without Z_kn on the WP5 §2 grid (N_G ≈ 250, 200 empty bands, full-frequency ε⁻¹, 10³ k per 50 meV bin), plus the
second-order screened-exchange (SOSEX) vertex as the first beyond-GW term; output ζ(E) on 50 meV bins, then GAP-EF's solver with Γ_ii → ζ(E)Γ_ii.
Cost ≈ 3×10⁴ core-h [E]. Pitfall: Z_kn must be applied once, either to the quasiparticle weight or to the rate, never to both.

### 2.3 LE-139: R2, the energy-only reduction [bound under a stated hypothesis; exact gap above it]
**Hypothesis (H-BGK).** Momentum randomisation on an iso-energy surface is a Poisson process of rate Γ_k that leaves the carrier uniformly distributed on
the surface. Energy-changing events (ii, phonon loss) occur at rate Γ_E. **Derivation [D given (H-BGK)].** The probability that no randomising event
falls between two energy-changing events is w_mem = Γ_E/(Γ_E + Γ_k) (CW5-C16). So at the next energy-changing event the momentum law is
(1 − w_mem)·(uniform) + w_mem·(memory). For any cascade observable m_k(E) (mean pair number, its square, …) the reduction error per generation obeys

  |m_k^{true}(E) − m̄(E)| ≤ w_mem(E) · osc_k m_k(E),   osc_k ≡ max_k m_k − min_k m_k on the surface.                                             (CW5-1)

Summed over generations, the error is ≤ Σ_n w_mem(E_n) osc(E_n). Below ~1 eV above threshold, Γ_k (intervalley + acoustic, ~10¹³–10¹⁴ s⁻¹ [E])
≫ Γ_E, so w_mem ≲ 0.1 [E]. Above 3–5 eV in Si, Γ_ii ≳ Γ^{ph} and w_mem can reach ½. There the bound needs osc_k small, which is (R-k′).
**Missing step.** osc_k m_k(E) for Si between 3 and 8 eV, from the k-resolved n_gen = 2 subset that WP5 §2 already specifies for θ_{R-k}.
**Spec addition.** Report w_mem(E) from the same EPW/GW rates and osc_k on 50 meV bins; θ_{R-k} is then bounded by (CW5-1), not estimated.

### 2.4 LE-140: R3, the close-collision excitation kernel (compute-formulate)
**What is computed.** dP/dω_e(b_imp, E_coll): the distribution of electronic excitation energy left behind when two Si (or Ge) atoms collide at impact
parameter b_imp and relative energy E_coll. It feeds the §2 cascade as a stochastic event list. **Hierarchy level.** X sector at strong coupling
(WP0 Theorem D beyond its window): the nuclear trajectory is classical, electrons are time-dependent; first order in nothing.
**Method.** Real-time TDDFT with Ehrenfest nuclei (Qb@ll, Octopus or SALMON; QE has no production real-time code), 64–216-atom cells, the
projectile launched along random directions; excitations are counted by projecting the time-evolved orbitals on the ground-state KS conduction
manifold after the collision (t ≈ 20 fs). **Convergence:** time step ≤ 2 as near closest approach; grid ≤ 0.2 Å (≈ 40 Ry equivalent, ZBL-hard
pseudopotentials with semicore states for E_coll ≥ 1 keV); cell such that the wake does not re-enter (≥ 15 Å); 20–50 trajectories per (b_imp, E_coll).
**xc nuisance θ_LZ:** repeat a 10% subset with a hybrid (HSE) kernel and with surface hopping (decoherence-corrected) instead of Ehrenfest; independently
compute the Si₂ quasi-molecular diabatic couplings h_LZ by multireference CI and compare the Landau–Zener P_LZ = exp(−2πh_LZ²/(v_N|ΔF_LZ|)) with
the TDDFT crossing probabilities. θ_LZ is the spread. **Pitfalls.** Adiabatic xc misplaces level crossings (charge-transfer states), so the gap of
the distorted configuration is too small; Ehrenfest gives mean excitations, not a distribution (use the projection statistics, not ⟨E_el⟩); the
electronic friction of a classical MD must be switched off where this kernel acts (double counting). Cost ≈ 10⁶ core-h (WP5 §3.4).

### 2.5 LE-141 and GAP-LEE (a): excitons, shallow trapping and the zero-field gap-energy release law [D for the law; exact gap for the rates]
**Item.** WP5 R6 and WP7-E G-E10 leave exciton formation, shallow trapping and luminescence escape unquantified. GAP-EF §4 gave the prompt formulas
((EF12)–(EF14)). WP5-AUD D-1 showed that the zero-field heat ratio depends on how much created-pair gap energy has relaxed by t_win; the R14 referees
left that release law UNRESOLVED. This section derives it.
**Bookkeeping first (corrects WP5-AUD's P_g; OC-1).** Per created pair, the gap energy E_g ends in one of four places by time t: heat (ℋ_ph), a frozen trap
(E_trap), escaping light (E_esc), or still in E_pairs + E_X. D′ already contains E_trap and E_esc. D-1 must therefore add only the last part. Define

  r_g(t) ≡ [E_pairs + E_X](t)/(N_ehE_g),   P_g(t) ≡ 1 − r_g(t).                                                                             (CW5-2)

WP5-AUD's sentence "fraction returned to phonons" would count trapped and escaped energy twice. With (CW5-2), the exact zero-field ratio is

  Y_H(t_win) = (1 − δ_coll)·[1 − 𝔶𝒢_gap r_g^{NR}(t_win) − d′^{oth}_NR]/[1 − 𝒢_gap r_g^{ER}(t_win) − d′^{oth}_ER],   𝒢_gap ≡ E_g/ε_eh,                   (CW5-3)

with d′^{oth} ≡ (E_st(t_win) + E_trap + E_es^{trap} + ΔZPE + E_esc)/ω. It reduces to WP5-v4 (W11) when r_g = 0 and gives the first-order term
(1 − 𝔶)𝒢_gap r_g at r_g^{NR} = r_g^{ER} (CW5-C1b). Excitons carry E_g − E_x^b each, so r_g overstates E_X by ≤ E_x^b/E_g (Si ≈ 1.3% [UNVERIFIED E_x^b]).
**Hypotheses for the law.** (H-g1) Each created pair is in one of the states F (free carriers), X (free exciton), B_j (exciton bound to impurity j),
T_j (carrier trapped on level j, frozen at mK; WP7-E-v3 §2.1: thermal emission exponent 10⁴), D (droplet). (H-g2) Dilute tracks: formation is geminate
or with a fixed background partner, so every transition is first order in the pair's own state. (H-g3) Zero field.
**Theorem CW5-G [D given (H-g1)–(H-g3)].** With p(t) the occupation vector of (F, X, B_j) and dp/dt = Mp (M the rate matrix: k_FX, k_FT, k_XB,j, the
X decay k_X↓ with luminescence fraction η_X, the BX Auger rate k_B↓),

  r_g(t) = 𝟙ᵀe^{Mt}p(0) = Σ_k w_k e^{−γ_k^{gap}t},   Σ_kw_k = 1,   γ_k^{gap} = eigenvalues of −M,                                              (CW5-4)

and the asymptotic split is: trapped b_trap = k_FT/(k_FX + k_FT); light (1 − b_trap)·[k_X↓/(k_X↓ + Σ_jk_XB,j)]η_X; heat the rest (CW5-C6, exact to 10⁻¹²).
*Proof.* Linear ODE; the time integrals of the outgoing fluxes are −M⁻¹p(0). ∎ Consequences: (i) for t_win ≫ max 1/γ_k^{gap}, r_g → 0 and the D-1 term
vanishes; the gap energy that never becomes heat is b_trap + light, and it is already in D′. (ii) **Dense tracks break (H-g2).** If formation is
bimolecular, dn/dt = −C_Xn², then r_g(t) = 1/(1 + t/t₀), t₀ = 1/(C_Xn₀) (CW5-C6b): a power-law approach, so at t_win ≫ t₀ the D-1 term is
𝔶𝒢_gap t₀/t_win, not exponentially small. NR tracks are denser than ER clouds of equal ω, so **r_g^{NR} ≠ r_g^{ER} is derived, not assumed**: this
is REF-A's point made quantitative. (iii) Droplets (D) need n above the Si/Ge EHD threshold [UNVERIFIED values]; they are outside (CW5-4) and enter
as a separate nonlinear branch.
**Exact remaining gap (single missing step).** The rates k_FX, k_FT, k_XB,j, k_B↓, η_X and C_X at 10–50 mK in detector-grade Si/Ge (impurity densities
10¹⁰–10¹² cm⁻³), and n₀ of the NR track (from §4.5). **Computation spec.** (a) C_X(T): phonon-assisted cascade capture of an e–h pair into hydrogenic
exciton levels, with acoustic deformation potentials from EPW (the WP5 (W2) g^S), levels from G0W0+BSE (GAP-EF §4.3); (b) σ_BX and k_B↓: effective-mass
plus central-cell DFT for D⁰X/A⁰X, Auger matrix elements from BSE wavefunctions; (c) k_FT from GAP-EF (EF12) with 𝓃_j; (d) solve (CW5-4) per class,
and the bimolecular case on the cascade-end spatial distribution (mark 𝔪). Output r_g^{NR,ER}(t_win; T). **Measurement proposal.** Y_H at two
windows (e.g. 10 µs and 1 ms) in the same zero-field detector separates r_g from E_st^{rel}P_rel (WP7-E-v3 §6 "two windows"); a 0 V versus HV
comparison suppresses exciton formation by drift and isolates r_g. **Nuisance.** θ_X becomes type T on r_g^{NR}, r_g^{ER} separately (IF-CW5-2).
**Book note.** "How much of the gap energy is heat by the end of the window?" has an exact answer for any linear kinetics, (CW5-4). The physics is in
the rates. Dense tracks change the functional form, and that difference is what makes NR and ER heat ratios depend on the window.

### 2.6 LE-142: R8, dense tracks and thermal spikes (compute-formulate)
**What is computed.** θ_dense: the change of P(N_eh, ℋ | E_R) when carriers in a dense track interact (Coulomb, Auger, screening), and the failure of
the binary-collision + Markov reduction for dense NR cascades (thermal spikes, Ge). **Hierarchy level.** (B2) independence is zeroth order in
n_pair a_X³; the first correction is a Boltzmann carrier–carrier collision term. Thermal spikes are beyond the Markov ion transport (truncation 0).
**Method.** (a) Carriers: ensemble Monte Carlo with molecular-dynamics Coulomb forces among all carriers (EMC-MD with P³M), seeded with the
cascade-end distribution and the track geometry (mark 𝔪); screened ii and Auger as extra channels. (b) Lattice: MLIP-MD of the NR cascade (§4.5
cells) coupled to a two-temperature model for the electrons (electron–phonon coupling g_ep from EPW). **Convergence:** EMC-MD time step 0.1 fs,
P³M mesh ≤ 1 nm, ≥ 10³ tracks per (E_R, type); TTM grid ≤ 1 nm. **Output:** θ_dense as the ratio P(N_eh|E_R)_{interacting}/P(N_eh|E_R)_{(B2)} and ΔF_NR.
**Pitfalls.** The electronic stopping friction and the §2.4 kernel must not both act; carriers leaving the MD box must be continued in the §2 cascade;
the thermostat must not absorb spike heat early. Cost ≈ 10⁴ GPU-h (MD) + 10³ CPU-h (EMC) [E].

### 2.7 LE-143: renewal asymptotics; the leading term derived [D]
**Item.** WP5 §6.4 states n̄(ω) = ω/ε_eh + b_N + o(1) and Var N_eh = F_ehω/ε_eh + O(1), tagged [D, sketch] under (r1)–(r3).
**(a) Single-line renewal [D, textbook].** If a carrier loses iid amounts X_i (law F_loss, mean μ, variance σ², non-lattice) and N(E) counts the
losses until E is spent, the key renewal theorem gives E N(E) = E/μ + (σ² + μ²)/(2μ²) + o(1) and Var N(E) = σ²E/μ³ + o(E). CW5-C5 checks both
facts: a gamma(2) law reaches 0.75, and a lattice law leaves the periodic remainder 1 − {E/d}.
**(b) Branching cascade, leading term [D].** (W3) is not a single renewal equation, because an event splits the energy over three children.
*Tagged-unit (many-to-one) representation.* Give each ii event at energy x the weight 1, shared equally by the x energy units of the parent. Then the
pair number is N(E) = ∫_0^E du Σ_{j on the lineage of unit u} 1/x_j, and

  m(E) ≡ E N(E) = E · E_unit[Σ_j 1/x_j],                                                                                                     (CW5-5)

where x_j are the energies of the successive particles that carry a uniformly chosen unit. A unit moves to a child with the size-biased fraction law,
or leaves the lineage into the gap or a phonon. (CW5-5) is exact for any energy-conserving branching law (CW5-C5(c): uniform binary fragmentation,
N_ev = 2x − 1, reproduced as 11.05 ± 0.1 at x = 6).
*Hypotheses.* (r1′) at large x the fraction law of the lineage is scale-free: the kernel shape depends on x only through x/E_g → ∞ (true for the
power-law DOS of (H-EF3) once ω₀/x → 0); (r2′) the law of ln(fraction) is non-lattice; (r3′) it has finite mean.
*Statement.* Under (r1′)–(r3′), ln x_j performs an asymptotically stationary random walk with negative drift. By the renewal theorem in ln x, its
entrance law into the threshold region [E_g, x*] converges as E → ∞. The sum in (CW5-5) is dominated by that region, because high-energy terms are
O(1/x). Hence E_unit[Σ 1/x_j] → 1/ε_eh, i.e. **m(E) = E/ε_eh + o(E)** [D]. ε_eh is the reciprocal of the expected inverse energy accumulated along a
unit's lineage.
**What stays [D, sketch].** The constant b_N and the variance law need second-order renewal estimates for the branching walk, and the decay rate of the
lineage's dependence on its start (the seed memory, VER-WP5-A N2). GAP-EF C6 confirms them numerically (10⁻⁴). (r2′) fails for the one-mode (R-k) model
on the {E_g, ω₀} lattice, as WP5 says. **LIMITS/L23 owed text:** OC-10.

---
## 3. WP7-T rows
### 3.1 LE-127: the electron bath of a tunnelling defect, α_ohm from scattering phases [D, sketch; Born limit checked against [FT]]
**Item.** WP7-T-v2 G-T1 quotes a "Yamada-type" α_ohm = Σ_l(2l+1)(δ_l^R − δ_l^L)²/π² as [UNVERIFIED] and needs a first-principles route (crowdion, H,
TLS in W, Al, Nb, WSi). **Derivation.** (i) A defect in configuration L or R scatters conduction electrons with S-matrices S_L, S_R at E_F. In a common
channel basis (angular momentum about the defect centre, per spin), let e^{2iδ̃_ν} be the eigenvalues of S_RS_L†. (ii) Anderson orthogonality: the
many-electron ground states overlap as |⟨Ψ_L|Ψ_R⟩| ∝ (k_FL)^{−½Σ_{σν}(δ̃_ν/π)²} for a system of size L. CW5-C8 checks the exponent on a 1D
semi-infinite chain (one channel, δ = −arctan V at E_F): fitted 0.0309 against 0.0312, and 0.0203 against 0.0210. (iii) In the spin-boson form of
WP7-T-v2 (4.1)–(4.2), the bath overlap decays as t^{−2α_ohm}. Matching the two power laws [UNVERIFIED step: Nozières–De Dominicis long-time form]:

  α_ohm = (1/2π²) Σ_{σ} Σ_ν δ̃_ν²   (eigenphases of S_RS_L† at E_F).                                                                           (CW5-6)

**Limits.** (a) If both configurations are diagonal in the same l basis (a reorientation about a fixed centre), δ̃_l = δ_l^R − δ_l^L with degeneracy
2l + 1, and (CW5-6) is WP7-T's formula, now derived, including the spin sum. A displaced scatterer (a hop by d_tun) is **not** of this form, so the
quoted formula does not apply to crowdions or H hops; the eigenphase form (CW5-6) does. (b) Born: a ±VΩ contact coupling gives δ̃ = 2πN_σ(E_F)VΩ and
α_ohm = 4(N_σVΩ)² (CW5-C8b). This is 2009.03804's K = (n₀VΩ)² with Black's rate, 4πKΔ₀²coth(ε/2k_BT)/(ħε) [FT, Eq. (4), PDF p. 4], i.e. α_ohm = 4K
(WP7-T C6e), **provided n₀ is the per-spin DOS**. 2009.03804 fits K = 0.07 and 0.11 for Al-covered resonators [FT, PDF p. 5]. Pitfall: with a both-spin
n₀ the factor becomes 2.
**Spec (compute-formulate).** Route 1 (direct S-matrices): KKR impurity Green's function (JuKKR or AkaiKKR, full potential, l_max = 3–4) for the two
relaxed configurations embedded in the host; S_R S_L† in a common basis centred at the midpoint; (CW5-6). Route 2 (QE, rtsc layout): PBE supercells
of the two relaxed configurations (W: 54, 128, 250 atoms; ecut 60 Ry, SG15 W_ONCV_PBE-1.2.upf with semicore; Γ-centred 4³ → 2³ k as L grows;
Marzari–Vanderbilt smearing extrapolated to 0); Slater-determinant overlap of the occupied KS states, ln|⟨Ψ_L|Ψ_R⟩| versus ln L; α_ohm = −slope.
Pitfalls: k-sampling and smearing destroy the orthogonality catastrophe (overlap must be computed with fixed occupations at a common Fermi level); the
host relaxation must be identical except near the defect; spin-polarised hosts (Nb, W are not) need δ̃ per spin. Cost: route 2 ≈ 10³ GPU-h per defect [E].

### 3.2 LE-128: S_HR,k, barrier shape and λ_P of real eV-release paths (compute-formulate, with derivation)
**What is computed.** For a hop i → j of a close Frenkel pair (Si, Ge) or a split interstitial (Al), the inputs of WP7-T-v2 (4.2)–(4.3): the
Huang–Rhys factors S_HR,k of the modes that accept ε^{hop}_ij, the reorganisation energy E_reorg = Σ_kS_HR,kω_k, and the tunnelling exponent.
**Derivation of the quantities [D, harmonic about each minimum].** Let ΔR = R^j − R^i (both quenched minima, WP5-AUD §3.1 protocol) and e_k the
mass-weighted normal modes at the final minimum. Then ΔQ_k = Σ_I√M_I e_{k,I}·ΔR_I and S_HR,k = ω_kΔQ_k²/2 (ħ = 1). The line shape A_T(ε) of (4.2) follows by
FFT of e^{−𝒬^{sb}(t)} with J_loc = πΣ_kS_HR,kω_k²δ(ω − ω_k). The weak/strong criterion of WP7-T-v2 §4.2 is E_reorg/ε^{hop}. The tunnelling exponent is
λ_eff = ∫ds √(2(V(s) − E))/ħ along the mass-weighted minimum-energy path; the Phillips λ_P = (d_tun/2)√(2M_effV) is its two-parabola value. The
T → 0 ring-polymer instanton action 𝒮_inst = 2λ_eff includes corner cutting.
**Pilot (formulated, not run; code/CW5/LE-128/).** 64-atom Si cell, a ⟨110⟩-split interstitial and a vacancy 2–4 Å apart. QE pw.x/neb.x, PBE, SG15
Si_ONCV_PBE-1.2.upf (`@PSEUDO@`), ecutwfc 40 Ry (check 30/40/50), 2×2×2 MP k, fixed cell at the PBE lattice constant; CI-NEB with 9 images to
5 meV/Å; Hessians at both minima by finite displacement (0.01 Å, 384 SCFs each); then S_HR,k, E_reorg, λ_eff and the A_T of the path; one ring-polymer
instanton (i-PI + the §3.4 MLIP, 64–128 beads) to compare 𝒮_inst/2 with λ_eff. Cost: ≈ 900 SCFs ≈ 30 h on the 4-core box (over the 3 h limit), ≈ 2 h on
the fork GPU [E]. Production: 50 paths per material (WP7-T-v2 §4.6). **Pitfalls.** Charged close pairs need a charge-state choice and a
finite-size correction; the 64-atom cell compresses the pair's strain field (repeat at 216 atoms for one path); λ_eff depends on the end-state
assignment, so the same quench and E^{conf} table as p_st (T-1 condition (ii)) must be used.

### 3.3 LE-129: the "frozen" verdicts, restated as a conditional verdict [D for the criteria; exact gap]
WP7-T-v2 (4.3) with Γ_att = 10¹³ s⁻¹ and t_obs = 1 yr gives ln(Γ_attt_obs) = 47.2 (CW5-C9). **Strong coupling** (E_reorg ≳ ε^{hop}, no gap
suppression, ω_wellA_T ≈ 1): a release within t_obs needs λ_eff ≤ 23.6, i.e. V d_tun² ≲ 166 meV Å² for a Si-mass entity. **Weak coupling** (S = 1,
ω_p = 60 meV, ε = 1 eV): ln[1/(ω_wellA_T)] = 33.6, so λ_eff ≤ 6.8.
| Path | λ_P (WP7-T C14e) | weak coupling | strong coupling |
|---|---|---|---|
| Si close pair (V 0.1 eV, d 1.5 Å [E]) | 27.5 (harmonic) – 37 (quartic) | frozen | frozen unless λ_eff ≤ 23.6, i.e. ≥ 14% below the harmonic estimate |
| Al ⟨100⟩ SIA | 25 | frozen | marginal: frozen unless λ_eff is ≥ 6% below the estimate |
| H in Nb | 4.1 | relaxes | relaxes |
**Verdict.** "Frozen" holds for every eV-release path in the weak-coupling regime. In the strong-coupling regime it hinges on one number per path.
**Single missing step:** λ_eff (equivalently 𝒮_inst/2) and E_reorg/ε^{hop} of the actual path, to ±5%: the §3.2 computation.

### 3.4 LE-130: TLS parameters of specific films [FT table; exact gap]
| Film | Quantity | Value | Conditions | Source [FT] |
|---|---|---|---|---|
| Al/AlOx junction barriers | TLS density σ | 0.4–0.5 /(GHz µm²) ≈ 10² /(µm³ GHz) (2–3 nm barrier) | large (≈ 1 µm²) junctions | 1705.01108 PDF p. 13 |
| Al/AlOx junction barriers | p_max | 6–8 D | qubit spectroscopy | 1705.01108 PDF p. 13 |
| AlOx (strain-tuned single TLS) | γ^{def} | 0.1–1 eV | phase qubit, piezo bending | 1705.01108 PDF p. 14 |
| glasses (ensembles) | \|γ\| | ≈ 1 eV | acoustic experiments | 1705.01108 PDF p. 11 |
| AlOx junction | dipole d (charge e) | ≈ 0.13 nm (d/x ≈ 0.06) | qubit splittings | cond-mat/0507622 PDF p. 5 |
| AlOx junction | tanδ_i | ≈ 1.6×10⁻³ | qubit | cond-mat/0507622 PDF p. 6 |
| CVD a-SiO₂, a-SiNx; thermal/PECVD SiO₂, a-Si:H, SiNx | tanδ₀ | §3.9 | §3.9 | §3.9 |
σ = 10²/(µm³ GHz) is 2.4×10¹⁹ /(eV cm³) per unit E (CW5-C15). It is a density of strongly coupled TLS, not P̄_STM: the conversion needs the
(Δ_tun/E)² weight and a lower cutoff. **Strongest statement.** Loss measurements fix only the product P̄_STM p² (tanδ₀ = πP̄_STMp²/(3ε_rε₀)); for CVD
SiO₂ (tanδ₀ = 5×10⁻³, ε_r = 3.9 [E]) P̄_STM = 2.4×10²¹ (p = 1 D) to 6.6×10¹⁹ (p = 6 D) /(eV cm³) (CW5-C15), bracketing WP7-T's 1.4×10²⁰.
**Single missing step:** an independent P̄_STM (or p) for the same film. **Measurement proposal:** one film, three measurements: dielectric tanδ₀
(P̄p²), acoustic 1/𝔔_ph (P̄γ², WP7-T-v2 §2.3(a)), and the power-saturation or Rabi scale (p). Their ratio separates P̄, γ^{def} and p. γ^{def} is
then cross-checked by strain tuning. **CANNOT-CLOSE as data** for a-WSi and TES-adjacent SiO₂: no [FT] source was found in this round.

### 3.5 LE-131: interacting TLS, spectral diffusion, avalanches; WP5 R4 [three derived statements; exact gap]
- **(a) Spectral diffusion leaves the ensemble DM rate unchanged [D].** Inside the TLS band, S^{STM}(q,ω) of WP7-T-v2 (2.2) is flat in ω up to the
  thermal factor. A normalised spectral-diffusion kernel K_SD(ω − ω′) maps it to ∫K_SD S^{STM}dω′ = S^{STM} wherever ω is farther than the kernel width
  from the band edges. Spectral diffusion therefore changes single-TLS lines (qubit physics), not (2.4). Interactions shift the ensemble at
  O(C_TLS) = O(P̄γ²/ρc²) ≈ 3×10⁻⁴ (WP7-T C14b′) [E].
- **(b) Release spectra of maximum-entropy form [D given (H-ME)].** Theorem T-1 fixes two moments of 𝒦^{rel}: ⟨N_hop⟩ and E_st^{rel}. If nothing else
  is fixed (H-ME, [C]), the maximum-entropy energy law on E ≥ 0 is p(E) = e^{−E/E_slope}/E_slope with **E_slope = E_st^{rel}/⟨N_hop⟩** (CW5-C14). This
  turns WP5 R4's conjectured e^{−E/E_slope} into a statement with one testable prediction: E_slope is the mean release per hop. It is also exactly the
  type-T tilt θ_𝒦 of WP6.
- **(c) Avalanche criterion [D for a branching model].** Let each release trigger a Poisson number of further releases with mean b_br (phonon-mediated
  triggering). Then sizes follow the Borel law: mean 1/(1 − b_br), finite for b_br < 1. At b_br → 1 the law is P(s) ∝ s^{−3/2} (CW5-C13). Triggered
  annealing (R4) is the b_br ≳ 1 regime.
**Single missing step.** b_br: the probability that the phonons of one release trigger another within the triggering volume. It needs the barrier
density below the phonon energy and the ballistic phonon flux. **Spec.** KMC on the WP7-T-v2 §4.6 rate catalogue with phonon-pulse-dependent rates
Γ_ij(t; Φ_ph) (T-1 holds for time-dependent rates), 10⁶ seeds; b_br from the first-generation trigger count. CATALOG-B G12 stays open.

### 3.6 LE-132: Andreev–Lifshitz (1969) [literature check: citation verified, original not read]
cond-mat/0310283 ref. [11] is "A. F. Andreev and I. M. Lifshitz, Zh. Eksp. Teor. Fiz. 56, 2057 (1969)" [FT, PDF p. 14] (Sov. Phys. JETP 29, 1107,
[UNVERIFIED: no DOI exists before 1992]). Crossref confirms the authors' review: A. F. Andreev, I. M. Lifshitz, "Quantum Theory of Defects in Crystals",
Usp. Fiz. Nauk 102, 323 (1970), doi:10.3367/UFNr.0102.197010v.0323 = Sov. Phys. Usp. 13, 670 (1971), doi:10.1070/PU1971v013n05ABEH004235. Neither
text was read. **Two findings:** (i) the T⁻⁹ law (L30) is credited in cond-mat/0310283 to its refs [16, 17] (Pushkarov), not to [11] [FT, PDF p. 3];
(ii) after §3.7 the L30 kernel and T⁻⁹ law no longer depend on the original. **Flag:** every LIMITS/G-T5 citation of Andreev–Lifshitz is marked
"[UNVERIFIED, original not read; bibliography verified (Crossref)]" (OC-11). Row CLOSED as the brief's second alternative.

### 3.7 LE-133: D_T ∝ T⁻⁹ for a narrow-band defecton [D]
**Hypotheses.** (H-d1) Δ_dfn ≪ T ≪ θ_p ≡ ħc/2a (cond-mat/0310283 Eq. (12) [FT, PDF p. 3]): the band is uniformly populated, phonons are long-wave
(q ~ T/c ≪ 1/a); (H-d2) point-like defect and long-wave phonons; (H-d3) dilute defectons (defecton–defecton scattering neglected); (H-d4) one
phonon branch of speed c (several branches add).
**Step 1: one-phonon processes are kinematically forbidden.** A defecton absorbing or emitting a phonon q needs |ε^{dfn}(k + q) − ε^{dfn}(k)| = cq.
The left side is ≤ v_max q with v_max ~ aΔ_dfn ≪ c under (H-d1). So the leading process is two-phonon (Raman) scattering q → q′, ω′ ≈ ω.
**Step 2: the two-phonon amplitude is ∝ ω.** (a) Quadratic (elastic-inhomogeneity, "Rayleigh") coupling: A ∝ Λ q q′/(ρ√(ωω′)) ∝ ω. (b) The linear
deformation potential at second order has two time orderings with denominators ≈ ±ω. They cancel at leading order. CW5-C4 expands the sum on shell
for a tight-binding band: the survivor is [ε(k + q) + ε(k − q′) − ε(k) − ε(k + q − q′)]/ω², the **second difference** of the dispersion, which is
+2Ja²cos(ka) q q′ + O(q³). So A_lin ∝ γ²(q²/ρω)(Δ_dfn a²/c²) ∝ ω as well: the linear channel renormalises Λ but does not change the power.
**Step 3: phase space and momentum ineffectiveness.** The rate is ∫d³q d³q′ |A|² n_B(1 + n_B) δ(ω − ω′) ∝ ∫ω⁴|A|²n_B dω ∝ T⁷: three powers from the
number of phonons, four from the cross-section σ ∝ (qa)⁴ (cond-mat/0310283 Eq. (49) [FT, PDF p. 7]). Each collision changes k by |q − q′| ~ T/c ≪ 1/a
(Eq. (54) [FT, PDF p. 8]), so randomising k takes ~(1/(qa))² collisions: the transport rate is ∝ T⁷(Ta/ħc)² ∝ T⁹ (CW5-C4: log₂ ratio 9.000000).
**Step 4.** With band velocity v ~ aΔ_dfn/ħ, D_T = v²τ_tr/3 ∝ Δ_dfn²T⁻⁹:

  D_T = (a c/(3ασ₀))(ε^{dfn}(p)/θ_p)²(θ_p/T)⁹   (cond-mat/0310283 Eq. (61) [FT, PDF p. 8]; α a numerical constant, σ₀ the impurity/vacancy cross-section ratio).   (CW5-7)

**Limits and leading correction.** For T < Δ_dfn (effective-mass regime) the source's Eq. (55) applies instead. Defecton–defecton scattering gives
D ∝ 1/(xσ) (Eq. (11)) and dominates at x above its crossover. The localisation of Eqs. (17)–(18) removes band transport in strain gradients
|∇φ|a > Δ_dfn. **Status:** L30 "[D, sketch] (T⁻⁹)" → **DERIVED** (Proposed LIMITS rows).

### 3.8 LE-134: crowdion polaron narrowing and strain localisation (W); Al SIA and 1D glide (compute-formulate, with formulas)
**Formulas [D for linear coupling].** Hopping between neighbouring sites is dressed by the phonons that distinguish them:
W_eff = W exp[−S_pol(T)], S_pol(T) = (1/π)∫dω J_ph^{(Δ)}(ω)ω⁻² coth(ω/2T). Here J_ph^{(Δ)} is the spectral density of the difference coupling.
For acoustic coupling, J ∝ ω³ (WP7-T-v2 (4.1)), so S_pol(0) = J₀ω_D²/(2π) is finite and S_pol(T) − S_pol(0) = πJ₀T²/3. Above 15 mK, bulk W is normal,
and the ohmic electron bath renormalises adiabatically, W_r = W(W/ω_co)^{α_ohm/(1 − α_ohm)} [UNVERIFIED classic; consistent with the (Θ/ω_co)^α form
of cond-mat/9409105 Eq. (10) quoted in WP7-T-v2 §4.1(c)], with α_ohm from §3.1. Coherent motion needs W_r e^{−S_pol} > max(α_ohmΘ/2, |∇φ|a_lat).
Otherwise the crowdion hops incoherently, and near its vacancy it drifts (WP7-T-v2 §4.3(b)).
**What is computed and how.** (a) W crowdion: QE PBE (SG15 W_ONCV_PBE-1.2, semicore), 250-atom bcc cell, ecut 50 Ry, 3³ k, MV smearing 0.01 Ry; CI-NEB
along ⟨111⟩ for the Peierls profile (meV scale); Hessian of the crowdion core for S_pol; FK fit (μ_FK, V_P) for M_cr; strain-interaction energy with the
parent vacancy versus separation, giving R₀ directly instead of V₀ ≈ 1 eV [E]. (b) Al ⟨100⟩ dumbbell: NEB migration (108–256 atoms); di-/tri-
interstitial 1D glide by MLIP-MD at 10–100 K, extrapolated by instanton rates. **Convergence and pitfalls.** The Peierls barrier is ≲ meV per cell, so
k-point and smearing noise must be < 0.1 meV/cell: use fixed-smearing differences at identical k-meshes, extrapolate the smearing to zero, and check
with 4³ k. The FK mapping is valid only if the NEB profile is sinusoidal (check the harmonics). Cost ≈ 10⁵ CPU-h per material (WP7-T-v2 §3.4).

### 3.9 LE-136: tanδ₀ of amorphous SiO₂ [FT]
| Material (preparation) | tanδ (intrinsic, low power) | T, ν | Source [FT] |
|---|---|---|---|
| CVD a-SiO₂, 300 nm (deposited at 13 °C and 250 °C) | δ_i ≈ 5×10⁻³ | 25 mK, ≈ 6 GHz (LC) | cond-mat/0507622 PDF p. 3, Fig. 1 caption p. 10 |
| PECVD SiO₂ | 2.7–2.9×10⁻³ | ≤ 100 mK, ~6 GHz (CPW) | 0802.2404 Table I, PDF p. 2 |
| thermal SiO₂ | 3.0–3.3×10⁻⁴ (3.1×10⁻⁴ in text) | ≤ 100 mK | 0802.2404 Table I p. 2; text p. 3 |
| a-Si:H; SiNx (comparison) | 2.2–2.5×10⁻⁵ (LC); 1.0–2.0×10⁻⁴ | ≤ 100 mK | 0802.2404 Table I p. 2 |
| bulk quartz (secondary quote, OH-doped) | δ_i ≃ 1.5×10⁻⁵ + 0.25 C_OH | — | cond-mat/0507622 PDF p. 6 (its refs 13, 22) |
**Saturation and thermal factor.** These are the low-voltage limits (single-photon level), so they are power-unsaturated. Thermally, tanh(hν/2k_BT) =
0.99999 at 25 mK and 0.894 at 100 mK (6 GHz; CW5-C15), so tanδ₀ = tanδ_i/0.894 for the 0802.2404 values if they were taken at 100 mK (the source says
"near 100 mK", PDF p. 3). **Reading.** a-SiO₂ tanδ₀ spans 3×10⁻⁴ (thermal oxide) to 5×10⁻³ (CVD), correlated with OH content (cond-mat/0507622 p. 6).
For a bulk a-SiO₂ target the OH-dependent bulk value applies, and it is lower. Use **tanδ₀ = 3×10⁻⁴ (thermal) and 5×10⁻³ (CVD)** as the bracket
for films, and bulk fused silica as preparation-specific (GAP: no [FT] bulk low-power mK value found). Owed L32 text: OC-12.

### 3.10 LE-137: the DM–TLS core vertex from first principles (compute-formulate)
**What is computed.** 𝔣^{def}_e(q) = ⟨R|n_e(q)|R⟩ − ⟨L|n_e(q)|L⟩ for real a-SiO₂ TLS (WP7-T-v2 (1.1)), replacing the rigid-ion core f = Z_O = 8. This
removes the three caveats: valence redistribution, macroscopic screening of the O dipole, and the single geometry. **Hierarchy level.** GS sector,
density row, n_D = 0, adiabatic (O(κ_BO²) corrections), scr = DFPT (the self-consistent adiabatic density; WP7-T-v2 §1.5: no extra ε⁻¹).
**Method A (preferred, nonperturbative).** Two pw.x SCF runs on the relaxed L and R configurations of the same glass cell. 𝔣_e(q) = FFT of
ρ_R(r) − ρ_L(r) at the cell's reciprocal vectors q = G_sc. This is exact at first order in the DM coupling and keeps all orders in the atomic
displacement (q·d ~ 1 at q ~ 1–2 keV, where DFPT's linearisation errs by O((q·d)²)). **Method B (DFPT, for the host relaxation field).** ph.x at
supercell-commensurate q with nat_todo restricted to the core atoms, fildvscf/fildrho on; vertex Σ_Iδρ_κ(q)·(u_I^R − u_I^L). **Key pitfall (WP7-T-v2
§1.5 scope).** The physical vertex is the full finite-q improper response including the G = 0 Hartree component. At q = G_sc ≠ 0 a periodic SCF or
DFPT density contains it. Below 2π/L_cell, however, the periodic cell imposes zero macroscopic field, which gives the Born (proper) dipole. There
the long-range part must be added analytically: 𝔣_e(q) ≈ 𝔣_e^{sc}(q) − iq·Δ𝐩_e(1 − 1/ε_∞(q̂)) [D, sketch]. Never rebuild δρ_κ from Z*_κ.
**Inputs and grids (code/CW5/LE-137/, rtsc layout).** 216-atom a-SiO₂ cells (72 SiO₂) from the WP7-T-v2 §2.7 MLIP-quenched glasses with NEB-identified
TLS (ΔE < 5 meV); PBE, SG15 Si/O ONCV 1.2 (`@PSEUDO@`), ecutwfc 80 Ry (O; check 70/80/90), ecutrho 320 Ry, Γ only (L ≈ 15 Å), conv_thr 10⁻¹⁰; |q| from
0.42 Å⁻¹ (≈ 0.8 keV) to 5 Å⁻¹. **Convergence.** 𝔣(q) stable to 2% under ecut +10 Ry and cell 216 → 648 atoms for one TLS; ensemble average over ≥ 10²
TLS for ⟨|𝔣|²⟩ to 10%. **Output.** ⟨|𝔣^{def}_e(q)|²⟩ on the WP7-T-v2 §2.7 q-grid, the Re(a*B) of off-centre cores, and the ratio to the rigid-ion value.
**Cost.** Method A: 2 SCFs per TLS ≈ 1 GPU-h each on the fork [E]; 10² TLS ≈ 2×10² GPU-h; Method B ≈ 10× that.

---
## 4. WP7-E rows
### 4.1 LE-144: ionic targets, the electronic route to stored energy [D for the ledger; exact gap]
**Item.** In alkali halides and other ionic crystals, a self-trapped exciton (STE) can convert into an F–H pair within ps (Pooley–Hersh mechanism
[UNVERIFIED]), so E_el → E_st is **prompt**. This contradicts the "post-prompt cross-channel" assignment of WP7-E-v3 Theorem E-2 for these materials.
**Derivation.** Add the cascade type "STE" to (W3) with a branching kernel k_FH (→ F–H close pair, energy E^{conf}_{FH}) against radiative and
nonradiative STE decay. Per ER deposit ω, the mean stored energy at t_pr is

  ⟨E_st^{el}⟩/ω = (⟨N_X⟩/ω)·p_FH·p_surv·E^{conf}_{FH},   ⟨N_X⟩/ω ≡ 1/ε_X (energy per exciton),                                                     (CW5-8)

consistent with WP7-B2-v2 (B2.9.1) Y_CC(eh, E) = ⟨N_x⟩p_FHp_survf_opt. The ER heat deficit enters d′_ER (so the ER calibration of ionic crystals is
not deficit-free), and the NR/ER ratio of WP5-v4 (W11) acquires ⟨E_st^{el}⟩ in **both** channels. **Single missing step.** p_FH(T) at mK and p_surv of
the close F–H pair against tunnelling recombination. **Spec.** STE and F–H adiabatic surfaces by constrained-occupation hybrid DFT (QE, HSE or PBE0,
ΔSCF, 64–216-atom NaI/LiF/CsI cells), conversion by surface hopping (≈ 10⁵ CPU-h, as WP7-B2-v2 §9); p_surv by the §3.2 path machinery (close-pair
tunnelling at mK). Owed note to Theorem E-2 (IF-CW5-7).

### 4.2 LE-145 and GAP-LEE (b): a predictive low-energy-excess model [bound and structure D; p(E) and U_rel missing]
**Item.** There is no predictive LEE rate (WP7-E-v3 G-E2, WP8-F G-F3). The data are mixed: in a glued crystal the rate is "more than two orders of
magnitude larger", with "time constant of 6–10 d" in the "3–38 and 30–85 eV" bins (2208.02790); "none of these tests have shown a significant effect"
under adjustable stress, with "the cracking of the epoxy used to glue the Ge-NTD" as a leading hypothesis and "sudden increases … after warming-up the
detectors above 10 K" (2202.05097); and "a single exponential does not sufficiently describe the time-dependent rate (χ²/(dof) = 4192/68)" (2208.02790).
All quotes [FT] as read in WP7-E-v3 §3.3; not re-read here.
**Hypotheses.** (H-L1) The LEE source is a reservoir of relaxable elastic energy U_rel stored at cooldown, in the crystal, the glue and the holder
interfaces. (H-L2) It relaxes by thermally or quantum-activated local events whose rates are spread flat in ln Γ over [Γ_min, Γ_max] (as WP5 §4,
WP7-T §4.5). (H-L3) The event energies follow a law p(E) (avalanche-type, §3.5(c)) that does not change with time.
**Derived statements.**
- **(i) Sum-rule bound [D, energy conservation; T-1 for closed chains].** Over any interval, the visible LEE energy cannot exceed the collected share of
  the elastic energy released then: ∫_{t₁}^{t₂}dt∫dE E·dℛ_LEE/dE dt ≤ ϵ_coll[U_rel(t₁) − U_rel(t₂)] + (event-seeded releases, (E14) source (i)).
- **(ii) Time law [D given (H-L2)].** dℛ/dt ∝ 1/t for Γ_max⁻¹ ≪ t ≪ Γ_min⁻¹ (CW5-C13), so the energy released per e-fold of time is
  U_rel/ln(Γ_max/Γ_min). A finite Γ_max⁻¹ (days) bends the 1/t law into the "sum of exponentials" the data prefer.
- **(iii) Predictive form [D given (H-L1)–(H-L3)].**

  dℛ_LEE/dE dt = [ϵ_coll U_rel/(ln(Γ_max/Γ_min)⟨E⟩)]·p(E)/t,   p(E) = E^{−τ_av}e^{−E/E_cut^{av}}/𝒩,   τ_av = 3/2 at critical branching (§3.5(c)).   (CW5-9)

  Prediction 1: the LEE rate scales with U_rel, i.e. ∝ σ²V/Y of the relaxing component. A glue layer with thermal-mismatch stress σ ≈ Y_g∫Δα dT
  dominates a clamped crystal: (2208.02790)'s factor > 10² is a ratio of U_rel, testable by FEM. Prediction 2: the clock resets when the relaxing
  component is warmed above its creep temperature (the "> 10 K" increases of 2202.05097). Prediction 3: a stress applied to the crystal bulk adds
  little U_rel if the bulk does not creep, which is consistent with 2202.05097's null if the source sits in the NTD glue. Prediction 4: spectral
  shape and time law factorise, so the spectrum shape is time-independent.
**Exact remaining gap (single missing step).** U_rel and its rate spread (Γ_min, Γ_max) for a given holder and glue, and the branching ratio b_br
that fixes τ_av and E_cut^{av}. **Spec.** (a) FEM of cooldown stress (crystal, glue, holder; C(T), α(T) from data) giving U_el per component, with the
relaxable fraction from low-T dynamic mechanical data of the glue; (b) MLIP-MD of a crystal/epoxy interface (10⁶ atoms, 1–10 K) for the event-energy law
and b_br; (c) fit (CW5-9) jointly to the 2208.02790 bins. **Measurement proposal.** Two identical crystals, one glued and one clamped, with a measured
glue volume; the rate ratio at fixed t after cooldown tests Prediction 1 without free parameters once U_rel is computed. **Nuisances:** θ_bg,𝔠 type A,
plus θ_U (M, on U_rel) and θ_τ (Δ, τ_av ∈ {3/2, fitted}) (IF-CW5-2).
**Book note.** The LEE is not predicted from first principles here. What is predicted is how it scales: with stored elastic energy, with 1/t, and with a
time-independent spectral shape. Each prediction can be falsified with existing holders.

### 4.3 LE-146: track recombination and the plasma phase [D for the loss formula; spec]
**Derivation [D].** Take (H-p1) a cylindrical Gaussian track of line density λ_L and initial radius r₀, (H-p2) ambipolar diffusion D_a at zero field,
and (H-p3) Auger loss C_An³ to first order. Then n = λ_L e^{−ρ²/s}/(πs), s = r₀² + 4D_at, ∫n³dA = λ_L³/(3π²s²), and the fraction of carriers lost is

  f_A = C_Aλ_L²/(12π²D_ar₀²)   (CW5-C11).                                                                                                  (CW5-10)

The loss is set at early times (∝ 1/r₀²). In a biased detector the plasma shields the interior until the ambipolar front erodes it (plasma time),
which delays the Ramo current; this is the time-domain mark of G-E5. **Spec.** Drift–diffusion–Poisson with rate equations (Auger, exciton formation
(§2.5), SRH capture) on the track geometry from §2.6/§4.5, 2D axisymmetric, mesh ≤ 1 nm near the core, field ramp 0–250 V/cm; outputs f_A(E_R, ℰ_b),
plasma time and the Ramo delay; CMPMC transport only for modules passed by CMPMC-AUD. Pitfalls: (CW5-10) fails once f_A ≳ 0.1 (nonlinear); C_A at mK
in Si/Ge [UNVERIFIED]. Cost ≲ 10³ CPU-h.

### 4.4 LE-147: carrier-driven defect reactions [D for the athermal law; exact gap]
**Derivation [D given a linearly coupled harmonic reaction mode].** Capture or recombination at a defect releases E_rec into local modes. If the
reaction coordinate R is linearly coupled with Huang–Rhys factor S_HR,R, then at T = 0 the number of quanta deposited in R is Poisson:
|⟨n|D(√S_HR,R)|0⟩|² = e^{−S}Sⁿ/n! (CW5-C12). The athermal reaction probability per event is the Poisson tail

  p_R = Σ_{n ≥ E_bar/ω_R} e^{−S_HR,R}S_HR,Rⁿ/n!   (at mK the Weeks–Kimerling thermal factor is absent),                                                (CW5-11)

and the stimulated rate is Γ_cd(t) = 𝓃_car(t)σ_capu_car p_R. It enters 𝒦^{rel}(…; n_car) as a time-dependent rate, so T-1 still holds (WP7-T-v2
C16b). **Single missing step.** S_HR,R, ω_R and E_bar for the real defects: the §3.2 computation with the charge-state change included (ΔSCF).

### 4.5 LE-148: pocket size distribution (compute-formulate)
**What is computed.** P(N_a | E_R, r̂_R): the number of atoms in amorphous pockets left at t_pr by NR cascades in Si and Ge, and the recrystallisation
energy per pocket. With it, the (b′) visible rate of WP7-E-v3 is ℛ_vis = ∫dE_R(dℛ_NR/dE_R) Σ_{N_a ≥ N_a*}P(N_a|E_R)P_rel(N_a, t_obs), with
N_a* = E_thr^det/(ϵ_coll e_a) and e_a = 0.1–0.2 eV/atom [E], i.e. N_a* ≈ 272–543 at 16.3 eV. **Method.** MLIP-MD (the WP5 §3.4 potential, ZBL-spliced)
cascades at E_R = 0.2–20 keV, ≥ 10³ per energy and material, cells 10⁵–10⁶ atoms, 10–50 ps, boundary thermostat; quench by the WP5-AUD §3.1 protocol;
pockets identified by a local order parameter (e.g. bond-angle or Steinhardt q₃) and connectivity, with the result reported for two thresholds.
The recrystallisation barrier spectrum comes from NEB/accelerated MD on 10² pockets. **Pitfalls.** The cluster definition changes N_a by ~2×, so report
both thresholds; thermal spikes in Ge need the §2.6 TTM coupling; E_st and pocket energies must use the same E^{conf} table (T-1 (ii)).
Cost ≈ 10⁴–10⁵ GPU-h [E].

### 4.6 LE-149: the (H-E6) residual [D: exact criterion and bound]
**Statement.** Let s be the full t_pr microstate and π(s) = (𝐍, 𝔪) its projection. If 𝒫_det(𝐌|𝐍, 𝔪) is defined as E[𝒫_det(𝐌|s) | π(s); Λ], WP7-E-v3
(E3) is exact by the tower property. The residual of a **Λ-independent** detector table, built with a reference seed Λ_ref, is

  |ΔP(𝐌|Λ)| ≤ Σ_{𝐍,𝔪}P_casc(𝐍, 𝔪|Λ)·TV[law(s|𝐍, 𝔪, Λ), law(s|𝐍, 𝔪, Λ_ref)],                                                                     (CW5-12)

where TV is the total-variation distance. (H-E6) is therefore exact iff the marks are a sufficient statistic for Λ. **Single missing step.** The TV for
the omitted features (cloud shape beyond centroid and rms, the branch fine structure of dℋ/dω_ph) between DM and photon seeds. **Spec.** Run the
detector stage on full cascade microstates and on mark-resampled microstates for the two seed classes; the observed difference in N^meas and E_sig is θ_H-E6.

### 4.7 LE-150: the TRIM inference of L36 [FT]
1805.09942 [FT, PDF p. 5]: "TRIM-2013 simulations were used to model the entire defect formation process, for a range of user-defined values of the Ge
displacement threshold energy from 15 to 23 eV"; "TRIM predicts a monotonic, decreasing relationship between the percent energy lost to defects in the
80–110 keV energy range and the Ge displacement threshold energy"; "To match … (6.08 ± 0.18) %, TRIM simulations suggest using a displacement threshold
energy of 19.7^{+0.6}_{−0.5} eV. The systematic error does not include modeling imperfections in Geant4 and TRIM." The paper does not state which TRIM
output it identifies with "energy lost to defects", nor TRIM's lattice and binding-energy settings. The detectors were biased at ±2 V (PDF p. 2), and the
paper attributes the inter-detector tension (2.06σ) possibly to "a difference in charge collection efficiency (electrons vs. electron-holes)" (PDF p. 6).
**Closure.** The status changes from UNRESOLVED to resolved: the inferred E_d is conditional on TRIM's undisclosed energy-to-defect model. In URF terms
the datum constrains only the (E13)-type combination, with collection terms present. The monotonic decrease agrees with NRT at fixed E_st,1 (WP7-E-v3 C8a).

---
## 5. LE-151: colour centres (D2) and molecular bond breaking (D5) [exact gap; measurement proposal]
**Status of values.** No [FT] value of p_q, p_FH(mK), single-F readout efficiency f_opt, p_esc or σ* yields was found. The ER/NR calibration remains the
MeV-dose 2503.20732 response [FT via WP7-B2-v2 §9]. Row closed as an exact gap. **Strongest derived statement.** WP7-B2-v2 (B2.9.1) with (CW5-8) for the
ER branch and the §3.2/§3.3 machinery for p_surv at mK. **Single missing step:** p_q·p_surv·f_opt at sub-keV recoils, and p_FH(T → 0).
**Measurement proposal.** (1) Tagged neutron scattering on LiF at 10 mK (recoil energy from kinematics, as in 2303.02196) followed by single-F confocal
or two-photon readout, counting F centres per tagged recoil: this measures Y_CC(E_R) = P_FP p_surv p_q f_opt directly. (2) 5.9 keV X-rays at mK: F yield
per absorbed energy together with STE luminescence quenching gives p_FH. (3) D5: photodissociation quantum yield of a molecular crystal at mK, with
fragment detection by IR absorption, gives p_esc. **Spec** (computation side): WP7-B2-v2 §9–§10 unchanged, plus §3.2 tunnelling-recombination rates for
close F–H pairs.

---
## 6. Checks (code/CW5/checks.py, 21/21 PASS, 19 s)
| Check | Content |
|---|---|
| C1, C1b | D-1 exact ratio 1.407 (1.400 at ε 3.8) vs first order 0.280; split r_g^{NR}, r_g^{ER} limits (sympy) |
| C2 | WP8-R HV FOM (WP5-AUD code copied): 1.9986/2.0136/1.7626; C7c′ 1.9926/2.0076; 220 eV 2σ 2.015; F_NR* at three ⟨𝔮⟩, two ε |
| C3 | REF-B closed-form proof of E_st/ω ≤ 1 − η^φ_NR (sympy derivatives, linearity, end values; 4000 random interior points) |
| C4 | LE-133: second-difference cancellation (sympy), O(qq′) form, T⁹ power counting |
| C5 | LE-143: non-lattice renewal limit 0.75; lattice remainder; tagged-unit formula vs exact fragmentation count |
| C6, C6b | LE-141: (CW5-4) and its exact asymptotic split; bimolecular r_g |
| C7 | LE-23: signed estimator unbiased, clipping biased |
| C8, C8b | LE-127: orthogonality exponent on a 1D chain; Born limit α_ohm = 4K |
| C9 | LE-129: window numbers, λ_P of the Si close pair |
| C10 | LE-138: d ln ε_eh/d ln λ_ph = 0.12; +2.7% at Z_qp = 0.8 |
| C11, C12, C13, C14 | (CW5-10); Poisson FC law; 1/t, ln sum rule and the Borel s^{−3/2} tail; maximum entropy |
| C15, C16, C17 | tanh factors, P̄ from tanδ₀, σ conversion; memory weight w_mem; B-2 numbers |
| C18 | six fetched arXiv IDs verified (API records) |

## 7. Literature (this return)
[FT], read here: 0802.2404 (Table I p. 2, text p. 3); cond-mat/0507622 (pp. 3, 5, 6, 10); 1805.09942 (pp. 2, 5, 6); 2009.03804 (Eq. (4) p. 4, K values
p. 5); 1705.01108 (pp. 11, 13, 14); cond-mat/0310283 (Eqs. (11)–(12) p. 3, (49) p. 7, (53)–(61) p. 8, ref. [11] p. 14). Bibliography verified via Crossref:
Andreev–Lifshitz, Usp. Fiz. Nauk 102, 323 (1970); Sov. Phys. Usp. 13, 670 (1971). [FT as read in the cited return]: 2208.02790, 2202.05097 (WP7-E-v3 §3.3),
2303.02196 (REF-WP5-AUD-A/B), 2503.20732 (WP7-B2-v2 §9). [UNVERIFIED]: Pooley–Hersh, Nozières–De Dominicis, Weeks–Kimerling, E_x^b(Si), C_A(mK).
No INSPIRE walk was needed (no row asks for a citation search).

---
## Symbols introduced/used
*Used as defined (NOTATION v4, "Rows added WP7", "Rows added WP7-E", WP5-AUD, GAP-EF):* ω, E_g, ε_eh, F_eh, F_NR, N_eh, 𝔶, y_ion, δ_coll, r_coll, g_Luke,
κ_cal, κ_cal(r_coll) (WP5-AUD, proposed), X^{oth}, d′, D′, E_pairs, E_X, E_x^b, E_trap, E_esc, E_st, E_st^{rel}, ⟨N_hop⟩, 𝒦^{rel}, Y_H, t_win, t_obs, t_pr,
ℋ, ℋ_nuc, ℋ_pr, ΔZPE, ϵ_prim, ϵ_NTL, ϵ_coll, 𝔮, P_g (WP5-AUD; redefined by (CW5-2)), E_s, E_s^{(0)} (WP5-AUD B-1; E_s^{(0)} redefined), λ_ph, 𝒜_ph, w₀ (GAP-EF),
Δ_as, Δ_tun, E_TLS, P̄_STM, C_TLS, γ^{def}, 𝐩^{def}, 𝔣^{def}, tanδ₀, J_ph, J_el, J_loc, α_ohm, ω_co, λ_P, d_tun, ω_well, Γ_att, A_T, 𝒬^{sb}, S_HR,k, ε^{hop}_ij,
η_pole, Δ_dfn, ε^{dfn}, θ_p (source), M_cr, μ_FK, V_P, E^{conf}, δρ_κ, Z*_κ, ε_∞, C_X, τ_X, σ_BX, 𝓃_j, σ_cap, u_car, θ_* (WP6 types).
*Introduced here (NOTATION grep: no collisions):*
| Symbol | Meaning | Where |
|---|---|---|
| r_g(t), r_g^{NR}, r_g^{ER} | fraction of created-pair gap energy still in E_pairs + E_X at t; P_g ≡ 1 − r_g | (CW5-2)–(CW5-4) |
| 𝒢_gap ≡ E_g/ε_eh | gap share of the pair energy | (CW5-3) |
| b_trap, γ_k^{gap}, w_k | prompt-trap branch of a pair; decay rates and weights of r_g | (CW5-4) |
| w_mem | k-memory weight Γ_E/(Γ_E + Γ_k) | (CW5-1) |
| δ̃_ν, N_σ(E_F) | eigenphases of S_RS_L†; per-spin DOS at E_F | (CW5-6) |
| S_pol(T), W_eff, W_r | polaron exponent; dressed and electron-renormalised hopping | §3.8 |
| b_br, τ_av, E_cut^{av}, U_rel | trigger branching ratio; avalanche exponent and cutoff; relaxable elastic energy | §3.5, (CW5-9) |
| ε_X, p_R, ω_R, S_HR,R | energy per exciton; athermal reaction probability; reaction-mode frequency and HR factor | (CW5-8), (CW5-11) |
| f_A, λ_L, r₀, D_a | Auger loss fraction; track line density, radius; ambipolar diffusion | (CW5-10) |
| θ_U, θ_τ, θ_H-E6 | nuisances (M on U_rel; Δ on τ_av; detector-stage sufficiency) | §4.2, §4.6 |
| (CW5-1)–(CW5-12), Theorem CW5-G, CW5-C1…C18, OC-1…OC-12, (H-BGK), (H-g1)–(H-g3), (H-d1)–(H-d4), (H-L1)–(H-L3), (H-p1)–(H-p3), (H-ME), (r1′)–(r3′) | labels (prefix CW5) | — |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-CW5-1 | WP5 (next revision) | OC-1 (D-1 exact form, r_g), OC-3, OC-4 (B-1, B-2), OC-9 (signed sampler), OC-10 (L23/renewal) | apply in §1.5, §2, §3.1, §3.3, §3.4, §6.4 |
| IF-CW5-2 | WP6 | θ_coll σ_ln 0.1 (OC-8); θ_X → type T on r_g^{NR}, r_g^{ER} separately; θ_U, θ_τ for the LEE model; θ_{R-k} bounded by (CW5-1) | rows in §5.2 |
| IF-CW5-3 | WP8-R | OC-7 (D-7, C7c′ texts); the (b) channel's timing law is (CW5-4)/(CW5-3) (G-R2) | revise §4.3–§4.4 (CW6 / LE-20) |
| IF-CW5-4 | coordinator: LIMITS | L30, L32, L36, L37, L38, L42 ✎ and the new rows below | merge (CW8 / LE-167, 168) |
| IF-CW5-5 | NOTATION | symbols "introduced here"; P_g redefined; E_s^{(0)} redefined; κ_cal(r_coll) | add rows |
| IF-CW5-6 | WP7-T | (CW5-6) replaces the [UNVERIFIED] Yamada formula; L30 DERIVED; §3.3 conditional verdicts | errata in G-T1, G-T2, §4.2, L30 |
| IF-CW5-7 | WP7-E | Theorem E-2: ionic exception (prompt E_el → E_st via STE, (CW5-8)); G-E2 → (CW5-9); G-E9 → (CW5-12) | erratum |
| IF-CW5-8 | CW8 (LE-162/163) | Andreev–Lifshitz flagged (OC-11); T⁻⁹ credited to Pushkarov refs [16, 17] of cond-mat/0310283 | bibliography |
| IF-CW5-9 | coordinator: SOTA, CORRECTIONS | WP5-AUD REFEREED after OC-1…OC-8; WP5-v4 REFEREED after IF-AUD-1…8 + OC-1…OC-8; SOTA sentence of OC-7 | record |

## Owed corrections (target → exact text)
| ID | Target | Type | Exact text |
|---|---|---|---|
| OC-1 | WP5-AUD §1.2 D-1 bullet, D-1 row, AUD-C3d label, R-e; WP5-v4 A-4/(W11); WP7-E-v3 (E7)–(E8) | S | "D′ ≡ E_st(t_win) + E_pairs(t_win) + E_X(t_win) + E_trap(t_win) + E_es^{trap} + ΔZPE(t_win) + E_esc, used only in the exact ratio Y_H = (1 − δ_coll)(ω − D′_NR)/(ω − D′_ER). At zero field Y_H = (1 − δ_coll)[1 − 𝔶𝒢_gap r_g^{NR}(t_win) − d′^{oth}_NR]/[1 − 𝒢_gap r_g^{ER}(t_win) − d′^{oth}_ER], 𝒢_gap = E_g/ε_eh, r_g ≡ [E_pairs + E_X](t_win)/(N_ehE_g) (trapped and escaped gap energy are already in E_trap, E_esc). Si, 100 eV, r_g = 1: 1.407 (+0.41); the first-order term 0.28 is invalid because 𝒢_gap r_g ≈ 0.31. (W11)'s first-order form requires 𝒢_gap r_g(t_win) ≪ 1. Excitons carry E_g − E_x^b each. r_g^{NR} ≠ r_g^{ER} in general (CW5 (CW5-4), bimolecular tail). 'L36–L38 numbers unaffected' → '[E]: drift ≈ 1 µs at 4 V/cm against ≳ 100 µs windows (Si and Ge data both biased)'." |
| OC-2 | WP5-AUD D-2; WP5-v4 A-12 | N | D-2 reclassified as clarification. Append to A-12: "(E7) counts 𝒲_bias(t_pr) once, inside NTL heat; never weight ℋ_pr (which contains it) by ϵ_prim. Its collection efficiency lies between ϵ_prim and ϵ_NTL [E]; ≤ 0.25 eV per carrier." |
| OC-3 | WP5-AUD B-1 (WP5 §2, §3.4 text) | S | "(i) carrier relaxation from creation down to ω_op; (ii) residual kinetic energy below ω_op; (iii) capture heat; (iv) pre-t_pr NTL heat; (v) lattice heat ℋ_nuc from the §3.4 MD projection (with anharmonic residual and thermostat energy). Σ_{(i)–(v)} = ℋ_pr − ΔZPE; ΔZPE is excluded from the spectrum. E_s^{(0)} = ω_s/2 per end-state mode (not the projection of R_I(0)). The ≤ 10% anharmonic acceptance is [E]." |
| OC-4 | WP5-AUD B-2 | W | "N_eh ≤ ⟨N_eh⟩ + 6σ (≥ 100 at 1 keV); trajectories per point ≥ 1100 for 6% on the variance at κ_ex = 2 (error √(2/(n − 1) + κ_ex/n)); 2303.02196's sub-keV E_r is set by neutron kinematics; its Eq. (1) books the non-NTL phonon energy as E_r (unit heat quenching), which is the L37 truncation; ⟨𝔮⟩ = 0.873 is a worst case from detector-model trapping probabilities [E]." |
| OC-5 | LIMITS L38 (Validity, Status) | W | Validity: "… hypotheses (B-a), (B-b) r_coll ≥ 1, (B-d), X^{oth}_NR ≥ κ_cal(r_coll)X^{oth}_ER (implied by κ_cal(1) for r_coll ≥ 1 only)"; Status: "DERIVED (AUD-1: AUD-C1, REF-A/B; bound: REF-B §2 proof, CW5-C3), REFEREED". Chain: move "g_Luke = 4/3.82 [FT]" out of the remainder clause. |
| OC-6 | WP5-AUD D-12, D-13, §7, C3c/C3e | N | "N_a ≳ 272–543"; "p_surv ≲ 0.47 (unrounded 0.4748)"; tags g_Luke [FT], y_ion [E], κ_cal, r_coll [D on E]; "[FT via X]" → "[FT] (source, as read by X)"; 300 eV bracket [E]; C3c, C3e "consistency identities". |
| OC-7 | WP5-AUD R-f, D-7, §0 row 5, IF-AUD-6, AUD-C7c/C7c′; WP8-R §0 row 6, §4.4, C7l, IF-R4; LIMITS L42; SOTA | S (claim) | "HV (≥ 100 V) NO-GO at E_R ≤ 300 eV holds at the central measured Y(E_R), F_NR (2303.02196; 1σ bands) and is firm at E_R ≲ 220 eV. At the 1σ corner (Y 0.098, F_NR 0.4, ⟨𝔮⟩ 0.873 [E], F_ER 0.119) the ceiling is 2.014 with the source's ε = 3.8 eV (1.999 with 3.75; 1.763 at ⟨𝔮⟩ = 1); at the joint 2σ corner it exceeds 2 from 220 eV (2.015). The threshold F_NR* = 0.28/0.41/0.51 at ⟨𝔮⟩ = 1/0.873/0.8 (ε 3.8). The verdict is CONDITIONAL on (Y, F_NR, ⟨𝔮⟩, C.L.). WP8-R C7l (F_NR = 0.15) is marginal: 1.99–2.01 with energy-matched Y(300 eV) = 0.12, up to 2.40 at F_ER 0.119, ⟨𝔮⟩ 0.873." |
| OC-8 | WP5-AUD §3.2(b), D-4, WP6 θ_coll row | S | "r_coll: median 1, σ_ln 0.1 [E] (WP8-R's \|r_coll − 1\| ≲ 0.2 read as 2σ), sign open in the profiled object (i); the conditional bound (ii) E_st/ω ≤ 1 − η is reported on the r_coll ≥ 1 branch only. The C8b illustration assumes r_coll ≥ 1, a flat E_st/ω prior on [0, 0.1] and δ_coll = X^{oth} = 0." |
| OC-9 | WP5-v4 §1.5 (sampler), §3.1 | S | "Defect seeds exported at phonon poles (WP7-T-v2 (1.3), IF-T9) carry the signed weight (π\|B\|²/η_pole)δ − 2πIm(a*B)δ. Sample classes with \|K_i\|/Σ\|K\| and score sign(K_i)Σ\|K\|; never clip; report the variance factor (Σ\|K\|/ΣK)²; only the class sum P(N_eh\|Λ) must be non-negative per q bin." |
| OC-10 | WP5-v4 §6.4 "Asymptotics"; LIMITS L23 | W | "n̄(ω) = ω/ε_eh + o(ω) is DERIVED (CW5 §2.7: tagged-unit formula (CW5-5) + renewal in ln x under (r1′)–(r3′)); the constant b_N and Var N_eh = F_ehω/ε_eh + O(1) remain [D, sketch] (second-order renewal)." |
| OC-11 | WP7-T-v2 G-T5; LIMITS L30 source cell | W | "Andreev–Lifshitz, Zh. Eksp. Teor. Fiz. 56, 2057 (1969) [UNVERIFIED, original not read; via cond-mat/0310283 ref. [11]]; review: Usp. Fiz. Nauk 102, 323 (1970) = Sov. Phys. Usp. 13, 670 (1971) (Crossref). T⁻⁹: cond-mat/0310283 Eqs. (12), (49)–(61) [FT], credited there to Pushkarov (its refs [16, 17])." |
| OC-12 | LIMITS L32 (last cell); WP8-F (4.2) "tanδ₀ of a-SiO₂ not quoted" | W | "tanδ₀ (low power, mK, ~6 GHz): thermal SiO₂ 3.0–3.3×10⁻⁴, PECVD SiO₂ 2.7–2.9×10⁻³ (0802.2404 Table I [FT]); CVD a-SiO₂ ≈ 5×10⁻³ at 25 mK (cond-mat/0507622 [FT]); preparation (OH) dependent; divide by tanh(hν/2k_BT) = 0.894 if taken at 100 mK; bulk fused-silica mK value GAP." |

## Proposed LIMITS rows
| # | Change / chain | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L30 ✎ | Status "(T⁻⁹) [D, sketch]" → DERIVED: one-phonon forbidden (v_max ≪ c), two-phonon amplitude ∝ ω in both coupling channels, transport factor (qa)² | cond-mat/0310283 Eqs. (12), (49), (54), (61) [FT] | Δ_dfn ≪ T ≪ θ_p, dilute | effective-mass regime T < Δ_dfn; defecton–defecton D ∝ 1/(xσ); localisation Eqs. (17)–(18) | DERIVED (CW5-C4) |
| L32 ✎ | tanδ₀ values (OC-12) | 0802.2404, cond-mat/0507622 [FT] | low power, T ≪ hν/k_B | OH content; bulk vs film | ✎ |
| L36 ✎ | "TRIM inference UNRESOLVED" → "E_d = 19.7 eV is conditional on TRIM-2013's undisclosed energy-to-defect model; error excludes TRIM modelling (1805.09942 p. 5 [FT])" | 1805.09942 [FT] | — | MD ⟨E_st⟩ | resolved (model-conditional) |
| L37 ✎ | Validity: "r_g^{NR,ER}(t_win)𝒢_gap ≪ 1 (else the exact-ratio D-1 form (CW5-3))" | — | — | (CW5-4) | DERIVED |
| L38 ✎ | OC-5 | 1803.02903 [FT] | (B-a), (B-b), (B-d) | O(d′², δ_colld′) | DERIVED, REFEREED |
| L42 ✎ (WP8-R) | OC-7 text | 2303.02196 [FT, via REF-WP5-AUD-A/B] | 1σ bands | ⟨𝔮⟩ [E] | CONDITIONAL |
| new (α_ohm) | (CW5-6) → Born limit α_ohm = 4K, K = (N_σVΩ)², Black rate | 2009.03804 Eq. (4) [FT] | weak coupling; per-spin DOS | eigenphase form beyond Born; displaced scatterer | DERIVED (Born, CW5-C8b); [D, sketch] (6) |
| new (renewal) | (W3) → tagged-unit (CW5-5) → m(E) = E/ε_eh + o(E) | key renewal theorem (textbook) | (r1′)–(r3′) | b_N, variance: [D, sketch] | DERIVED (CW5-C5) |
| new (gap release) | WP7-E-v3 (E1) + linear pair kinetics → r_g(t) = Σw_ke^{−γ_kt} (CW5-4); bimolecular → 1/(1 + t/t₀) | — | (H-g1)–(H-g3) | droplets; rates at mK | DERIVED (CW5-C6) |
