# R16 referee report VER-CW3 (hostile, isolated) on returns/R16/CW3.md

Referee VER-CW3, brief briefs/R16/VER-CW3.md. Read: the return, code/CW3/ (checks.py, fork/), the files it cites in returns/R8, R12, R13 and state/LOOSE-ENDS.md, plus
CONVENTIONS, NOTATION. Not read: referees/R16/*, other returns/R16, briefs/, log/LAUNCHES. Rerun: `python3 -I code/CW3/checks.py` gives **28/28 PASS in 10.5 s**,
the same as claimed. Independent checks are in the scratchpad only (pt.py, alp.py). Full text fetched with lit.py into literature/papers-r16-VER-CW3/:
2109.08168v2, 2011.01940, 2501.05504, 1306.6089, 2101.01241, 2305.05681, 1809.02863, 1905.13650, 1108.5383, 1206.2644, math-ph/0201055, 1101.2210.
PDFs deleted afterwards; html and txt kept.

## 0. Verdict table (scope 1–3)
| # | Item | Verdict | Reason (details in §1–§4) |
|---|---|---|---|
| V1 | LE-77 (CW3.1): Fano prefactor 1; c^F normalised with Γ^tot; K_x shift; owed corrections 1–4 | **STANDS WITH CORRECTION** | I re-derived it by hand and the kernel and the (W15) bound hold. One slip: "Im Υ = −½ΣΓa" must read Υ = −(i/2)Σ_fΓ^{(f)}a^{off}_f. Γ/δ ≲ 1.7 lies outside the O(Γ/δ) expansion |
| V2 | LE-75: 𝔉 = 0 for PT, N_e even, with/without SOC; [C]/[D, sketch] → [D]; corrections 5, 6, L-Fano | **STANDS WITH CORRECTION** | The proof needs Ẽ ∝ 𝟙 on D(Λ₀) (or [Ẽ, Γ̂] = 0 and the branch kernels in the same eigenbasis). Counterexample: with a real non-scalar level-shift matrix, the per-branch odd weight is ±0.06 while the branch sum is ≈ 0 (§1.2) |
| V3 | LE-76: Γ/δ map spec; "K_ν ≥ 0 for GaAs outside the d11 shell" [E] | **STANDS WITH CORRECTION** | δ₀ = 0.3 eV is used everywhere, but the return defines δ_Λ₀ as including the distance to the intervalley threshold. Γ–L lies at ≈ 0.3 eV, so δ → 0 exactly where Γ is 20–60 meV. A second excluded shell (valley thresholds) is missing |
| V4 | LE-79: 𝔳²_s row (CW3.2), 𝒪₂ mapping, = −2×𝒯_e; correction 9 | **STANDS** | Matrix element, anticommutator form and 𝒯_e normalisation re-derived (ψ†∇↔²ψ → −(k+k′)²). 17th row consistent with WP0 (𝒯_e was an extra row, not one of the 16) |
| V5 | LE-78: (CW3.3) exact orbit–orbit f-sum term, complete O(α²) list | **STANDS** | Prefactor re-derived with WP0's 𝓜¹ = q²𝓃/m normalisation; the q r ≪ 1 limit reproduces −(4/3)E′/(N m). Breit–Pauli list complete under (L); ordering-independent. Wording: "27%" is relative to δ_mv (21% of the total) |
| V6 | LE-83: (CW3.4), 𝒢_GS → Ω²_{P,e}/(c_Lq)²; "≫ 1 for q ≲ q_BZ [D]"; Si counterexample; correction 10, L17′ | **STANDS WITH CORRECTION** | Limit (a) re-derived. Numbers checked: 0.513 eV, 333, 18.3 keV. But [D] holds only for q ≪ q_BZ. The return itself says that at q = 1 keV (< q_BZ) the derivation's assumptions fail ([E]). Read "[D] q → 0; [E] up to q_BZ" |
| V7 | LE-74: PST energy cutoff gives the low-lying order [D given PST]; acoustic branch not an obstruction; correction 7 | **STANDS** | math-ph/0201055 §4.5 quote verified (journal pp. 175–176). Gap conditions concern σ_r only. Needs smeared nuclei (V ∈ S⁰), as stated |
| V8 | LE-80: Theorem D-m (i)–(iii) [D at stated levels]; correction 8 | **STANDS WITH CORRECTION** | (ii) Williamson/Bogoliubov needs a positive-definite quadratic form. Add: Goldstone and Q = 0 acoustic zero modes gapped by the (M2) field, or excluded at finite N. (iii) inherits the V9 defect for 𝔥_off |
| V9 | LE-82 (G5′): "𝔥_off CLOSED [D, upper bound]", 𝔥_off² ≤ max⟨nk\|H_off²\|nk⟩ = FM zeroth moment | **FALLS** | (a) With U_qp = 1, H_off\|nk⟩ contains the disconnected term c†_{nk}H_off\|FS⟩. Its norm² is ∝ N (pair + phonon creation from the sea), so 𝔥_off is extensive and [8.1′] is vacuous. (b) Even the connected part is bounded by λ_max of the band matrix, not by its largest diagonal entry |
| V10 | LE-82 (3): Dirac running α̃(ω), "QED-like" coefficient 2N_D/3π | **STANDS WITH CORRECTION** | 1101.2210 Eq. (4) [FT] gives dα/dl = −4α²/3π, for one flavour only. The general form 2(N_D+1)/3π is my inference (charge part ∝ N_D, velocity part independent of N_D), not a quote. At the benchmark α̃ = 0.25 and α̃² = 0.06, not 0.39 / 0.15. The conclusion gets stronger |
| V11 | LE-85: 2305.05681 Eqs. (5)–(7) CONFIRMED; tensor wording; skin-depth condition; correction 11 | **STANDS** | Eqs. (2)–(7), Π^{ij} = −ω²(1−ε^{ij}), Π^λ = −eΠe, Π_aA = ig m_a B₀ and the skin-depth footnote all verified [FT] |
| V12 | LE-87: massive ν̃, ω^F and 𝔇^F; [D, sketch] → [D]; correction 20 | **STANDS** | Kinematics re-derived by hand (as C7). The factor m_χ/m_ν̃ requires 𝔇^{NR} to be normalised with 1/(4m_χ²); say so |
| V13 | LE-88 (b), (d) [D] | **STANDS WITH CORRECTION** | (b) fine. In (d), "connected terms O(1/N_eff)" is an estimate, not a derivation: tag [E] (or [D, sketch]) |
| V14 | LE-89: 1306.6089 amplitude CONFIRMED "with the per-level-shift convention"; u derived; corrections 12, 13 | **STANDS WITH CORRECTION** | Rabi Ω = dE checked, and 2101.01241 (S22)–(S25), (S41), (S45) quotes verified. But 1306.6089 states in its own words that d_nε_SE* is "the energy shift produced between spin-up and spin-down states", i.e. the splitting. Eq. (1) is right only if d_nε_SE* = d·E (per-level shift), so the source's sentence is misstated by ×2. The return infers the per-level convention by analogy with the Larmor term (which is per-level). The source's explicit sentence contradicts that analogy, so the convention is not "1306.6089's own" |
| V15 | LE-90: 2501.05504 prefactor 32, M_n; "Eq. (7)'s m_V² is m_Vω_n"; correction 15 | **STANDS WITH CORRECTION** | The 32 and odd-n-only hold. M_n = ρπr_n²L₀ is printed in the source, so it is a consistency check, not a derivation. Typo: \|⟨n\|δH₀\|0⟩\|² = **8**κ²ρ_V e²cos²θM_n/(ε₀²ρ²L₀²ω_n), not 4. Off resonance the numerator depends on the smearing prescription. The source's m_V² is the driven damped-oscillator form, so it is not an error. Delete "is m_Vω_n" |
| V16 | LE-91: drive ∝ ω² [D]; 2δ_rel^a(Cu) = −1.97×10⁻² [FT]; correction 16 | **STANDS** | Body-force argument re-derived. Mode orthogonality to translations makes the origin of ξ irrelevant. All five quoted values match 1809.02863 Table II, which is in units of a_B |
| V17 | LE-93: R_{k′l′} CONFIRMED via 1108.5383 Eq. (6); Eq. (9) algebra CONFIRMED / exact gap; correction 17 | **STANDS** | Quotes verified: 1108.5383 Eq. (6) normalisation, 1206.2644 Eq. (3) [2] = 1108.5383, 2011.01940 Eqs. (7)–(9). "CONFIRMED" is by citation-chain inference, as the return says. Priority [E] not checked (INSPIRE walk) |
| V18 | LE-94: dark photon Eq. (2) exact at all x → DERIVED; x³ split 1/8 + 1/2; correction 18, L-D10′ | **STANDS** | Independent Dirac-trace code (polarisation sums −g, −g + kk/m²) gives the ratio to Eq. (2) = 1 to 10⁻¹⁰ at x = 10⁻³…3. sympy series confirmed |
| V19 | LE-94: **2109.08168 Eq. (3) REFUTED** by (m_a+2m_e)/(m_a+m_e); seagull H_sg; L-D13 | **STANDS** | Independent trace code: σv = e²g²m_a²(m_a+2m_e)/[16πm_e²(m_a+m_e)³] to 10⁻¹². Source |M|² (HTML Eq. (16) = PDF Eq. (15)) integrated with the normalisation that is right for the dark photon gives this, not Eq. (3). NR seagull rate re-derived. **REFUTED confirmed.** Labels are HTML-v2 numbering: PDF Eq. (17) = HTML (18) |
| V20 | LE-95: Bethe ln Ī [D]; PDG [FT]; correction 19, L-D11′ | **STANDS WITH CORRECTION** | Derivation fine. "NR bracket ln(2mv²/I) − v²" is inconsistent: ln γ² = +v² + … cancels −β², so the bracket is ln(2mv²/I) + O(v⁴). C6c is a hard-coded `True`, not a check. PDG wording not verified by me |
| V21 | LE-96: 1905.13650 CONFIRMED; L-D3 text; correction 14 | **STANDS** | 3–10, 3.0, ≈10 (uniform prior), 2.7, 8.4 and 4.4 (Supp. Eq. (32), "initial results") all verified [FT] |
| V22 | LE-84: CC-1 accepted at stated level | **STANDS** | No upgrade claimed |

## 1. Scope 1 details (owed corrections and upgrades)

**1.1 LE-77 (V1).** Let G = (ω+iΓ/2)^{-1}, with exact window integrals ∫|G|² → 2π/Γ and ∫G → −iπ. Then W_b = Γ_b(2π/Γ)[|ρ|² + Σ_b′Γ_b′c_b′] − 2πΓ_bc_b
with c = Im(ρ*a^{off}), and ΣW = 2π|ρ|². That gives K_b = (Γ_b/Γ)(1 + c̄^F − c_b^F) with c^F = Γ^{tot}c/|ρ|², exactly (CW3.1). Σ_ν𝔉_ν = −Γ^xc̄^F holds.
Bound: |ΔP| ≤ ½Σ_b(Γ_b/Γ)|c̄^F − c_b^F|·spread. Use |c̄^F| ≤ (Γ^{ph}/Γ)max|c| and the b = x term. This gives exactly (Γ^{ph}/Γ^{tot})max|c^F|·spread, so correction 2 is
correct. The [E] statement "K_ν ≥ 0 for Γ/δ ≲ 1.7" applies a first-order estimate (|c^F| ≲ 0.3Γ/δ, residual O(Γ²)) at Γ/δ ~ 1. That is the same caveat
WP5-v4 had. Add "(perturbative; reliable for Γ/δ ≪ 1)".

**1.2 LE-75 (V2), the gap.** The proof's step "∫G†AG dω is real symmetric" uses G = (ω − Ẽ + iΓ̂/2)^{-1} with scalar Ẽ. At O(g²) the level-shift matrix Re Σ on a
degenerate D(Λ₀) has the same order as Γ̂. In a Θ-real basis it is real symmetric but in general not ∝ 𝟙. Then H_eff = Ẽ − iΓ̂/2 is complex-symmetric and non-normal.
∫G†B_bG is then complex for a single-branch kernel B_b; only B = Γ̂ gives a real result, by the resolvent identity. Test (scratchpad pt.py): same code as C2, with all
data real (the Θ-real basis), Ẽ = s·diag(1, −1, 0.5, −0.3). Per-branch odd (Fano) weight: s = 0 gives 1.6×10⁻¹² (the theorem); s = 0.05 gives ±0.063; s = 0.2 gives ±0.15.
The branch sum is ≈ 0, which is trivial. C2a tests only Ẽ = 0, so it cannot see this. Two cases are safe. For Ge with one-body self-energies on a Kramers product,
Ẽ and Γ̂ are scalar: a T-even Hermitian operator on a Kramers doublet is ∝ 𝟙. For a D that is a unitary irrep, Schur's lemma applies. The e–h phonon-exchange
(vertex) term, or near-degenerate seeds, break this. Correction to §2.2, owed corrections 5, 6, NOTATION row 4 and L-Fano: add
"(P5) the O(g²) level-shift matrix on D(Λ₀) is scalar (e.g. a product of Kramers doublets with one-body self-energies, or a unitary irrep);
otherwise only Σ_b𝔉_b = 0 is derived". Tag [D] under (P1)–(P5).

**1.3 LE-76 (V3).** δ_Λ₀ = min{edge distance, intervalley-threshold distance, JDOS scale}, the return's own definition. For GaAs the L threshold is ≈ 0.3 eV above the CBM. Seeds with
ε_ck within ~Γ_{Γ–L} of it have Γ/δ ≳ 1. Replace "K_ν ≥ 0 holds for GaAs outside the d11 shell" by "outside the d11 shell and outside the intervalley-threshold shells
|ε_ck − E_{L,X}| ≲ 2Γ [E]". Spec pitfall to add: `fermi_energy = 6.0` and `dis_froz_max = 9.5` in fork/GaAs-LE76/epw.in are absolute eV values. They must be reset
from the FR-PBE scf output (mid-gap, CBM + margin), or elecselfen and the frozen window are wrong. Otherwise the inputs agree with the text: celldm 10.6829 = 5.653 Å, 48 bands,
16 spinor WFs, exclude 1–10 = Ga 3d.

**1.4 LE-79, LE-78 (V4, V5).** (CW3.2): (k+k′)²/4 = k·k′ + q²/4 for k′ = k+q ✓. Orbit–orbit: [n†,[p_i·T_ij·p_j, n]] = 2q·T_ij·q cos(q·r_ij). The [p, T] reorderings are
linear in p and drop out. With 𝓜¹ ≡ ⟨[n†,[H,n]]⟩/V (WP0 (4.6): kinetic → q²𝓃/m) and FT[(𝟙+r̂r̂)/r] = 8π(𝟙−k̂k̂)/k², I get exactly (CW3.3).
The q r ≪ 1 limit gives −(4/3)q²E′/(N m) ✓. The HF 𝒮_st formula is correct.

**1.5 LE-83 (V6).** For q → 0 on the LA branch, Σ_κZ^{(e)}_κ = N_e/cell and e_κ = √(M_κ/M_cell)ê. These give 𝒢 = e²𝓃_e²/(ρ_Tc_L²q²) ✓. A neutral-fluid
compressibility argument gives the same thing independently. Outside q → 0 the formula is not derived, by the return's own §3.3. Corrections:
owed correction 10 and IF-CW3-4: "≫ 1 for q ≪ q_BZ [D]; [E] ≳ 10² at q = 1 keV; [E] ≳ 1 beyond". L17′: "false for every solid as q → 0 [D]".
"Si counterexample derived" stands for q → 0.

**1.6 LE-82 (V9, V10).** (G5′) as stated in WP4 is a sup over ψ_b-evolved states. With U_qp = 1 and the bare Fermi sea, H_off (number-changing H_ep, H_ee) acting on
|nk⟩ = c†_{nk}|FS⟩ has a component c†_{nk}H_off|FS⟩. Example: g_{cv}b†c†_cc_v creates a pair and a phonon from the filled band. Its norm² is ∝ N.
So "max⟨nk|H_off²|nk⟩ = FM zeroth moment + Σ^{(2)}_ee" is false: the right-hand side is the linked part only. If the interacting |i⟩ is used instead, ψ_b
is not in a one-QP bare sector. Separately, H_d in the one-QP sector contains the number-conserving one-body e–e correction (Σ_HF − v_xc), which mixes bands.
The sup is then λ_max of the band matrix M(k), which is ≥ the maximum diagonal entry. Status: "(G5′) 𝔥_off CLOSED [D, upper bound]" → **not closed**. The FM
zeroth moment is a defensible [E] for the linked part. A rigorous intensive bound needs a dressed vacuum, i.e. U_qp ≠ 1, which is exactly gap (1), or a
linked-cluster restatement of (G5′) and [8.1′]. The Al size ≈ 0.2 eV stays [E]. IF-CW3-7 needs this correction. Dirac running: replace by
α̃(ω) = α̃₀/[1 + (2(N_D+1)α̃₀/3π)ln(Λ_D/ω)] (1101.2210 Eq. (4), N_D = 1: 4/3π [FT]). The benchmark becomes α̃ ≈ 0.25, α̃² ≈ 0.06. Delete "QED-like".

**1.7 Other upgrades.** LE-74 (V7): stands; the [UNVERIFIED] Bachmann–De Roeck–Fraas citation is correctly flagged. LE-80 (V8): see table. LE-87, LE-91: stand.
LE-88 (d): tag. LE-89 u: (S22)–(S24) verified; C10b reproduces 3.84×10⁻⁴ from the source's T₂ = 16.7 ms and Γ/2π = 78 kHz.

## 2. Scope 2: claims that a published paper is wrong or misprinted
| Claim | Rating | Basis |
|---|---|---|
| 2109.08168 Eq. (3) (= HTML Eq. (18), PDF Eq. (17)) too large by (m_a+2m_e)/(m_a+m_e); its small-m_a limit 4m_a²/m_e² should be 2m_a²/m_e² | **CONFIRMED** | Independent trace computation; the source's own |M|² (HTML (16)) is ¼ of exact, the same offset as its dark-photon (9), whose rate (12) is right. Eq. (18)'s limits follow from (17)/(3), so they inherit the error. Side note (not claimed by CW3): PDF Eq. (16), the dR/dcosθ, has 4m_e²(ω−ω′)² where its |M|² has 4m_e²ω², a second internal inconsistency |
| 2011.01940 Eq. (9) not current-conserving at bound kinematics (paper-error verdict = exact gap) | **CONFIRMED (algebra) / UNRESOLVED (error)** | Eq. (9) form verified [FT]. The return correctly does not call the paper wrong |
| 1306.6089 Eq. (1) amplitude | **CONFIRMED** (amplitude, with d_nε_SE* = d·E); **source wording "energy shift between spin-up and spin-down" REFUTED by ×2** | §1 V14 |
| 2501.05504 Eq. (7) m_V² vs m_Vω_n | **Source correct; CW3 wording to fix** | CW3 does not call Eq. (7) an error, but owed correction 15's "is m_Vω_n" would imply one. The form is prescription-dependent off resonance, and Eq. (8) agrees on resonance |
| 2101.01241 / CASPEr Ω_a = ½·2Δε/ħ | **CONFIRMED** | (S41) quote and the RWA reasoning verified |

## 3. Scope 3: new derived results
(CW3.1) holds; (CW3.2) holds; (CW3.3) holds; (CW3.4) holds for q → 0 only, see V6; (CW3.5) holds. Theorem D-m holds with the V8 hypothesis added. The 𝔥_off formula falls (V9).
The ω^F identity holds. The Rabi/u resolution holds. The 2501.05504 derivation holds, with the typo fixed. The drive ∝ ω² holds. The Bethe ln Ī holds, with the V20 wording fixed. The running α̃ is corrected (V10).
In C1–C11, C6c is vacuous (hard-coded) and C11 is arithmetic only. All other checks test what they claim. C2 cannot detect the V2 gap.

## 4. Scope 4: CLOSED-AS-EXACT-GAP rows
| Row | Single step right? | Spec sufficient (what / level / method + convergence / pitfalls)? |
|---|---|---|
| LE-73 fibred LAP | **Doubtful as "single".** The Mourre estimate must hold away from thresholds. In the thermodynamic limit the X+ multi-phonon and pair thresholds (critical points of E_Λ + Σω) may be dense in the window complement, and then the hypothesis is empty. State: "LAP away from a discrete threshold set, or a threshold-uniform LAP (open)" | Maths step; no compute spec needed: OK |
| LE-74 quasi-local superadiabatic generator | Plausible | Maths: OK |
| LE-81 CDW GRPA | Plausible | What/level/method/convergence (Goldstone, f-sum 10⁻³) given. **Pitfall missing:** the phonon-mediated term appears both in Γ_{HF+ph} and in D^{-1} = D₀^{-1} − |g|²Π. Avoid double counting by keeping one of them. TiSe₂'s CDW is commensurate, so the phason is gapped; that is acknowledged via the artificial-Q test |
| LE-82 U_qp, bin (c), Dirac | (c) "same fibred LAP": the operator is H_d, not H_K, so "same" should read "analogous". After V9, (G5′) joins the open list | Dirac: refers to WP4 §5.4 with the running check (correct the coefficient, V10) |
| LE-86 CC χ n → p e⁻ | Plausible (distorted-wave golden rule) | **Insufficient.** No convergence criterion (shell-model valence space, number of final states, lepton partial waves). **Pitfalls missing:** g_A quenching for GT (≈ 0.7–0.8), first-forbidden terms when k_eR_N is not ≪ 1 at Q ~ MeV, and Fermi-function sign/Z+1 conventions |
| LE-88 (c) quadratic response | Plausible | **Insufficient.** Method only (2n+1 DFPT + HEG check). Missing: the dynamic (ω₁, ω₂) level, convergence targets, pitfalls (local-field/xc kernel in R^{(2)}, sum-frequency poles) |
| LE-92 near-T_CM LLG | Plausible | Complete (what, level, method, convergence L ≥ 4ξ, 10³ trajectories, pitfalls) |
| LE-93 Eq. (9) quantitative | Plausible | **Thin.** "DHF evaluation of (F.4) with S_{J_TJ_T}": add the partial-wave cutoff, the convergence of the continuum normalisation, and the pitfall that J_T needs the same gauge as n (continuity) |
| LE-76, LE-78, LE-83 (compute-formulate) | n/a | Complete apart from the V3 pitfall (absolute energies in epw.in) |

## 5. Scope 5: proposed LIMITS rows
| Row | Verdict |
|---|---|
| L-D10′ | Correct (Eq. (2) and App. (7)–(12) checked [FT]; my derivation agrees) |
| L-D13 | Correct; add the version note "HTML v2 Eq. (18) = PDF Eq. (17)". Leading correction: none at tree level; in-medium effects negligible at m_a ≳ 100 keV per the source |
| L-D11′ | Derivation correct; fix the "− v²" (V20). PDG wording not verified by this referee (not on arXiv): keep [FT] as CW3's claim |
| L17′ | Change validity to "q → 0 [D]; up to q_BZ [E]" (V6). 2110.01587 §VII not checked here |
| L-O2 | Correct |
| L-Fano | Add (P5) (V2) and "perturbative in Γ/δ" (V1) |
| L9b′ | Correct (2305.05681 Eqs. (2)–(7) verified, including the skin-depth footnote) |

## 6. Required changes (summary for the coordinator)
1. V9: withdraw "(G5′) 𝔥_off CLOSED [D, upper bound]". Restate the formula as the linked part [E] and add (G5′) to the LE-82 exact gaps. Fix IF-CW3-7.
2. V2: add hypothesis (P5) to §2.2, owed corrections 5, 6, NOTATION row 4 and L-Fano.
3. V10: Dirac coefficient 2(N_D+1)/3π; benchmark α̃ ≈ 0.25.
4. V6: [D] only as q → 0 in §3.3, owed correction 10, IF-CW3-4 and L17′.
5. V3: add the valley-threshold exclusion to the GaAs K_ν ≥ 0 claim; add the absolute-energy pitfall for epw.in.
6. V14, V15: reword owed corrections 12, 13, 15 and the SOTA line (source misstatement; m_V² is not an error); fix the 4 → 8 typo in §4.5.
7. LIMITS targets checked: L17, L-D1, L-D3, L-D4 ("prefactor open"), L-D5 ("0.01–0.02 [E, UNVERIFIED]"), L-D8, L-D10 ("Eq. (3) open", "observed"), L-D11 ("[D, sketch] (Bethe log)") and L9b exist, and the text CW3 replaces matches. LIMITS.md contains a second row labelled L17 (line 172, OPEN ELF list), so name the target row unambiguously.
8. Minor: Υ formula (V1); "− v²" (V20); LE-88 (d) tag; LE-86, LE-88 (c), LE-93 specs (§4); LE-73 threshold caveat.
