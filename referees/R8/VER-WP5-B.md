# R8 verification VER-WP5-B: returns/R8/WP5-v3.md against REF-WP5-B (R7)

**Read:**
- the R8 closing table (§R8.1–R8.3);
- the changed sections: §1.1–§1.5, §2, §3.1, §3.3, §5, §6.1–§6.4 and §8;
- code/WP5-v3/checks.py, which I re-ran: 55/55 PASS in under 1 min.

**Isolation:** as in R7. No other referee report or return was read. No literature was re-fetched, because R7 already verified the
quotes against the full texts.

## 1. Item-by-item verdicts (REF-WP5-B V1–V20 and its "required corrections")
| R7 item | Verdict | Evidence in v3 |
|---|---|---|
| V1 (W1) vs 2\|ImΣ\|; LFE index; anti-Hermitian part; differential rate | RESOLVED | (W1) is now Γ^out with (1 − f)(1 + n_B). (W16): 2\|ImΣ\| = Γ^out + Γ^in. The identity (1 − f)(1 + n_B) + f·n_B = 1 − f + n_B checks. (W1′) uses W_GG′ = ε⁻¹_GG′ v_C(p+G′). ρ†[(W − W†)/2i]ρ = Im(ρ†Wρ) is correct, and the sign matches 2v_C\|ρ\|²Im(−ε⁻¹). The first line is now the differential rate |
| V2 ε_ion ↔ g^L identity | RESOLVED | WP5-cp1–cp3 (Z*, ε_∞, ω_LO; multipoles; Ewald cutoff) are added and propagated to §1.5 (O4-d2) and to the §2 e–ph spec |
| V3 plasmon single channel; Al | RESOLVED | §1.1(a) is restricted to ε₂(ω_pl) > 0. Al gets type 𝔱 = pl with a decay kernel (§5). The bookkeeping argument (longitudinal, non-radiating, so ω_p goes to electrons) is fine. Nit: "carries the whole f-sum" (C27) is exact only as q → 0. At finite q < q_c the Lindhard continuum below qv_F shares the f-sum, but there is still no e–h weight at ω = ω_p |
| V4 Born parameter | RESOLVED | Z_κα/v_F = 14.6 (Si), 34.8 (Ge) (C6b, reproduced). 3.7×10² is withdrawn everywhere I checked (§1.1(e), §3.3, §6.1) |
| V5 (W3), moments | RESOLVED (stood) | (H-t), (H-m) were added at REF-A's request. The toy-root statement (C23) is correct. Lindhard is now correctly "first moment after BCA + Markov truncation 0" |
| V6 (B2) density and criterion | RESOLVED | Densities are now 7×10¹⁹ / 3×10²⁰ cm⁻³. The condition is split into Pauli (B2a, occupation ≲ 3%) and Coulomb (B2b, n a_X³ ≈ 5–19 at 1 keV, ≈ 0.46 for 30 pairs). The scope is [E] for small seeds and [C] at keV, with θ_dense. Arithmetic checked (a_X = 4 nm) |
| V7 (W4), (W14) exact | RESOLVED (stood) | Unchanged. The exciton variant (C30) is trivially correct |
| V8 (ii) vs (iii) inconsistency | RESOLVED, with a minor NEW ERROR (N1) | (iii) is now tagged [E, inconsistent model] and given no evidential weight; the consistent decomposition is stated |
| V9 thresholds; "vanishes" | RESOLVED | 352/395 eV (336/382 eV keeping v_N²) reproduce my R7 numbers. The soft threshold is argued correctly: at v_th, k ≳ E_g/v_N = 2k_F, the Bethe-ridge tail. The §6.1(a) switch-off became "strong suppression". The Ge 254 eV statement is updated |
| V10 (W15) estimate; Si map; negative K_ν | RESOLVED, with a NEW ERROR (N2) | The bound is kept. The [E] worst case is 0.3Γ/δ (spread ≤ 1) and 0.11Γ/δ is optimistic. The GaAs Γ/δ is stated as unknown. On K_ν: \|𝔉_ν\| ≤ 4πΓ^(ν)max\|c\| gives K_ν ≥ 0 when 4π max\|c\| ≤ 1 (correct). The signed sampler, ν ~ \|K\|/Σ\|K\| with weight sign(K)Σ\|K\|, is unbiased. (W17) normalisation and the Kramers trace (C14f) are fine |
| V11 Migdal subtraction | RESOLVED | The prescription is now (1 − P_Mig)S^GS with M + δM in (W9). I checked the expansion: (1 − P)q²/2(M + δM) = (1 − P)q²/2M − E^Mig_1 + O(PδM/M, δM²/M²). The X-sector recoil term P_Mig q²/2M (REF-A's point) is correctly added. Sizes: P_Mig(1 keV) ≈ 5.1×10⁻³ and crossover ≈ 53 eV, both reproduced ([E], ⟨r²⟩ = 1 Å²) |
| V12 L20 observable, truncation (A), U | RESOLVED | ν = ℋ_nuc + E_st. (A) is "exact by definition", and the 4m_eE/M justification is explicitly rejected. U_FP → E_st and U_EDFT → electronic. Discrepancy (5) (u in f_n) is added; I had verified it for both papers in R7 |
| V13 L21 step-model region; seed envelope | RESOLVED | The failure point ω ≈ ε_eh(2.1 − b_N) = 7.17 eV is checked and labelled heuristic. The α-envelope no longer bounds θ_seed, and the "50% in p₂" attribution is marked UNRESOLVED and unused |
| V14 R&K claims | RESOLVED | "Δ undefined" is withdrawn. The bound direction now uses F(1/ϵ − ϵ) ≥ 0 (C2d). C in "eV" is added. C2e (0.130 = exact at F = 0.112) matches my R7 number |
| V15 2001.06503 / 2209.04503 claims | RESOLVED | "½εS_e not derived" is withdrawn and replaced by the (D)-inconsistency objection plus the forward-peaking estimate. C26: ⟨T⟩/(T_max/2) = 2T_min ln r/(T_max − T_min) = 0.0138 at r = 10³, correct. The Z₁ wording is "Bohr-stripped effective Z₁". The D1 settlement agrees with my R7 reading |
| V16 2506.03810, 2301.06592 | RESOLVED (stood) | The inference is relabelled as our [E], with the momentum-tail caveat |
| V17 (W8), (W9) | RESOLVED (stood) | — |
| V18 renewal non-lattice | RESOLVED | Hypotheses (r1)–(r3), [D, sketch]. The deterministic-loss toy m(E) − E/d = −{E/d} is correct. A W⁻² tail gives a second moment ∝ E, which breaks (r3). Stronger than my R7 request |
| V19 vacuous checks C1c, C7b, C14e, C20b, C20c | RESOLVED | See §2 |
| V20 contested corrections | n/a | Rebuttals R8.2(a)–(c) are addressed to REF-A, not to me. I note (a) is correct: 𝔊(0) = 1 under (H-t) |
| R7 "required corrections" 1–11 | all RESOLVED | Mapped as above; closing-table rows B-1…B-20, B-L22, B-(d), B-(e) |

## 2. Rewritten checks (formerly vacuous)
| Check | v3 content | Verdict |
|---|---|---|
| C1c | Exponent bookkeeping (E, L) of R&K Eq. (9). Real-space Δ gives (3, 0) = E³, matching Eq. (8). A k-space Δ gives (3, 6) | Non-vacuous. It can fail and it discriminates the two readings of Δ. OK |
| C7b | Derives ⟨p²⟩ = Mω/2 from the harmonic Gaussian ground state, then the DOS mixture gives E^kin = ⟨ω⟩_D/4 | Non-vacuous. OK |
| C14e | Exact-rational test cases of ½Σ\|𝔉\| ≤ 2πΓ^ph max\|c\| and of K_ν ≥ 0 when 4π max\|c\| ≤ 1, plus a trivial solve for 1/(4π) | The test-case part is a genuine check. The symbolic solve is a restatement but harmless. OK |
| C20b | Series in ε (δM → εδM, P → εP) of prescription minus exact split. The O(ε) coefficient vanishes; the O(ε²) term is q²(PδM/M² + δM²/M³)/2 | Non-vacuous. It would fail without the X-sector recoil term or the (1 − P) factor. OK |
| C20c | P_Mig(1 keV) = 5.13×10⁻³, δM/M = 2.73×10⁻⁴, crossover 53.3 eV | An [E] arithmetic record, now honestly labelled. OK |

Also re-checked:
- C2d, C5a–c, C6b, C18, C19, C21a,b, C22, C24, C25, C26: correct.
- C15a (cascade onset 4Δ_BCS: the hotter QP needs E ≥ 3Δ to emit a pair-breaking phonon and keep E ≥ Δ, so ω ≥ 4Δ): correct. This is a self-found fix outside my items.

## 3. New errors in the changed sections
- **N1 (minor, §6.4(iii), C19).** The comparison "residual-KE variance 0.21 eV²/carrier ≫ ω₀⟨E_res⟩ = 0.066 eV²" uses the wrong comparator. Shot-noise
  variance scales as ω₀ times the **phonon** heat per carrier, not ω₀ times the residual kinetic energy ⟨E_res⟩ = 1.04 eV. In the Klein picture the phonon
  heat per carrier is ~ rω₀/2 ≈ 0.25–0.5 eV (Eq. (16) E_r ≈ 0.5–1 eV per pair), so ω₀·(phonon heat) ≈ 0.016–0.03 eV². The conclusion (residual variance
  dominates) is strengthened, but the stated number and its label must be fixed.
- **N2 (minor, §1.5 positivity sentence).** "K_ν ≥ 0 … holds for Γ/δ ≲ 1.7, i.e. on the whole O4-d11 map (Γ/δ ≤ 0.6)" reapplies the **Si** Γ/δ
  map to GaAs. That is the defect the same section corrects three sentences later ("Γ/δ for GaAs is unknown"). Fix: "K_ν ≥ 0 wherever
  Γ/δ ≲ 1.7 (with the [E] phase); whether GaAs satisfies this awaits the GaAs Γ/δ map".
- **N3 (cosmetic, §8).** "constrain a linear combination of the two" now refers to three nuisances (θ_GW, θ_Z, θ_{R-k}). Also, θ_Z (a global
  factor of 0.8–1 on Γ_ii) and θ_GW (±20%) are largely degenerate. WP6 should be told to treat them as correlated, or to merge them.
- **N4 (nit, C27 label).** "first moment = πω_p²/2 = f-sum (no e–h weight left)" holds in the q → 0 Drude limit only (see V3).
- No error found in (W16), (W1′), (W17), WP5-cp1–cp3, the (B2a,b) numbers, the Migdal expansion, the thresholds, or the L20/L21 rewrites.

## 4. Overall
**WP5-v3 resolves every REF-WP5-B item.** It introduces two minor errors (N1 and N2) and two cosmetic ones (N3 and N4), and none of
them changes a conclusion. My recommendation is to accept for rung 4 once N1 and N2 are fixed. The statuses in §11 of v3 match the
evidence.
