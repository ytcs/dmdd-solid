# R12 verification VER-WP7-B2-A (isolated; referee A of R11)

Under review: returns/R12/WP7-B2-v2.md and code/WP7-B2-v2/checks.py. I re-ran the checks: 39/39 PASS.
Against: my referees/R11/REF-WP7-B2-A.md, WP0-v3, NOTATION and CONVENTIONS.
Full text fetched for the two-phonon value: Deinzer & Strauch, PRB 69, 045205 (2004), "Two-phonon infrared absorption spectra of
germanium and silicon calculated from first principles". It is open access (Univ. Regensburg epub 1971, via Unpaywall) and its Fig. 3
plots the Ikezawa–Ishigame 293 K data. It was saved to literature/papers-r12-VER-WP7-B2-A/ and deleted after use.

## 1. R11 items
| R11 row | Item | Verdict | Note |
|---|---|---|---|
| 1a | (B2.1.1)–(B2.1.2), Eq. (42) | RESOLVED | Acoustic condition is now c_νv ≪ 1 |
| 1b | Coupling-to-mass "generalised" | RESOLVED | Invariant under v → v − λM for any λ; the source's orthogonal projection is stated |
| 1c | GaAs ×0.47 | RESOLVED | Dropped. LO residue Z − Z*/ε_∞ (C21, re-run). Ratio 0.114 and the 46% sensitivity re-derived (dd/d(Z*/ε_∞) = −0.0277). Footnote 2 credited; Fig. 2 marked UNRESOLVED. The spec now requires the same Z*, ε_∞ in the mixing term |
| 2a | (R3) scope | RESOLVED | Exact for mass-independent vertices, leading order in σ_M/M̄ otherwise |
| 2b, 2c | S5; glass ε | RESOLVED (no change needed) | — |
| 2d | C^{IR} ∝ ω² | RESOLVED | Dropped. Now A + Bω² (cond-mat/0604205), with the incoherent estimate as the A term. Gap 1 rewritten |
| 2e | Isotope channel | RESOLVED, with one NEW ERROR in its new comparison (§2) | 1.879×10⁻⁴ mass-weighted (C4a). Novelty UNRESOLVED, worded "not found [E]" |
| 3 | Gap 6 wording | RESOLVED | Closed for S_self and for S_dist at n_ph = 1; n_ph ≥ 2 is sketch |
| 4 | §10(iii) Born | RESOLVED | f(v) criterion; V/E = 1.29 at v = 1.2×10⁻³ (C26); Eq. (12) derived (C22, matches my R11 check); axisymmetric DWBA in the spec |
| 5 | Solid He | RESOLVED (no change needed) | — |
| 6 | Larmor, Polder, λ_S | RESOLVED | Cited as standard [UNVERIFIED citations, correctly tagged]; any T; AFM statement at B₀ = 0; λ_S = g_J − 1 only for J multiplets |
| 7 | Ni²⁺ bracket | RESOLVED | ≈ 0.83 (C24); 1.19 withdrawn |
| 8a | Magnetic-dipole single phonons | RESOLVED | (B2.7.0) one-phonon j_T vertex checked: ⟨1\|P\|0⟩ = i√(Mω/2N)e*, lattice sum N, giving √N(eZ*/M)√(Mω/2). The overall phase is stated as convention-dependent. u × P is now the readout operator |
| 8b | L^{ph} selection rule; κ | RESOLVED | κ is retracted as a finding; the selection-rule point is kept |
| 8c | SMM S⁺ branch | RESOLVED | (B2.7.2): the m = −S S⁺ line at D(2S−1) − ω_Z with weight 2S is re-derived (C16) |
| 8d | 2601.01043 | RESOLVED (no change needed) | Quote fixed to Eqs. (17)–(18); 0.25 tagged [E] |
| 9 | X10 screening | RESOLVED | n_r/\|ε\|² = 1 + (3/2)ω_p²/ω² = 1 + 1.24×10⁻³ (12 e/atom), matching my estimate |
| 10, 11 | D2, D5 | RESOLVED | (M) now includes orientation independence |
| 12 | Eq. (48); source-defect list | RESOLVED | The ×3 residual of Eq. (49) is stated; rigid-ion vertex and κ retracted as defects |
| C | Notation, Theorem D chain, τ | RESOLVED | ω_Lar, 𝔰_net, mode label ν (no leftover e_Iλ/ω_λ; m_s kept only as species mass). Spin-ordered targets removed from the GS chain (LSWT route, OW0-17). T is in every τ |

## 2. The two-phonon value used in the isotope B−L comparison (§2.4, C27, gap 2)
**The value.** The return uses α ≈ 9 cm⁻¹ near 76 meV (≈ 610 cm⁻¹), Si, room temperature, giving Im(−1/ε) ≈ 6×10⁻⁵ [UNVERIFIED].
**Full-text check.** Deinzer–Strauch Fig. 3 (293 K; experimental diamonds from Ikezawa & Ishigame) shows the 610 cm⁻¹ peak at
α ≈ 9–10 cm⁻¹. **The value is CONFIRMED** as a 293 K peak value. The conversion is also right: ε₂ = αn_r/ω = 8.0×10⁻³ with
n_r = 3.42, so Im(−1/ε) = ε₂/|ε|² = 5.9×10⁻⁵.
**NEW ERROR (frequency mismatch, conservative direction).** C27 combines D(50 meV) ≈ 20 eV⁻¹ with Im(−1/ε) taken at 76 meV.
76 meV lies above Si's one-phonon band (ω_max ≈ 64.5 meV), where D = 0 and the isotope channel vanishes. The ratio must use both
quantities at the same ω. At 50 meV (403 cm⁻¹) the same figure gives α(293 K) ≈ 0.5–0.6 cm⁻¹. Then:
- ε₂ ∝ α/ω, so Im(−1/ε) ≈ 5.9×10⁻⁵ × (0.55/9.5) × (76/50) ≈ **5×10⁻⁶**;
- the ratio becomes Γ_iso/Γ_EM ≈ **6×10³** (at 293 K).
The text itself notes the in-band absorption is "smaller at mK": at T = 0 only summation processes remain, and the difference
processes that dominate below ω_max at 293 K vanish (Deinzer–Strauch §V, Fig. 1). So the ratio at mK is larger still.
Required correction:
- replace "~5×10², exceeds by ~10²–10³" by "≳ 6×10³ at 50 meV, using 293 K data (an upper bound on Im(−1/ε)); larger at mK";
- evaluate the ratio at matched ω inside the band;
- change the tag to [FT via Deinzer–Strauch Fig. 3, PRB 69, 045205; data Ikezawa–Ishigame];
- add α(403 cm⁻¹, 293 K) ≈ 0.55 cm⁻¹ as the in-band input;
- fix C27 to use the in-band ImL.
The qualitative conclusion (isotope channel dominant inside the one-phonon band, EM-like part alone above it) is unchanged and
strengthened. Gap 2 can be reworded: the room-temperature value is now verified, and only the low-T in-band ε(ω) is still needed.
The decomposition B−L = g[N·nuclear + (Z·nuclear − electron)] and (B2.4.1)–(B2.4.2) are correct: re-derived Γ_iso = πg²σ_wD/(2Ω_at)
from (B2.2.1). "Add without interference" holds because Z* is isotope-independent at leading order and the isotope phonon has no
photon mixing.

## 3. Other new errors in changed sections
- §3 τ: `K=1ph-coh` is used for the n_ph = 0 (elastic) term. The K slot has no elastic value (CONVENTIONS §11). Minor: flag it as an
  IF (e.g. `K=el`) rather than mislabel it.
- No other new errors found in §1 (B2.1.4), §2.1–2.5, §3, §5–§8, the closing table or the LIMITS rows. C21–C28 re-run and spot-derived.

## 4. Summary
All R11 items are RESOLVED. There is one NEW ERROR: C27/§2.4 evaluates the isotope-to-EM ratio with a two-phonon absorption taken
at 76 meV, outside the one-phonon band. The quoted α ≈ 9 cm⁻¹ itself is CONFIRMED (293 K peak). At matched ω (50 meV) the ratio is
≈ 6×10³ (293 K bound), not ~5×10². There is one minor τ label issue in §3.
