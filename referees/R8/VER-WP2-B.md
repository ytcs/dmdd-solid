# R8 / VER-WP2-B: verification of returns/R8/WP2-v3.md against REF-WP2-B (R7)

## Scope and checks
Read:
- WP2-v3 §0, §1.2, §2, §3, §5, §6.1, §7.1, §8.2, §9, §10–§14, and the closing table §16;
- my R7 report.

Same isolation as R7: I did not read REF-WP2-A, state/, or other returns.

Re-ran code/WP2-v3/checks.py: **31/31 PASS**. The quoted numbers are reproduced: j_BZ = 0.4436, 2𝓃_e/𝓃_e(R) = 1.19×10⁻⁴,
𝔯(51/102 keV) = 1.090/1.287, shell 1.8%/10.4%.

I checked these new formulas by hand:
- **(5.2″) closed form.** 𝔯(ξ) = 3 + 3/ξ² − 3(1+ξ²)arctan ξ/ξ³ expands to 1 + (2/5)ξ² = 1 + (qa)²/10. At ξ = 1 it gives 6 − 3π/2 = 1.288,
  which matches my R7 quadrature exactly.
- **Uniform term.** ∫₀^∞ j₂(y)/y dy = 1/3, so the uniform term is 6𝓃_e/3 = 2𝓃_e. As a cross-check, 𝔯(ξ → ∞) = 3, i.e. the uniform limit.
- **(3.4″) weighting.** The |c_κ|²/M_κ weighting is consistent with the per-species first moment.
- **GS f-sum.** (1 − P)q²/2M − E₁^Mig = (1 − P)q²/2(M + δM) to first order.
- **(6.1) normalisation.** The factor (2π/Ω)|c_κ|² equals ∫dω S_self. This was an error I missed in R7; REF-A was right.

## Item-by-item verdicts (numbering = rows of my R7 table)
| # | R7 item | R7 verdict | v3 status | Note |
|---|---|---|---|---|
| 1 | Vertex DW bookkeeping (e^{−W} on δρ_κ part); δρ_κ notation | SWC | **RESOLVED** | §1.2: O(2W) stated, C14; "(98)–(104) at O(u), q → 0"; NOTATION row change proposed (IF-11) |
| 2 | Coherent S (2.1)–(2.2) | STANDS | RESOLVED (kept) | 1910.08092 citation moved to line (91) |
| 3 | Shell indexing and the "≈2%" | SWC | **RESOLVED** | Pairs (ΔR, κ, κ′) with ΔR_κκ′; 1.8% at 10 keV, 10% at 2 keV, envelope 3%/15% |
| 4 | BZ-average theorem (2.4) | SWC | **RESOLVED** | All-ΔR κ ≠ κ′ terms with j_BZ(ΔR + r_κ − r_κ′); Σj = 1; hypothesis q ≫ max(n_ph, 2W)q_BZ. Gradient analysis correct: the self linear term averages to zero, the cross terms keep a linear piece. C9 wording fixed; C9b/C9c added. WP2-D1 "below q_BZ" downgraded to [E] (IF-10) |
| 5 | 2607.24933 Eq. (47) | SWC | **RESOLVED** | Charge limited to polarisation weights; caveat and non-use in their numerics stated; intra-cell charge withdrawn |
| 6 | (3.1)–(3.2) | STANDS | RESOLVED (kept) | — |
| 7 | (3.4′) qualifiers | STANDS | **RESOLVED** | Signed moment; multiplicative vertex; species-weighted (3.4″) |
| 8 | Panjer route at T > 0; ⟨n_ph⟩ | SWC | **RESOLVED** | Forward march at T = 0 only; FFT of e^{−2W}[e^Φ − 1] with regulator at T > 0; created number = ∫_{ω′>0} |
| 9 | Sherman–Morrison L4 | STANDS | RESOLVED (kept) | — |
| 10 | 1712.06598 Eqs. (5), (12) | STANDS | RESOLVED | CONFIRMED kept. Eq. (12) now also labelled the paper's declared "≈" estimate (correct; it is still a formula-level error) |
| 11 | (5.1) cumulants | STANDS | RESOLVED (kept) | — |
| 12 | (5.2) GS/X split; compute 𝔨₃^GS directly | STANDS | **RESOLVED** | "never as 𝔨₃ − 𝔨₃^X" in (5.2), L6, G3 |
| 13 | (5.2′) 𝔨₃ contact formula | STANDS | RESOLVED | "At all q" stated. The neutral-combination precision (V_eN + V_NN) is correct |
| 14 | κκ/eκ relation "exactly" | SWC | **RESOLVED** | (5.2″): trace part exact at every q; core term (qa_1s)²/10 (9%/29%); uniform 2𝓃_e (1.2×10⁻⁴) at q → 0⁺; "exactly" withdrawn in §0, (5.2″), IF-1 |
| 15 | (6.1)/(6.1′) | STANDS | RESOLVED, with A's normalisation fix accepted | — |
| 16 | 2309.10839 Eq. (9) | STANDS | RESOLVED (kept, v1 noted) | — |
| 17 | Toy 𝔨₃ 7% | STANDS [E] | RESOLVED | Θ(ω_max) cutoff caveat added |
| 18 | Spin channel "exact"; isotope disorder | SWC | **RESOLVED** | Exactness confined to incoherence; O(ΔM/M) caveat on the lattice-factor identification. n_ph ≥ 1 qualifier also correct |
| 19 | Cubic isotropy | STANDS | RESOLVED (kept) | — |
| 20 | 2205.02250 "discrepancy" | FALLS | **RESOLVED** | Dropped everywhere (§0, (5.1), L6, §13) |
| 21 | 2411.03433 IA width | SWC | **RESOLVED** | "Declared and quantified approximation" in (8.2)(iv) and L19 |
| 22 | Si/Ge Z* = 0 | STANDS | RESOLVED (kept) | — |
| 23 | Gap closures | SWC | **RESOLVED** | G3 cells with q ≲ n_ph q_BZ flagged or routed to (2.2); FFT at T > 0; G11 pair shells |
| 24 | Contested corrections | n/a | RESOLVED | §14 has no rebuttals; the inter-referee settlements are argued by derivation and agree with my reading |

Unverified quotes are now honestly tagged UNRESOLVED (hep-ph/0608035, 2011.09477, 2607.06005, 2506.11191, 1911.03482); no change requested.

## New errors in the changed sections
**None of substance.** Two remarks, neither a NEW ERROR:

- **R1 (wording, §2 Consequences (ii) and §12 gap 2).** The "≈ 4 × 0.44 × 0.3² ≈ 0.16" size of the κ ≠ κ′ BZ-averaged correction adds the
  four nearest pairs only. Since Σ_ΔR j_BZ = 1 while the four nearest already sum to 1.77, the farther pairs carry net weight ≈ −0.77. They
  enter with smaller but nonzero c̄^{n_ph}, so they partly cancel. "Up to ≈ 0.16 [E]" is acceptable as an upper-ish indicator; say "nearest
  pairs only; farther pairs enter with opposite-sign weight".
- **R2 (precision, (5.2″) uniform term).** 2𝓃_e is the electron-only uniform contribution in the limit q → 0⁺ (the q = 0 integral is
  shape-dependent, as stated). It is correct and agrees with WP0-v2's record of REF-WP0-A. It should stay labelled [D] for the uniform
  part and [D, sketch/E] for the G ≠ 0 anisotropic remainder, as written. No change needed.

## Verdict
All 24 items of REF-WP2-B are RESOLVED (the 9 STANDS-WITH-CORRECTION items and the 1 FALLS item applied; 13 STANDS items kept, several with the requested qualifiers; 1 n/a). No new errors were found. WP2-v3 passes on the REF-WP2-B
side; the only open item is still WP3's evaluation of 𝔨₃^X against (5.2″).
