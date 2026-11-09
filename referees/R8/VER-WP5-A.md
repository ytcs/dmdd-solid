# R8 verification VER-WP5-A of returns/R8/WP5-v3.md (against referees/R7/REF-WP5-A.md)

Read: WP5-v3 §1.1–§1.5, §3.1, §3.3, §6.1–§6.4, §11, §R8.1–§R8.3. Checks: code/WP5-v3/checks.py re-run, **55/55 PASS**.
Isolation kept: REF-WP5-B was not read; the B-items appear here only as WP5-v3 cites them.
No new literature fetch. The rebuttals are adjudicated against the passages I read in full text for R7 (2209.04503 p. 1 and p. 4).

## 1. Item-by-item verdicts (R7 V1–V20 and §6 sub-items)
| R7 item | Verdict | Note |
|---|---|---|
| V1 (W1) out-rate; Z factor; exchange | RESOLVED | (W1) now carries [1−f][1+n_B]. (W16) gives 2\|ImΣ\| = Γ_out + Γ_in. θ_Z is global ~20%. (d) is tagged beyond hypothesis. (W1′) anti-Hermitian LFE form checked: W_{GG′} = ε⁻¹_{GG′}v_C(p+G′) and −2Im(ρ†Wρ) reduce to 2v_C\|ρ\|²Im[−ε⁻¹_00] at G = 0 |
| V2 ε_ion ↔ g^L | RESOLVED | WP5-cp1–cp3 stated and propagated to §1.5 (O4-d2) and §2 |
| V3 Born parameter | RESOLVED | Z_κα/v_F ≈ 15 / 35 everywhere I checked (§1.1(e), §3.3, §6.1) |
| V4 (H-t), (H-m) | RESOLVED | Adopted, with a better rationale (rebuttal (a), accepted below) |
| V5 (B2) density and criterion | RESOLVED | (B2a) Pauli occupation 3%; (B2b) n a_X³ = 5–19 at 1 keV, so [C] there; ~0.5 for 30 pairs, so marginal [E] (rebuttal (b), accepted); θ_dense added |
| V6 Lindhard BCA + Markov | RESOLVED | Truncation 0 in §6.1 step 3. Bonus fix: ν = ℋ_nuc + E_st replaces ν = ℋ + E_st (correct: (W4)'s ℋ contains ≈ 69% of E_el as carrier heat) |
| V7 R&K/KP/F_NR moments | RESOLVED (stood) | unchanged |
| V8 renewal → [D, sketch] | RESOLVED | (r1)–(r3) stated; C24 toy checked (m − E/d = −{E/d}) |
| V9 (W14); (iii) inconsistent | RESOLVED | (iii) tagged [E, inconsistent model], no evidential weight |
| V10 (R-k) | RESOLVED | Γ_E includes Γ_ii; (R-k′) added; error [E]; R2 extended |
| V11 thresholds | RESOLVED | 352/395 eV; 336/382 eV with the exact quadratic (I re-solved 2m_ev(v+v_F) = E_g: 336, 383); "strongly suppressed, not zero" |
| V12 [A] = E³ | RESOLVED (stood) | — |
| V13 \|M\|²; Δ | RESOLVED | "Δ undefined" withdrawn |
| V14 App. A bound reason | RESOLVED | F(1−ϵ²)/ϵ ≥ 0 now given. 0.130 = exact value at F = 0.112: checked (0.98·0.112 + 0.02 = 0.1298) |
| V15 2001.06503 | RESOLVED (stood) | — |
| V16 ½εS_e; Z₁ | RESOLVED | ½εS_e claim withdrawn, App. B cited; Z₁: rebuttal (c) accepted. NEW ERROR in the replacement argument (§3, N1) |
| V17 (W15) | RESOLVED | (W17) makes c^F dimensionless (Γ·(\|ρ\|²/E)/\|ρ\|²). Kramers trace for Ge. Worst case 0.3Γ/δ with 0.11 as optimistic. K_ν ≥ 0 iff 4π max\|c\| ≤ 1, checked: K_ν ≥ Γ^{(ν)}(1 − 4π max\|c\|)/Γ^tot. "GaAs Γ/δ unknown" caveat added |
| V18 Migdal/GS bookkeeping | RESOLVED | 𝓜⁰_GS = 1 − P_Mig and 𝓜¹_GS = (1−P_Mig)q²/2M − E₁^Mig, both checked. Expanding (1−P)q²/2(M+δM) gives (1−P)q²/2M − E₁ + P·E₁ + O(δM²), so the stated residual O(Pδ, δ²) holds. Prescription (1−P_Mig)S^GS with M+δM. Minor (§3, N4) |
| V19 spec | RESOLVED | §2 fixes the rate definition (Γ_out, θ_Z) and the code-pair conditions |
| V20 θ_seed | RESOLVED | 50% misattribution marked UNRESOLVED and not used; envelope demoted to illustration |
| §6 lit. ratings | RESOLVED | REFUTED claims dropped; ratings carried as stated |

Count: 20/20 RESOLVED. NEW ERRORS: N1 (one substantive point), plus minor items N2–N4 (§3).

## 2. Rebuttals addressed to REF-A (§R8.2)
**(a) V4, "𝔊 ≡ const spuriously solves (W3) at ϑ = 0": ACCEPT.** At ϑ = 0 every e^{ϑ·δ𝐍} = 1 and the terminal data are 1. Constants c
solve Γ_x c = Σ_c∫𝒦_c c^{m_c} only if c = 1 (for branching with m ≥ 2 and absorbing states reached, c = 1 is forced by the terminal data). Under (H-t),
𝔊 = E[1] = 1 is the true solution, so my wording was wrong. The real role of (H-m) is the one given:
- if termination is not a.s., 𝔊(0) = Pr(termination) is the minimal root of the fixed-point map, and 1 is a spurious root;
- toy check: f(s) = (1−p) + ps² has roots s = 1 and s = (1−p)/p (since ps² − s + 1 − p = (s−1)(ps − (1−p))). For p = ¾ the minimal root is ⅓.

My substantive request (state (H-t) and (H-m)) is met.
**(b) V5, scope of (B2) for ≲ 100 eV seeds: ACCEPT.** n = 30/(4π/3·(10⁻⁶ cm)³) = 7.2×10¹⁸ cm⁻³. With a_X = 4 nm, a_X³ = 6.4×10⁻²⁰ cm³,
so n a_X³ = 0.46. By my own criterion that is marginal, not ≪ 1. A denser initial cloud (100 eV electron range of a few nm) worsens it.
The cloud expands while the cascade runs, so the time-averaged value is lower; "[E], marginal" is the right tag.
**(c) V16, Z₁ = 12 enters C: ACCEPT (UNRESOLVED → CONFIRMED).** Page 1 of 2209.04503, which I read in R7, defines a = 0.8853a₀/Z,
Z = Z₁^{0.23} + Z₂^{0.23}, "with suitable values of the effective atomic numbers of the incident ion and the target atom Z1 and Z2", and
C = 16.2616/(ZZ₁Z₂). Page 4 fixes "the effective number of valence electrons in the incident ion is Z1 = 12, while Z2 = 14". The page-1
definition reserves Z₁, Z₂ for *effective* numbers, and page 4 supplies them. The loose phrase "number of valence electrons" (a Si atom has 4)
does not override the explicit symbol assignment. Arithmetic: 16.2616/((12^{0.23} + 14^{0.23})·168) = 0.0268 keV⁻¹, +10% vs 0.0243.

## 3. New errors in changed sections
**N1 (substantive, §6.1 Discrepancy (3), WP5v3-C26): the "forward-peaked dσ_n" objection uses the wrong weight; withdraw it or tag [E].**
In 2001.06503 App. B, Eq. (29) applies the mean-value theorem to ∫dσ_{n,e} T_n(ΣT_e). There T̄_n is the average of T_n **weighted by the
electronic loss ΣT_e in the same collision** (same impact parameter b), not by dσ_n alone. Electronic loss per collision grows toward small b
(closest approach), which is where T_n is large. So the relevant weight favours large T_n, and ⟨T⟩_{dσ_n ∝ T⁻²} ≪ T_max/2 (0.014) does not bear
on t̄_n. The direction is even plausibly opposite: t̄_n ≳ ε/2 is possible. The C26 arithmetic is right, but it is applied to the wrong average.
The **first** half of the objection stands [D]: under (D)/(III) each event has T_n = 0 or ΣT_e = 0, so the cross term vanishes and a
½εS_e ν̄″ term is inconsistent with the approximation that produced S_e. Keep that half; drop or re-weight the second.
**N2 (minor, §6.2 Validity): circular b_N.** "ω ≳ ε_eh(2.1 − b_N) ≈ 7.2 eV" inserts b_N = 0.19. But 0.19 is only the value at which the
step-model mean would agree with the URF asymptote; the URF b_N is not computed. Either quote ω ≳ 2.1ε_eh − ε_eh b_N with b_N unknown, i.e.
≈ 7–8 eV for |b_N| ≲ 0.3 [E], or say "≈ 2ε_eh". The heuristic is otherwise fine.
**N3 (minor, §6.1 Discrepancy (5), new, attributed to REF-B): overstated.** In 2209.04503, ε_R = η̄ + ν̄ with the sub-threshold boundary
ν̄ = ε + u = ε_R (Eq. (4) with s ≤ u). So the primary's u is counted in ν̄ (atomic), not in the electronic fraction, and f_n = 0 below threshold.
The inconsistency is real only for the U spent in secondary collisions. Those enter the recursion as ν̄(T_n − U), are absent from ν̄, and so
fall into η̄ = ε_R − ν̄ by complement. Restate it as "U lost in secondary displacements is booked as electronic by the complement definition".
The bound "up to u/(ε+u)" is not derived; tag [E] or remove it.
**N4 (minor, §3.1 size): "≲ 1% at keV" needs a range.** P_Mig ∝ E_R in the REF-A soft form gives ~5% at 10 keV. NR seeds in G3 go to 10 keV
(§3.4 grid), and the soft-limit formula itself degrades as q grows. State "≈ 0.5% at 1 keV, ∝ E_R, soft-limit [E]". Also note that the
1 Å² valence ⟨r²⟩ is my order-of-magnitude input, not a computed value: it should cite WP3's P_Mig(q) once available.
No other errors found:
- §1.1(a) plasmon restriction: checked (Drude: Im[−1/ε] = (πω_p/2)δ(ω−ω_p) saturates ∫ωL = πω_p²/2);
- (W16): checked;
- (B2a) occupation: checked;
- (W17) dimensions: checked;
- C20b expansion: checked;
- thresholds: checked;
- 0.130 at F = 0.112: checked;
- C23, C24 toys: checked.

## 4. Verdict
All 20 R7 items are RESOLVED. All three rebuttals are ACCEPTED. One substantive new error (N1, the dσ_n-weighted ⟨T_n⟩ argument in
L20 Discrepancy (3)) and three minor ones (N2 circular b_N, N3 overstated u-booking claim, N4 P_Mig size range) must be fixed. None of
them changes a [D] result or a LIMITS status. With N1 corrected, WP5-v3 meets my rubric at rung 4 for the items I refereed.
