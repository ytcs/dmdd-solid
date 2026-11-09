# R12 verification VER-WP7-D-B: returns/R12/WP7-D-v2.md against REF-WP7-D-B (R11)

Isolation as in R11. I read only the v2 return, code/WP7-D-v2/checks.py and my own R11 report.
Checks re-run: `python3 -I checks.py` gives **49/49 PASS** (about 5 s).
Independently re-checked here:
- (D.4) R_{I⁺I⁺} sign: by hand.
- N4: exact single-bin s/b = 2.650 at TS = 2.71 (mpmath).
- N12: dark-Compton series. URF 1 − 3x/2 + 5x²/2 − 35x³/8; paper 1 − 3x/2 + 5x²/2 − 15x³/4 (sympy).
- (F.7): t = ω² − q² = 2m_χω − m_χ².
- §2.4(a): wording of the density-row-alone term.
- §1.4(i): the condition t_int ≫ min(t_coh, 1/Γ_T), tested in the two limits (monochromatic drive; white drive on a narrow line).

## Item-by-item
| R11 item | v2 location | Verdict | Note |
|---|---|---|---|
| V1 / A1 k sign in (D.1) | (D.1), (D.3), N2 | RESOLVED | weight at k = −m_φv. (D.3) pairs 𝒮_φ(k,ω) with R(−k,ω), consistent with its second equality |
| V2 coherent amplitude | §1.3 | RESOLVED (STANDS) | N1 adds an independent quantum Kubo-sign test |
| V3 stationary coupling, "any t_int" | §1.4(i) | RESOLVED | condition t_int ≫ min(t_coh, 1/Γ_T) is correct in both limits; windowed form plus counterexample given |
| V4 / A2(i) R label and ⟨I^z⟩ sign | §1.5, N3 | RESOLVED | R_{I⁺I⁺} for H = +ω_LI^z, ⟨I^z⟩ < 0: checked by hand |
| V4 / A2(ii) "resonant growth agrees" | §1.5(b), IF-D11, L-D1 | RESOLVED | now UNRESOLVED by a factor 2, with both readings stated |
| V4 / A2(iii) u formula | §1.5 | RESOLVED | [D, sketch]; supplement declared unread |
| V5 / A3 crossover 3/2; double counting | §1.6, L-D3, N4 | RESOLVED | "O(1)·t_coh", constant dropped from LIMITS; "apply one or the other, never both". The new "3–10" penalty is from 1905.13650 [ABS] only (tagged) |
| V6 / A4(i) "1/ε₀ = slab case" | §1.3, §1.7, IF-D9, N10 | RESOLVED | withdrawn; orientation factors 1 / 3ε₀/(ε₀+2) / ε₀ relative to bulk are correct |
| V6 / A4(ii) grid | §1.0, §1.10, N11 | RESOLVED | [m_φ, (1 + 3.6×10⁻⁶)m_φ]; v_max²/2 = 3.51×10⁻⁶ |
| V7 / A5 (D.8), Cu number, tag alignment | (D.8), §1.8, §5, L-D5 | RESOLVED | (D.8) displayed; δa/a sign correct; 2δ_rel^a, negative, [E, UNVERIFIED]; 0.045 kept only as an upper bound |
| V8 / A6 multiferroic near T_CM | §1.9, §1.10, IF-D13, L-D6 | RESOLVED | LSWT only for T ≪ T_CM; near-T_CM response is an exact remaining gap; longitudinal GL origin stated |
| V9, V10 fermionic class, NC nuclei | §2.1–2.4(a) | RESOLVED (STANDS) | the new A-C9 wording (density row alone gives m_χ²(1 − 2m_χ/M)) is correct |
| V11 / A7 2011.01940 sizes | §2.4(b), N6, IF-D10 | RESOLVED | numbers match mine (1.007 / 1.021; 0.887; 0.661–0.592). The J_T and Dirac caveat is stated; "paper wrong" downgraded to UNRESOLVED, which is acceptable (algebra CONFIRMED) |
| L-D8 spin-count equivalence (R11 (b)) | §2.4(b), N5a,b | RESOLVED | derived; residual R_{k′l′} normalisation correctly flagged UNRESOLVED-minor |
| V12 / A8 pair operators, per volume | (T.1)–(T.2), N8 | RESOLVED | derivative DM current with (p − p̄)^μ; rate per unit volume; ρ rescaling |
| V13 "first order in e"; "O(x²) relativistic" | §3.4, (T.4), N12 | RESOLVED | O(e²κ_mix). The agreement in fact holds through O(x²) (I had checked only O(x)); the x³ attribution is UNRESOLVED |
| V14 §3.1 reductions | §3.1 | RESOLVED | [D, sketch] |
| V15 §11.9 closed | §3.5 | RESOLVED (STANDS) | — |
| V16 Bethe log | §4.1, L-D11 | RESOLVED | [D, sketch] / UNVERIFIED |
| V17 / A9 n_r³ | §4.2, N9, L-D12 | RESOLVED | M1 ∝ n_r³, E1 ∝ n_r |
| V18 / A10 labels, collisions, unused symbols | header, §6 | RESOLVED | displayed labels are exactly (D.1)–(D.9), (F.1)–(F.7), (T.1)–(T.4), (S.1)–(S.2) (grep); X_rd, e_λ; h_mod and d_α used in (D.8) |
| (a) massive-ν̃ reduction | §2.5 | RESOLVED | O(Δ_χ/m_χ) stated, [D, sketch] |
| (b) PDF numbering of 1306.6089 | §1.5, §1.6, L-D3 | RESOLVED | HTML (2), (3), (8), (9) = PDF (A1), (A2), (A7), (A8) |
| (f) priority of the continuity remark | §2.4(b) | RESOLVED | UNRESOLVED; 2201.11905 [ABS] |

## New content checked (changed sections)
- §1.5(c) spin temperature, tanh(β_sω_L/2) = p: coth(β_sω_L/2)⟨I^z⟩ = −1/2 for spin ½, independent of p. This is correct and consistent with
  1306.6089 §A.3. No error.
- §3.3 identical-boson factor n_φ²/2 with the symmetrised 𝒯^{(2)}: consistent, no double factor. No error.
- (F.7) light scalar mediator: the algebra is correct (N7a,b). **NEW ERROR (minor, missing validity).** (F.7) is called "light mediator" but needs
  m_φ > m_χ. For m_φ < m_χ, m_φ² − t vanishes at ω = (m_χ² + m_φ²)/(2m_χ) < m_χ, which is inside the kinematic range: an on-shell
  pole, and χ → ν̃φ is open, so the DM is unstable. State "valid for m_φ > m_χ (a width is needed near the pole otherwise)". The source's own
  condition is m_φ ≫ m_χ.
- **NEW ERROR (cosmetic).** The label of check N13 says "the 1/2 of (T.3)". (T.3) is the dark-Compton operator; the ½ is in §3.3. Relabel the check.

## Verdict
All 18 R11 verdict items and the A1–A10 corrections are **RESOLVED**. There are 2 new errors, both minor: the (F.7) validity condition and the
N13 label. Neither blocks REFEREED status for WP7-D-v2.
