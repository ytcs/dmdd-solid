# R5 / NOTATION-APPLY: conventions, symbol table v3, corrections index, consistency audit

Conventions/notation agent. Read: STATEMENT (v2, v1), FRAMEWORK, LIMITS, NOTATION v2, CONTROLS, DONE, RULES, README, log, LAUNCHES,
registry, state/*, returns/** (D1, D2, X1, X2, WP0–WP6, O4), referees/R2/*, literature/L1.md. No return or referee file was edited.
Written: CONVENTIONS.md (new), NOTATION.md (v3, rewrite), state/CORRECTIONS.md (new), this report.
Audit script (sympy, 26 checks, all PASS, < 10 s): `/tmp/claude-0/-home-user-breakthrough-maths/30a63adb-c597-5cb8-b46c-4c5645c8b7d4/scratchpad/notation/audit.py`.
It lives in the session scratchpad because the brief restricts writes to four files; per RULES the coordinator should copy it to
`code/NOTATION-APPLY/audit.py` before any number here is cited in the paper.

## 1. What was decided (details and one-line reasons in CONVENTIONS.md)
- Units HL, e² = 4πα, Coulomb kernel v_C(k) = e²/k²; Fourier e^{+iq·r}; q from DM to target; ω to the target, ω_q = q·v − q²/2m_χ − Δ_χ.
- ρ_mn O(1) (no N); M^{(2)} in D1 normalisation (D2's is M/√N); ℓ_Q with N outside; phonons b, magnons a; EPW g as NOTATION v2.
- S_ab per WP0 (3.1), R not χ, Π^γ only for the e²-normalised photon self-energy; S = (2q²/e²)L/(1 − e^{−βω}); spin 2 inside S.
- ∫_ℝ ωS = π𝓃_eq²/m_e; [T, n_q] = q·j exactly.
- Screening: proper = R̃; three channels (ext + LFE, DFPT, pair); M̃ = X2 (2.2); coupling vector c_s fixes the external-field type.
- Halo: 2105.00599 (ρ_χ = 0.3, v₀ = 238, v_esc = 544, v_⊙ = (11.1, 250.2, 7.3)); v_E(t) in integrals; reference v_E^ref = 250.5 km/s,
  v_max = 794.5 km/s; isotropic factor η/(2q); rates per unit target mass.
- "Debye–Waller" = FC e^{−2W} only (AH tadpole is Σ^{AH}); GS/X0/X+ sectors (G → GS); sideband = X+, ZPL = X0; outside the window the
  Dyson convention DC (O4's "C1") with O4 d1–d11.
- τ = (n_B, n_g, n_A, 𝒳, n_T, K, 𝔐, n_D), with 𝒳 (was X), new K labels (coherent/incoherent), and metadata T, ref, scr, conv.
- Error tags [D], [D, sketch], [E], [C], [FT], [ABS], [UNVERIFIED]; statuses incl. SUPERSEDED; correction types S/N/W.
- NOTATION v3: ~300 rows, 162 ⚠ markers; every colliding meaning has a distinct name; a "Returns" column gives local names.
- Label namespaces collide heavily (C1, D1, W1, N1, R1, T1): always cite with the return prefix (CONVENTIONS §14).

## 2. Consistency audit of the key formulas (mapped to CONVENTIONS)
| # | Formula | Returns stating it | Check | Verdict |
|---|---|---|---|---|
| 1 | Master rate Γ_χ = ∫d³q/(2π)³ tr(𝔇S(q,ω_q)) | W0 (3.3); D1 N4; D2 §0; W1; W2 (5.3), (8.1); W3 (W.1); W4 [3.1], [7.2]; W5 (W6); W6 (1.2) | WP0 bookkeeping; W4 magnon [2.2] = (3.1) with ⟨ν,k\|s\|0⟩ = √N ℰ; W4 [7.2] prefactor m_χq*/(πΩ) (A15) | AGREE |
| 2 | Isotropic velocity kernel 𝒢 → η(v_min)/(2q) | W0 (9.1), W2, W3, W4, W6 (C10a), REF-A | A1 | AGREE, except D1 (η/q) and REF-B §1 (verified η/q): **owed** |
| 3 | dℛ/dω = ρ_χσ̄_e/(4πm_χρ_Tμ²)∫q dq F²ηS̄ | W0 (9.2); W6 (1.4); Hochberg (S.9); 1509.01598 (17) via dictionary | A2, A2c, A3 | AGREE; D1's 1/(2π) is 2× (A2b) **owed** |
| 4 | S ↔ L: S = (2q²/e²)L/(1 − e^{−βω}) = q²L/(2πα(…)) | D1 §3, D2 §0, W0 (5.4), (9.3), W1 [E1], W2 (4.1), W4 [4.1], (4.4), W5 (W1), KKL (6), Hochberg (1) | A4 | AGREE (W3 (W.4c) drops the thermal factor; immaterial at T ≪ E_g) |
| 5 | ε₂ = (e²/2q²)(1 − e^{−βω})S^{prop} | D1 N6, D2 §0, W4 (4.4) | by inspection | AGREE |
| 6 | \|f_crys\|² = Ωq³S̄/(4παm_e²) = Ωq⁵L̄/(8π²α²m_e²) | W1 [E12], W6 (1.5), 2101.08275 (16) | A5, A5c | AGREE; D1's Ωq³S̄/(2παm_e²) follows only from η/q (A5b) **owed** |
| 7 | ε₂^{PA} = (8π²α/Ωq²)⟨⟨Σ(n+½±½)\|M\|²δ⟩⟩; S^{X+} = (4π/Ω)⟨⟨…⟩⟩ | D1 (2), (4); D2 (2.2); X2 (2.3) (M → M̃); W3 (W.4c); W0 (5.6) structure | A6, A6b | AGREE after M_D2 = M_D1/√N, V = NΩ |
| 8 | Optical limit ε₂^{PA} = (8π²α/Ωω²)⟨⟨\|ê·(A₁^v+A₂^v)\|²…⟩⟩ | D1 §6.1, D2 C1, W3 L9 (EPW (63), Noffsinger (1)) | A7, A7b | AGREE (full-text closure in WP3) |
| 9 | M^{(2)} (two orderings, unrestricted m) | D1 (1), D2 (2.1), X1, X2, W3; EPW/Noffsinger S1/S2 | A8 (on-shell denominators); EPW denominators = −(ours), overall sign drops out | AGREE (D2 = D1/√N; WP0 (4.9) uses D2's ℓ_Q) |
| 10 | Soft acoustic limit (C7) | D1 §6.2, D2 C7, W0 (4.9), X1 (X1), W3 §3, CONTROLS C7 | A9 (X1′ → X1) | X1 = W3; D1, D2 FALL (REF); W0 (4.9) only at band extrema **owed**; CONTROLS C7 last sentence contradicts C7a–e **defect** |
| 11 | M̃ (pair channel); M ∝ ρ ⇒ M̃ = M/ε(P,ω_f); rigid limit ε(q,ω∓ω_Q) | X2 (2.2), §5; W0 (5.6)–(5.7); W3 §3; REF-A §5 | A10 (coherent potential), A10b (X2 K5) | AGREE (W0 (5.7) is a truncation); external weight in GaAs: **defect** (item D4) |
| 12 | Halo functions η, ξ = 2∫v′η dv′; η̃ = ρσ̄η/m | W6 (1.3), 1509.01598 (15), 2311.04957 | A11 | AGREE |
| 13 | f-sum: ∫₀^∞ωε₂ = (π/2)ω_p²; ∫_ℝωS = π𝓃q²/m | CONTROLS C4, D2 §3, W0 (4.6), (9.5), W1 [E11], W2 (3.4), W6 W1 | A12, A12b; A13 (commutator) | AGREE; W0 (8.2) 2π is 2× **owed**; W0 (4.6)/(5.3) commutator term **owed** (no f-sum effect) |
| 14 | Other sum rules | spin 𝓜¹ = 𝓃_eq²/4m_e (W0 (4.6e)) ↔ W1 [E6] ¼S^{IP}; 𝓜¹_eκ = 0 (W0) ↔ W3 J7 (split ≠ 0, total 0); zeroth moment: REF-B, W3 J4 vs O4 (vi), X1 BN | by inspection | AGREE; O4 (vi) wording must be scoped to the Fan part **owed (W)** |
| 15 | Third-moment / κ₃ links | W0 (4.7), W2 (5.2), W3 J3 | not comparable yet | OPEN (WP2 gap 7) |
| 16 | σ̄_e anchor and F_DM | W0 (2.3), D1 N5, D2 §0, KKL (11)–(12) | A16 | AGREE |
| 17 | Thresholds and edge masses | L1 (0.34/0.47 MeV), W1 §3.4 (0.473), W6 (3.1) (0.319, 0.285, 0.358) | A17 | AGREE (differ only by E_th and v_max inputs; annual band 0.307–0.330 MeV at 1.12 eV) |
| 18 | Hyperfine contact | W0 (1.2), W4 D1 | A18 | W0 2× **owed** |
| 19 | Fano thinning F_meas = ϵ_detF + 1 − ϵ_det | W5 §6.2 (vs R&K App. A) | A14 | AGREE with W5 (source error) |

## 3. Residual defects for the coordinator (not removable by renaming)
- **D1. CONTROLS.md C7** still ends "A uniform rigid shift … M^{(2)} → 0 as Q → 0 for acoustic branches", which contradicts the
  adopted C7a–e (the limit is X1's soft factor, generically ~10²× iℓ_Q ê·q). Delete the sentence.
- **D2. REF-B §1** states that D1's η/q angular average was verified. It is wrong (REF-A §1, WP0 (9.1), audit A1). Record in SOTA's R2 row.
- **D3. WP6 §7.3 library string** writes `nT=130K` in the n_T (order) slot. Fixed by convention (CONVENTIONS §11); the WP6 spec must follow.
- **D4. External local-field weight in non-centrosymmetric targets.** X2 (2.2) and WP0 (7.2) use Σ_G(ε̃^{-1})_{G0}ρ(q+G) (potential side);
  WP1 [E2] derives (1+Rv)_{0G} from Im R = (1+Rv)Im R⁰(1+Rv)† (density side) and says they differ in GaAs. Equal for R_{GG′} = R_{G′G}.
  Whether the difference is physical or an index/conjugation convention has not been settled: REF-WP1 and REF-WP3 should resolve it
  (PAER in GaAs and the C8 decoy depend on it).
- **D5. Theorem D bookkeeping of zeroth moments.** O4 (vi) "Z + fp = 1, each m keeps its weight" versus REF-B/WP3 J4 "no zeroth-moment
  rule for n_e". The two are compatible only if O4's statement is read as the Fan (self-energy) part per pair; the referees of WP0+O4
  should confirm the scope.
- **D6. v_E.** NOTATION v2 called 250 km/s "v_E"; WP6 shows 250.5 is |v_⊙| and the annual mean Earth speed is 252.1. Decided as
  v_E(t) in integrals, v_E^ref = 250.5 for scalars, annual range in the halo band. If the coordinator prefers the annual mean, every
  quoted threshold shifts by ~ −0.4% (m_min ∝ v_max^{-2}).
- **D7. ℓ_Q and M normalisations are mixed inside WP0** ((4.9) and (5.6) use D2's N-inside convention; (5.7) and the PAER rate use D1's).
  Harmless after mapping, but the WP0 erratum must state it.
- **D8. Missing symbol tables.** WP5 and WP6 (and the pre-directive returns D1, D2, X1, X2, WP0) have no "Symbols introduced/used" table;
  their renames are listed in state/CORRECTIONS.md §0–§12 instead.
- **D9. τ needs fields WP0 did not give.** Broken-symmetry references (WP4), screening channel set (X2/WP6) and resonance convention (O4)
  are now metadata; the coherence flag in K replaces x_coh (WP2). WP0's referees should endorse or revise CONVENTIONS §11.
- **D10. Open cross-check.** The κ₃ G/X split (WP2 (5.2)) against WP3's Migdal spectra and WP0 (4.7) has not been made by anyone (OPEN).
- **D11. SOTA hygiene.** SOTA still uses the retired yield symbol (P(Q|…)), lists the R1 C7 forms as live and the halo flags as open;
  the owed edits are listed in state/CORRECTIONS.md §15–§16 together with the README/LIMITS updates.

## 4. Collision statistics
Letters with three or more meanings across the campaign before v3: Δ (≥ 12), W (≥ 9), S (≥ 10), g (≥ 10), κ (6), η (7), ε (≥ 10), v (7),
Q (6), Λ (3), P (≥ 8), n (≥ 9), K (≥ 8), T (≥ 6), R (≥ 6), A (≥ 8), D (≥ 9), F (≥ 8), ξ (5), τ (6). All are resolved in NOTATION v3.

## 5. Symbols introduced/used
This return introduces no physics symbols; it defines the campaign set. New names (all in NOTATION v3): v_C, v_T, v_∥, v^g_n, p_{nn}, c_ν,
𝔄, 𝔖, s^W, K^{soft}, GS, 𝒳, DC, Λ₀/Λ₊, 𝓜¹, 𝓃_s, 𝒯_e, t_ph/t_g, ε_mac/ε_Mer/ε_Lin/ε_bg, W^{scr}, f_Hxc, 𝔗_G, r^{pair}, c_coh, δM^{intra},
ρ^{ren}, Δ_BCS/Δ_D/Δ_scis/Δ_Mott, δω, d_{A,m}, δρ_κ, δ_v, σ_ω, ζ_S, 𝒮_F, 𝔨_m, 𝒞_m, 𝔫_κ, w_κ, ρ^{ph}_κ, Π^{ph}, 𝒥_κ, x_κ, h^I_κ, b_{Qν}/B_{Qν},
g^x, g^{AH}, Σ^{AH}, ℋ, 𝔊, ϑ, 𝒦, ε_eh, F_eh, 𝔡_H, ϵ_det, E_el, Y_H, E^{Mig}_1, n_r, Ψ^{vib}, 𝒢 (velocity kernel), N_esc, κ_mix, e_χ, y_χ/y_e, ℛ, Γ_χ.
