# R16 / GAP-EF-v2 errata: the corrections of VER-GAP-EF-v2 applied

Agent ERR-GAP-EF-v2, brief briefs/R16/ERR-GAP-EF-v2.md. This is an **addendum**. Read it together with returns/R16/GAP-EF-v2.md, which is
not edited and stays the record. It answers every row of referees/R16/VER-GAP-EF-v2.md (VER) that is not plain STANDS: verdict rows 5, 6, 8,
11, 12, 14, 17 and 20; notes a.1–a.4; §(4) (i)–(iv); the LIMITS rows L-EF1, L-EF2 and L-EF4; and owed corrections V-1…V-14. **For the merger:**
where §2 or §3 below gives replacement text, use that text and not the GAP-EF-v2 original. Every passage not listed is unchanged.

Inputs read: returns/R16/GAP-EF-v2.md (all of it), referees/R16/VER-GAP-EF-v2.md, code/GAP-EF-v2/{cascade,model,checks}.py with
data/results.json and data/scan.json, returns/R13/WP5-v4.md l.165–182 and l.680–690 ((W4), (W4′), A-10), returns/R12/WP7-E-v3.md l.76–92
((E1-pr), (E1-W4)), CONVENTIONS §12–§14 and the R13 amendments, and NOTATION. **Literature:** four full texts were fetched with lit.py into
literature/papers-ERR-GAP-EF-v2/: 0911.1532, 2004.10709, 2311.05011 and 1902.02687. Per-page `.txt` extracts were kept and the PDFs and HTML
deleted. Page numbers are PDF pages.

**Numerics.** All runs are light: checks.py, one β-Ga₂O₃ solver run, and an mpmath evaluation of the Rényi gap law (≈ 1 s). There was one
scratch run of the λ_ph → 0 cascade at h = 0.0025, which took ≈ 2 min; it is quoted as such and is not in checks.py. **code/GAP-EF-v2/checks.py:
32/32 PASS in ≈ 18 s.** The solver (cascade.py, model.py) and data/*.json are unchanged, so data/results.json remains the record of the return.

**Status after the errata.**
- The solver is CROSS-CHECKED.
- (EF1)–(EF8), (EF12′), the revised (EF12) under (H-cap), and (EF13) are DERIVED under their stated hypotheses. §1.4 (the asymptote) is
  [D, sketch] plus GAP-EF-v2-C6.
- L-EF4 is CROSS-CHECKED, not DERIVED.
- Material numbers are [E].
- No GAP-EF-v2 result changes by more than its quoted digits. The θ_ii = 1, λ_ph → 0 row now shows 𝒱_> = 2𝒞_<> = 0 exactly (§2, R-6).

---
## 1. Resolution of each VER item that is not plain STANDS

**VER #5 / V-2: the λ → 0 closure. STANDS WITH CORRECTION; corrected further (Rebuttal R2).** The verifier is right that the "10⁻⁴" claim is
not met, and right about the mechanism, which is cascade.py l.74. It is wrong about the order of the artefact. Facts, from GAP-EF-v2-C23 and one
scratch run:
- **Mechanism.** At λ_ph = 0 and θ_ii = 1, the grid point x = E_g has 𝔓_t(0) = 0, so p_t = 0. l.74 then sends the carrier one step h down the
  "phonon" branch, even with phonon=False. N is unchanged. Energy h moves from ℋ_< to ℋ_>, with probability O(h) per carrier.
- **Size.** The spurious ⟨ℋ_>⟩ per carrier is 1.80 × 10⁻⁴, 4.50 × 10⁻⁵ and 1.13 × 10⁻⁵ at h = 0.01, 0.005 and 0.0025 (ratio 4.00, so
  **O(h²)**). Its variance contribution is 8.2 × 10⁻⁶, 1.0 × 10⁻⁶ and 1.3 × 10⁻⁷ (ratio ≈ 8, O(h³)).
- **The identity holds on every grid.** On each grid, (EF8) with this term booked, ε/E_g = 1 + 2(r̄_c + ⟨ℋ_>⟩/(2n̄)), holds to 10⁻¹⁵.
- **Why the extrapolated row misses.** Linear Richardson extrapolation, 2f(h/2) − f(h), maps ch² to −ch²/2 (sympy). The extrapolated row
  therefore carries −½ of the coarse-grid artefact: ⟨ℋ_>⟩/carrier = −8.98 × 10⁻⁵, 𝒱_> = −6 × 10⁻⁶ (the "negative variance") and
  2𝒞_<> = −1.5 × 10⁻⁴. This is why the row closes (EF8) without its ℋ_> term only to **1.8 × 10⁻⁴**. On the pair (0.005, 0.0025) the defect
  falls to 4.5 × 10⁻⁵.
- **θ_ii = 3/2 has no artefact.** The threshold grid point lies above E_g, so 𝔓 > 0 there, and the row closes to 10⁻¹⁵.
- **Physics.** ε_eh and F_eh are unaffected. In the model, ℋ_> ≡ 0 without phonons, so 𝒱_> = 2𝒞_<> = 0 exactly and 𝒱_< = F_eh = 0.0811.
  With the artefact heat returned to ℋ_<, r̄_c = (ε/E_g − 1)/2 = 0.29263 (grid pair 0.01/0.005) or 0.29265 (pair 0.005/0.0025), against the
  table's 0.2927. Every percentage built on r̄_c is unchanged at the quoted digits; for example, 0.6/0.29265 − 1 = +105.0%.

C23 now tests the per-grid identity (10⁻¹²), the h² scaling, the Richardson image, and the row closures (5 × 10⁻⁴ for θ_ii = 1, 10⁻⁸ for
θ_ii = 3/2). That is 2.8× the observed θ_ii = 1 defect, and far above the θ_ii = 3/2 one (10⁻¹⁵), against v2's 2 × 10⁻³. The solver is not changed, because results.json is the record and
the closure can be checked without changing it. The defect for a production code is listed as pitfall (p2) in the new §5 text. Replacement text:
R-6 and R-7.

**VER #6 / V-1: the 0911.1532 misprint. STANDS WITH CORRECTION; conceded.**
- The misprint is a dropped digit. "0.04439766" with its second "4" deleted is the printed "0.0439766" (string check in C2). It is not a
  transposition, so v2's diagnosis, inherited from REF-A, is withdrawn.
- I evaluated the value independently here, without REF-A's or VER's numbers. From the Rényi jammed-gap law
  G(g) = 2∫₀^∞ t e^{−gt−2Ein(t)} dt on 0 ≤ g ≤ 1, with mpmath at 30 digits: ∫G = ρ∞ and ∫(1 + g)G = 1 both to 10⁻²⁰, and
  ⟨g⟩ = 0.337617418, F_unc = Var g/(1 + ⟨g⟩)² = **0.0443976648**.
- The solver's 0.0443995 agrees with this to 1.8 × 10⁻⁶. C2 now compares against this independent value. v2's C2 compared against a typed
  target and included an arithmetic tautology; both are removed.
- One caveat, stated openly. The paper's "about 14%" (p.4), the gap to F_exact, fits the printed value (13.8%) better than the corrected one
  (13.0%). The misprint may therefore have entered before typesetting. The independent evaluation and the paper's own F_nnp sum still fix the
  value: 0.0443977 + 0.007685 = 0.05208, as printed on p.5 (Eq. (38) and l.390 of the extract), whereas the printed F_unc would give 0.05166.
- A second, separate misprint: see Rebuttal R1 (ρ∞).

Replacement text: R-5, R-8, L-EF1.

**VER #8 / V-12: the R&K cross-check. STANDS WITH CORRECTION; conceded.**
- The scatter attribution ("The scatter in data points is due to Monte-Carlo statistics") is in the Fig. 3 caption on **p.7**
  [FT 2004.10709, extract l.426–432]. The "constant at 2% level" sentence is on p.6.
- The fourth slope, from data/results.json rk_slopes, is ∂F/∂E_g = (0.112355 − 0.118321)/0.2 = **−0.0298** against Eq. (13)'s −0.028
  (+6.5%). So there are **four** slopes, not three.
- Maximum point deviations: −1.09% in ε and −2.38% in F, both at A = 3.
- C8 now re-evaluates the R&K planes from Eqs. (12)–(13). It tests all four slopes to 8% (observed ≤ 7.7%) and the points to 1.2% / 2.5%.
  The old tolerances were 10% and 3%.

Replacement text: R-9.

**VER #11 / V-13: k₂. STANDS WITH CORRECTION; conceded.**
- k₂(Si) = 2.3270(5.5947 × 0.063^{0.96403})^{0.23947} × 1.164^{0.05072} = **1.871 eV**, so "1.86" becomes "1.87".
- The exponent 1 − (3 + γ)β is 0.0507 with the stored fit coefficients. It is 0.0506 with the rounded (0.964, 0.2395). Both round to the
  text's 0.05.
- C25 now pins min 1.196, max 2.534, in-domain min 1.505 (GaSb), and Si 1.871.

Replacement text: R-10.

**VER #12 / V-4: the SiO₂ contradiction. STANDS WITH CORRECTION; conceded.** §2 is right: ab initio gives +7.8% against the model's +3.4%.
§5's "comparable for SiO₂" is replaced. The new C29 recomputes every pair. Ab initio does worse than the model for exactly {4H-SiC, SiO₂}, and
better for C, 3C-SiC, GaN and β-Ga₂O₃. Replacement text: R-13 (last bullet).

**VER #14 / V-7: the β-Ga₂O₃ ω₀ convention. STANDS WITH CORRECTION; conceded and quantified.**
- 784.92 cm⁻¹ = 97.32 meV is the zone-edge maximum along b₃ [FT 1902.02687 p.6].
- The same paper's Γ-point values are in Table I (p.8). The largest LO frequency there is 764.26 cm⁻¹ (mode 12, E ∥ c) = **94.76 meV**.
- With that Γ-point convention the model gives ε = 9.976 eV against 9.991 (−0.15%). The residual becomes +56.4% against +56.1% (C27).
- So the convention mix is flagged, and it is immaterial. The table keeps 97.3 meV so that it matches results.json.

Replacement text: R-11.

**VER #17 / V-3: the (EF12) ledger clause. STANDS WITH CORRECTION; conceded, with derivation.**
- By WP5-v4 (W4′) [l.177], ℋ_eff ≡ ω − N_ehE_g − E_st − E_esc, with N_eh ≡ N_e^f + N_X. A captured electron lowers N_e^f, and hence N_eh, by
  one. So ℋ_eff rises by **exactly E_g**, whatever the trap level is.
- WP7-E-v3 (E1-pr) [l.83] books the same E_g on the right-hand side of (W4′) in three parts:
  - (E_c − E_j) to ℋ (phonons emitted on capture to level E_j);
  - (E_j − μ_F) to E_trap^{pr};
  - (μ_F − E_v) to E_pairs^{unp} = (N_h^f − N_e^f)(μ_F − E_v).
- The three parts sum to E_c − E_v = E_g. The new C26 checks this in sympy for symbolic E_j and μ_F.
- v2's "ℋ_eff += Σ_captured E^tr_{e,j}" is withdrawn. Replacement text: R-12.

**VER #20 / V-6: the tag on §0 row 11. STANDS WITH CORRECTION; conceded.** The composite tag is restored. Replacement text: R-1.

**VER a.1 / V-9: the seed is not stated.** The full list of missing steps is S1–S3. S1 is the initial state and the ω ↔ x identification;
S2 is that N counts the seed pair; S3 is that the seed's hole is a terminal carrier with residual 0, which is what gives exactly two terminal
carriers per pair. Replacement text: R-2.

**VER a.2 / V-14: ⟨Σs_i⟩ is implicit.** It is written out in R-2, and matches cascade.py l.82 (`ss`).

**VER a.3 / V-14: the asymptote tag.** Rows 1 and 3 are re-tagged (R-1). The verifier treated §1.4 as having a single sketched step. It has
several, and **all of them** are now stated (A1–A5 in R-3). The tag stays [D, sketch]: A2 and A3 are cited, not proved here.

**VER a.4 / V-8: "the sibling effect".** Conceded. F^{ren} is the iid value, so F_eh − F^{ren} measures every departure from iid per-pair
costs. Replacement text: R-7 (bullet), IF-EF1 (ii′), and L-EF3 (consequential).

**VER §(4) (i)–(iv) / V-10: the §5 specification.** It is completed with what is computed, the approximation level, the method and
convergence criteria, the pitfalls, the n_gen = 1 sampling size and estimator, and the acceptance tests. Replacement text: R-13. The magnitude
in (ii) is rebutted (R3); the pitfall itself is accepted.

**L-EF1, L-EF2 and L-EF4 (VER §5) / V-1, V-5, V-11.** All conceded. L-EF1 additionally carries the ρ∞ correction (R1). See §3.

---
## 2. Replacement texts for GAP-EF-v2.md (complete; the merger uses these)

**R-1. §0, rows 1, 3, 5 and 11** (complete rows):

| # | Item | Result | Tag |
|---|---|---|---|
| 1 | Reduction of WP5 (W3) | Exact first and second moment recursions (EF3)–(EF4) of the energy-only cascade, solved by quadrature. Discretisation ≤ 0.05% (Si), 0.12% (C) (GAP-EF-v2-C5); asymptote stable to 10⁻⁴ (GAP-EF-v2-C6) | D (recursions) given (H-EF1)–(H-EF7); asymptote [D, sketch] + GAP-EF-v2-C6 |
| 3 | The uncomputed term | F_eh = 𝒱_< + 𝒱_> + 2𝒞_<> (EF7). Si: **0.091 + 0.288 − 0.265 = 0.114**; 2𝒞_<> computed by two routes (GAP-EF-v2-C4b). The dominant anticorrelation is between the residual heat ℋ_< and the above-threshold phonon heat ℋ_> along each carrier line; it cancels 92% of 𝒱_> | D (exact in the model, recursions); asymptote [D, sketch] + GAP-EF-v2-C6 |
| 5 | Limits | Rényi/RPP exactly (ρ∞ = 0.74759792, F = 0.0510387, GAP-EF-v2-C1); renewal value 0.0443995 against the independently evaluated F_unc = 0.04439766 (0911.1532 prints 0.0439766, a dropped digit; GAP-EF-v2-C2). Klein's 2.8E_g + rω₀ = identity (EF8) + threshold 3/2 E_g + uniform population; (K2) **overstates c₀ by 39% (θ_ii = 1) and 36% (θ_ii = 3/2)** (GAP-EF-v2-C11). R&K: F_∞ 0.1145 vs 0.115, **agreement at their ≈ 2% MC scatter**, plus five points and **four** slopes of their fitted planes, Eqs. (12)–(13) (GAP-EF-v2-C8) | D (limits); R&K CROSS-CHECKED |
| 11 | IF-E9 | (EF12) thinning **requires an energy-independent capture probability**; general law (EF12′) otherwise (GAP-EF-v2-C16, GAP-EF-v2-C16b); each captured electron raises ℋ_eff by exactly E_g (GAP-EF-v2-C26). (EF13) made consistent with WP5-v4 (W4′): **ℋ_eff unchanged, bare heat +N_XE_x^b, plus a variance term** (GAP-EF-v2-C21) | D (formulas); D, sketch (σ_cap); E (numbers) |

**R-2. §1.3: insert before *Step 1* (V-9), and replace *Step 2* (V-14):**

*Seed and the ω ↔ x identification.* The deposit ω creates one primary pair. The electron starts at kinetic energy x₀ = ω − E_g above the
conduction-band edge. The hole starts at the valence-band edge, x = 0 < θ_iiE_g, so it is terminal at once with residual 0. This is the
"one-sided pair seed" of §1.4 and §1.7(b); a symmetric seed shares x₀ between the two. The recursions below are for the subtree of one carrier
(t, x). On every path, x = N_sub E_g + ℋ_< + ℋ_>, with N_sub the number of ii events in the subtree (GAP-EF-v2-C3). **N counts the seed pair:**
N = 1 + N_sub(e, x₀). The heat ℋ includes the hole's zero residual. Therefore ω = E_g + x₀ = N E_g + ℋ, which is the ledger of (EF1). Every pair,
the seed included, ends with exactly one terminal electron and one terminal hole, which is the condition of (EF8) (solver: 2.000 carriers per
pair). ε_eh and F_eh are slopes in ω and do not depend on the seed; the offset b_N does (§1.4).

*Step 2 (factorisation).* Write Y = d_ii + Y₁ + Y₂ + Y₃ after an ii event. Independence of the subtrees gives E[Y_iY_j] = m_im_j for i ≠ j at
the drawn energies. Averaging over (H-EF3), with P_t ≡ ρ_tm_t and S_t ≡ ρ_ts_t, the single, square and pair sums are

  ⟨Y₁ + Y₂ + Y₃⟩ = [2P_t * ρ_t * ρ_t̄ + ρ_t * ρ_t * P_t̄](y)/𝔓_t(y),   ⟨Σs_i⟩ = [2S_t * ρ_t * ρ_t̄ + ρ_t * ρ_t * S_t̄](y)/𝔓_t(y),
  ⟨Σ_{i<j}m_im_j⟩ = [P_t * P_t * ρ_t̄ + 2P_t * ρ_t * P_t̄](y)/𝔓_t(y),   y = x − E_g.

(The code computes ⟨ΣY_i⟩ as `sm`, ⟨Σs_i⟩ as `ss` and the pair sum as `cr`, at cascade.py l.78–83.)

**R-3. §1.4: replace the first paragraph (V-14, a.3).** The tag is unchanged; all of the steps are now stated.

### 1.4 Asymptotic linearity [D, sketch]
For x ≫ E_g the solutions become n̄ = ω/ε_eh + b_N and Var N = F_ehω/ε_eh + O(1). The derivation needs five steps. A1, A4 and A5 are written out
here or in the code; A2 and A3 are cited (WP5 §6.4, (r1)–(r3)).
- **A1 (energy is harmonic).** Every vertex conserves energy (GAP-EF-v2-C3), so the function x ↦ x satisfies the homogeneous form of (EF3) with
  d_ii = E_g, d_ph = ω₀ and d_< = x. This fixes the normalisation: ε_eh = E_g + (heat per pair).
- **A2 (many-to-one, cited).** The first-moment equation for n̄ is a Markov renewal equation for one tagged line, the size-biased spine. The
  spine is a Markov chain on x with downward increments: phonon steps ω₀, or ii steps to a product chosen in proportion to its expected
  descendants.
- **A3 (key renewal theorem, cited).** Under (r1) finite mean increments, (r2) non-lattice increments and (r3) a finite second moment, the
  renewal density converges, so n̄(x) − x/ε_eh → b_N.
- **A4 (second moment).** The variance equation has the same kernel as the mean equation. Its source is 2⟨Σ_{i<j}m_im_j⟩ − (the square of the
  mean), minus the same expression at x − ω₀. By A3 applied to the mean, this source grows only linearly, so A3 applied again gives
  Var N = F_ehω/ε_eh + O(1).
- **A5 (lattice).** (r2) fails on the {E_g, ω₀} lattice. The remainder is then bounded and periodic, not convergent. A linear fit over
  [X/2, X] averages it out, and GAP-EF-v2-C6 bounds what is left at < 10⁻⁴ (X = 40 vs 80; fit windows [X/2, X] vs [3X/4, X]).

The bullets of v2 §1.4 (λ_ph > 5, scan.py at X = 25, b_N) follow unchanged.

**R-4. §1.5:** unchanged.

**R-5. §1.7(a): replace the last four sentences, from "(EF3)–(EF4) give coverage" (V-1; R1).**

(EF3)–(EF4) give coverage 1/ε = 0.747599 and F = 0.051040 after Richardson extrapolation. The exact values are Rényi's constant
ρ∞ = 0.74759792 (evaluated here with mpmath; 0911.1532 Eq. (23) p.4 prints 0.7475987, a misprint in the 7th digit) and F_exact = 0.0510387
[FT 0911.1532 Eq. (2) p.2]. The agreements are 1.3 × 10⁻⁶ and 1.6 × 10⁻⁶ (GAP-EF-v2-C1). The renewal estimate of the same limit is
F^{ren} = 0.0443995. The independent value is F_unc = Var g/(1 + ⟨g⟩)² = 0.04439766, from the exact jammed-gap law
G(g) = 2∫₀^∞ t e^{−gt−2Ein(t)} dt (GAP-EF-v2-C2, agreement 1.8 × 10⁻⁶). 0911.1532 prints F_unc = 0.0439766 (p.4). That is a **dropped-digit
misprint** of 0.04439766, as the paper's own F_nnp = F_unc + δF_nnp = 0.0443977 + 0.007685 = 0.05208 (p.5) requires; the printed value would
give 0.05166. The paper's "about 14%" (p.4) fits the printed value, so the slip may predate typesetting.

**R-6. §1.6 table, row 2** (complete row; V-2):

| case (a_DOS = ½ unless stated) | ε_eh/E_g | 𝒱_< | 𝒱_> | 2𝒞_<> | F_eh | F^{ren} (EF6′) | F^{ren}/F_eh | r̄_c/E_g |
|---|---|---|---|---|---|---|---|---|
| λ_ph → 0, θ_ii = 1 | 1.5853 | 0.0811ᵃ | 0ᵃ | 0ᵃ | **0.0811** | 0.0566 | 0.70 | 0.293ᵃ |

ᵃ In the model, ℋ_> ≡ 0 without phonons, so 𝒱_> = 2𝒞_<> = 0 exactly and 𝒱_< = F_eh. The solver's raw Richardson entries (0.0813, −6 × 10⁻⁶,
−1.5 × 10⁻⁴) and r̄_c = 0.29272 contain the O(h²) threshold artefact described below. Without it, r̄_c = 0.29263–0.29265.

**R-7. §1.6: replace the paragraph below the table, and bullet 3 (V-2, V-8).**

The first three rows are Richardson-extrapolated on one grid pair (h = 0.01, 0.005) in **every** column. (v1 mixed an extrapolated ε with an
unextrapolated r̄_c; REF-B 2.1.) r̄_c is the mean terminal residual per carrier.

On each grid the identity (EF8) holds to 10⁻¹⁵, provided one artefact is booked. At λ_ph = 0 and θ_ii = 1, the grid point x = E_g has
𝔓_t(0) = 0, so p_t = 0, and cascade.py l.74 moves the carrier one step h down the phonon branch although phonon=False. N does not change, but h
moves from ℋ_< to ℋ_> with probability O(h). The spurious ⟨ℋ_>⟩ is therefore O(h²) per carrier: 1.80 × 10⁻⁴ and 4.50 × 10⁻⁵ at h = 0.01 and
0.005 (GAP-EF-v2-C23). Linear Richardson extrapolation maps ch² to −ch²/2, so the extrapolated θ_ii = 1 row closes ε/E_g = 1 + 2r̄_c only to
**1.8 × 10⁻⁴** (4.5 × 10⁻⁵ on the pair 0.005/0.0025). The θ_ii = 3/2 row, whose threshold grid point has 𝔓 > 0, closes to 10⁻¹⁵.
GAP-EF-v2-C23 tests both to 5 × 10⁻⁴ and 10⁻⁸. ε_eh and F_eh are unaffected. "ℋ_> = 0 up to an O(h²) threshold artefact."

- **Correlations beyond iid per-pair costs raise F.**
  - Without phonons ℋ_> ≡ 0, so 𝒞_<> vanishes trivially. It does not measure sibling correlations (v1's wording was wrong, REF-A a.3).
  - F^{ren} (EF6′) is the iid renewal value. The gap F_eh − F^{ren} = +0.025 at θ_ii = 1 and +0.013 at 3/2 is **positive**, and it measures
    every departure from iid per-pair costs together:
    - correlations between siblings;
    - correlations between the electron and the hole of one pair;
    - correlations between more distant carriers;
    - the non-identical per-pair laws.
  - The gap does not isolate any one of these, so "sibling correlations raise F" is an interpretation [C]. 0911.1532 makes the same qualitative
    point for RPP [FT p.8]: "the correlation correction to F is positive", and division correlations "are not the only … correlation
    corrections".
  - The no-phonon value F_eh = 0.081 is pure partition noise: the exact jamming distribution of residuals, strongly peaked at x → 0 as in Rényi
    parking.

**R-8. §1.7(b):** unchanged. Its r̄_c comparisons (+105%, +70%, −16%) hold with the artefact-free r̄_c (0.6/0.29265 − 1 = +105.0%).

**R-9. §1.7(c): replace from "R&K state that" to the end of (c) (V-12).**

R&K state that their F is "constant at 2% level" across scans [FT 2004.10709 p.6]. They attribute the point scatter to "Monte-Carlo
statistics" in the Fig. 3 caption [FT p.7]. So **the agreement is at their ≈ 2% scatter**, not at 0.5%. The stronger cross-check is against
R&K's own fitted planes, Eq. (12) ε = 1.7E_g + 0.084A + 1.3 and Eq. (13) F = −0.028E_g + 0.0015A + 0.14 (p.6), over A ∈ {3, 5.2, 7} and
E_g ∈ {1.0, 1.124, 1.2} (GAP-EF-v2-C8):

| quantity | solver | R&K Eqs. (12)–(13) |
|---|---|---|
| ε at (A, E_g) = (3, 1.124) / (5.2, 1.124) / (7, 1.124) | 3.425 / 3.651 / 3.787 eV | 3.463 / 3.648 / 3.799 eV |
| F at the same points | 0.1103 / 0.1145 / 0.1168 | 0.1130 / 0.1163 / 0.1190 |
| ∂ε/∂A (secant over A ∈ [3, 7]) | 0.090 | 0.084 |
| ∂F/∂A (secant) | 0.0016 | 0.0015 |
| ∂ε/∂E_g (secant over E_g ∈ [1.0, 1.2]) | 1.69 | 1.7 |
| ∂F/∂E_g (secant over E_g ∈ [1.0, 1.2]) | −0.030 | −0.028 |

All five points agree to ≤ 1.1% in ε and ≤ 2.4% in F; the largest deviations of both are at A = 3. All four slopes agree to ≤ 7.7%. This is an
independent route (event sampling against deterministic quadrature), so the solver is CROSS-CHECKED, at ≈ 2%.

**R-10. §1.8, the k₂ sentence (V-13):** "… and 1.5–2.5 eV over the rows inside the fit domain (GAP-EF-v2-C25); it is **1.87 eV** at
ω₀ = 63 meV and E_g = 1.164 eV." In the line before (EF11), the exponent reads "E_g^{1−(3+γ)β} = E_g^{0.051}". With the stored coefficients
this is 0.0507; with the rounded (0.964, 0.2395) it is 0.0506.

**R-11. §2 table, β-Ga₂O₃ row** (complete row; V-7):

| Material | E_g, ω₀ (eV) [source] | ε_eh measured (eV) [source] | model V0 (V1, V3) | resid. | F measured | F model V0 |
|---|---|---|---|---|---|---|
| β-Ga₂O₃ (extended) | 4.8 [FT 2311.05011 p.1] (4.5 [FT 1902.02687 p.1]), 0.0973: **zone-edge maximum** along b₃ (DFPT-LDA) [FT 1902.02687 p.6]; other rows use ω_LO/ω_O,max at Γ. The Γ-point maximum LO, 764.26 cm⁻¹ = 0.0948 [FT 1902.02687 Table I p.8], gives model 9.976 eV and residual +56.4% (GAP-EF-v2-C27) | 15.6, EBIC + MC "experimental estimation" [FT 2311.05011 p.5] | 9.99 (10.40, 10.76) | +56.1% | — | 0.087 |

**R-12. §4.1, (EF12)** (complete display and the sentence after it; V-3):

  ε_eh^{(W4)} = ε^{cas}/(1 − f_cap^e),   F_eh′ = (1 − f_cap^e)F_eh + f_cap^e   (GAP-EF-v2-C16).                                              (EF12)

*Ledger.* With E_st = E_esc = 0, WP5-v4 (W4′) gives ℋ_eff ≡ ω − N_ehE_g, with N_eh ≡ N_e^f + N_X. Each captured electron lowers N_eh by one, so
**ℋ_eff rises by exactly E_g per captured electron**, whatever the level E_j is. WP7-E-v3 (E1-pr) splits that E_g into three parts:
(E_c − E_j) goes to ℋ, (E_j − μ_F) to E_trap^{pr}, and (μ_F − E_v) to E_pairs^{unp} (GAP-EF-v2-C26). Hence ⟨ℋ_eff⟩ = ⟨ℋ_eff⟩_{f=0} + f_cap^e⟨N_ii⟩E_g.
This is the same logic that fixes (EF13).

The rest of §4.1 is unchanged, from "(H-cap) is a real restriction" onwards.

**R-13. §5: replace the bullets "Kernels", "Statistics for F" and "Expected accuracy" by the following (V-10, V-4).** "Per material" and
"Recommendation" are unchanged.
- **What is computed.** For each material: ε_eh and F_eh as the asymptotic slopes of n̄(ω) and Var N(ω) (§1.4); the decomposition (EF7); and
  the cascade-end distribution (r̄_c, σ_res per type) for §4.3. The method is (EF3)–(EF4), with the reduced kernels replaced by iso-energy
  averages of full-band kernels:
  - the ii kernel 𝒦̄_t(x → x₁, x₂, x₃) from (W1′), using G0W0 bands and the BerkeleyGW full-frequency ε⁻¹(p, ω) with local fields;
  - phonon emission and absorption rates per branch ν, from EPW (W2) with WP5-cp1–cp3, with n_B(ω_ν, T) kept, which removes (H-EF6);
  - an explicit plasmon channel, so that its effect on F, UNRESOLVED under (H-EF7), is measured.

  Above ≈ 15 eV, match to free-electron states with GW lifetimes. Hole bands and B_h come from the band structure.
- **Approximation level.** G0W0 quasiparticles (θ_GW); RPA screening with LFE; DFPT-level g; energy-only reduction (H-EF1) for generations
  n_gen ≥ 2 (θ_{R-k}); independent subtrees (B2) (θ_dense).
- **Method and convergence.** A deterministic upward sweep on an energy grid of bin h, with the kernels tabulated on the same grid. Every one of
  the following criteria must pass, or the grid is refined:
  - (c1) *bin halving* h → h/2, starting from ≤ 10 meV: |Δε|/ε < 10⁻³ and |ΔF|/F < 3 × 10⁻³. This solver achieves 4 × 10⁻⁴ and 5 × 10⁻⁴ in
    Si (GAP-EF-v2-C5). Report the Richardson value with the (h, h/2) difference as its error.
  - (c2) *energy cap* X_cap → 1.5X_cap (≈ 100 → 150 eV), including the free-electron matching point 15 → 20 eV: |Δε|/ε and |ΔF|/F < 10⁻³.
  - (c3) *asymptote*: X → 2X, and fit windows [X/2, X] against [3X/4, X], must agree to < 10⁻⁴ (GAP-EF-v2-C6). Use X ≥ 60E_g wherever the
    phonon-to-ii ratio near threshold is that of λ_ph > 5.
  - (c4) *k-mesh* of the iso-energy averages: two meshes, with the change in 𝒦̄ propagated to |Δε|/ε, |ΔF|/F < 10⁻³.
  - (c5) *internal identities*: energy conservation per path < 10⁻¹² (GAP-EF-v2-C3); N route = heat route < 10⁻⁹ (GAP-EF-v2-C4a);
    𝒱_< + 𝒱_> + 2𝒞_<> = F_eh by two routes < 10⁻⁹ (GAP-EF-v2-C4b).
- **The k-resolved first generation (n_gen = 1).** The primary and its first ii products keep their k-resolution, because the error of (H-EF1)
  is largest there.
  - *Sampling.* Draw N_s first-step final states (k₁, k₂, k₃) from the full-band 𝒦, importance-sampled on Im ε⁻¹.
  - *Conditional moments.* For each draw i, evaluate the subtree mean M_i and variance V_i exactly from the iso-energy tables.
  - *Estimator* (law of total variance): n̄ = 1 + mean_i M_i, and Var N = mean_i V_i + var_i M_i.
  - *Error.* Batch means over 20 batches.
  - *Size.* For a near-Gaussian M, the relative error of var_i M_i is √(2/N_s). Since var_i M_i ≤ Var N, the bound is N_s ≤ 2/δ_F², i.e.
    8 × 10⁴ for δ_F = 0.5% [E]. Start at N_s = 10⁴ and double until the batch error satisfies SE(F)/F < 0.5% and SE(ε)/ε < 0.1%.
  - *Pure event sampling* (no tables) instead needs N_ev ≈ 2/δ² events in total, i.e. 2 × 10⁴ events of ≥ 1 keV for 1% on F.
- **Pitfalls.**
  - (p1) *ω₀ on the grid.* Each phonon step must be an integer number of bins to < 1%, the rule that model.grid enforces. The options are a bin
    commensurate with the dominant branch, h = ω_ν/n_ν, or a linearly interpolated step m(x − ω_ν) for the other branches, whose O(h²) error
    must pass (c1). Fixed 10 meV bins would put PbTe (13.5 meV) 26% and PbSe (17.1 meV) 17% off grid (GAP-EF-v2-C28). An off-grid step of this
    kind is v1's CsI bug.
  - (p2) *Threshold point.* Where the ii phase space vanishes at E_th and no phonon channel is open, the carrier must terminate. It must not take
    a phonon step: that is the O(h²) artefact of GAP-EF-v2-C23.
  - (p3) *Plasmon double count.* Within RPA the plasmon is part of Im ε⁻¹. An explicit plasmon channel must be removed from the ii kernel
    (CONVENTIONS §13 row 21).
  - (p4) *Lattice.* The increments {E_g, ω_ν} break (r2). Fit slopes over [X/2, X]; never use a single-point ratio.
  - (p5) *Seed dependence.* Report slopes. b_N depends on the seed.
  - (p6) *Gap temperature.* Use E_g at the temperature of the measurement.
  - (p7) *Cancellation.* F is a small difference of large terms (§1.6). Report 𝒱_<, 𝒱_> and 2𝒞_<> with (c5).
- **Acceptance tests (before full kernels are switched on).** With its kernels replaced by those of (H-EF3)–(H-EF4), the full-band code must
  reproduce:
  - (a1) L-EF1: ρ∞ = 0.74759792, F = 0.0510387 and F_unc = 0.04439766, to 10⁻⁵;
  - (a2) L-EF4, against this solver: ε = 3.651 eV and F = 0.1145 at (A, E_g, ω₀, B_h) = (5.2 eV³, 1.124 eV, 63 meV, 12 eV), to 10⁻³ relative.
    Against R&K's Eqs. (12)–(13) only ≈ 2% is expected;
  - (a3) the λ_ph → 0 rows, c₀ = 1.5853 (θ_ii = 1) and 2.0562 (θ_ii = 3/2), to 10⁻⁴;
  - (a4) the Si calibration point, ε = 3.749 eV at 𝒜_ph = 5.595 eV³.
- **Expected accuracy.** The DFT/TDDFT full-band MC residuals (meas/calc − 1) are:
  - +16% (Si), +0.6% (C), +7.3% (4H-SiC), +4.5% (3C-SiC), +7.8% (SiO₂);
  - +7.8% (GaN against EBIC) and +39% (β-Ga₂O₃ against the EBIC + MC estimate).

  Sources: [FT 2610.16949 Table II p.8; FT 2311.05011 p.5; FT 2308.03893 pp.18–19]. (v1's "0% (GaN)" compared the calculation with a number it
  may share an origin with, and is deleted.) The ab initio route is clearly better than the one-𝒜 model for C, 3C-SiC, GaN and β-Ga₂O₃, and
  **worse for 4H-SiC (+7.3% against +3.5%) and SiO₂ (+7.8% against +3.4%)**, as in §2 (GAP-EF-v2-C29).

**R-14. §7: check rows that change.** The header becomes "(code/GAP-EF-v2/checks.py, 32/32 PASS, ≈ 18 s)".

| Check | Content |
|---|---|
| GAP-EF-v2-C1 | RPP limit: 1/ε → Rényi ρ∞ = 0.74759792 (mpmath here; the paper prints 0.7475987) to 3 × 10⁻⁶, F → 0.0510387 to 5 × 10⁻⁶ (v2: 3 × 10⁻⁴, 10⁻⁴) |
| GAP-EF-v2-C2 | renewal F_unc against the **independent** mpmath value 0.04439766 to 5 × 10⁻⁶; printed 0.0439766 = dropped digit (string test); F_nnp = 0.05208 needs the corrected value, not the printed one (v2's typed target and tautology removed) |
| GAP-EF-v2-C5 | grid doubling: Si ε 6 × 10⁻⁴, F 10⁻³; C ε 1.5 × 10⁻³ (v2: 10⁻³, 2 × 10⁻³, 2 × 10⁻³) |
| GAP-EF-v2-C8 | R&K F_∞ within 2%; planes re-evaluated from Eqs. (12)–(13); five points ≤ 1.2% / 2.5%; **four** slopes within 8% (v2: three, 10%) |
| GAP-EF-v2-C10 | renewal F = σ²/ε² against the explicit constrained recursion to 10⁻³ (v2: 2%) |
| GAP-EF-v2-C13 | statistics recomputed from the §2 measured values (typed) and checked against the text-quoted numbers −6.5/24.6/8.2/12.3, 5.5/8.7/13.9, 14.2/23.0/56.1, 63.4/178.8% (v2 compared json with json) |
| GAP-EF-v2-C15 | (EF11) 1.695 and FD 1.777 as quoted, ±0.005 (v2: agreement within 10%) |
| GAP-EF-v2-C23 | (EF8) exact per grid with the threshold artefact booked (10⁻¹²); artefact O(h²) (ratio 3.8–4.2); Richardson image −ch²/2 (sympy); rows 5 × 10⁻⁴ (θ_ii = 1), 10⁻⁸ (θ_ii = 3/2) (v2: 2 × 10⁻³) |
| GAP-EF-v2-C25 | k₂ ∈ [1.196, 2.534] eV, in-domain minimum 1.505, k₂(Si) = 1.871 (v2: loose range only) |
| GAP-EF-v2-C26 (new) | (EF12) ledger: ℋ_eff rises by exactly E_g per captured electron; the H / E_trap^{pr} / E_pairs^{unp} split sums to E_g (sympy) |
| GAP-EF-v2-C27 (new) | β-Ga₂O₃ with ω₀ = Γ-point LO maximum 94.76 meV: Δε < 0.3%, residual change < 0.5 points |
| GAP-EF-v2-C28 (new) | 10 meV bins: maximum off-grid fraction on [10, 20] meV = 1/3 (sympy); worst survivors PbTe 26%, PbSe 17%; CsI, NaI on the grid |
| GAP-EF-v2-C29 (new) | ab initio vs model residuals: ab initio worse exactly for {4H-SiC, SiO₂} |

**R-15. Closing table of GAP-EF-v2, rows A-K9 and B-2.1 (λ → 0)** (complete rows):

| Item | Type | Resolution | Location |
|---|---|---|---|
| A-K9 | W | GAP-EF-v2-C2 targets the independently evaluated F_unc = 0.04439766. 0911.1532's 0.0439766 is a **dropped-digit** misprint (not a transposition; VER #6). Agreement 1.8 × 10⁻⁶ | §1.7(a), GAP-EF-v2-C2; errata R-5 |
| B-2.1 (λ → 0 row) | W | Whole row on one grid pair (Richardson in every column). (EF8) is exact per grid; the Richardson row closes to 1.8 × 10⁻⁴ (θ_ii = 1, an O(h²) threshold artefact) and 10⁻¹⁵ (θ_ii = 3/2) (GAP-EF-v2-C23) | §1.6; errata R-6, R-7 |

**Symbols.** One new local symbol, S_t ≡ ρ_ts_t (§1.3, the second-moment analogue of P_t). It is local to §1 and goes to IF-EF5. Nothing else
is new.

---
## 3. Owed corrections of GAP-EF-v2 (Interface flags and proposed LIMITS rows), re-issued

| # | Status | Complete text (re-issued) or note |
|---|---|---|
| **IF-EF1** | **re-issued (V-8)** | Owner: WP5 (v4 §6.4(ii)–(iii); WP5v3-C4b). **(ii)** 54/175 ≈ 0.31 is the variance with N held fixed. With the energy constraint, the same independent-residual model gives 27/686 = 0.0394, **3× below** the data, not down to it. The direction of WP5-v4's sentence is therefore wrong, not only its number: the omitted correlations must *raise* F. **(ii′)** The leading anticorrelation is between ℋ_< and ℋ_> along each carrier line (2𝒞_<> = −0.265 against 𝒱_> = 0.288 in Si), not between sibling residuals. **Correlations beyond iid per-pair costs** (sibling, e–h within a pair, longer-range, non-identical per-pair laws) raise F: F_eh − F^{ren} = +0.025 (θ_ii = 1) and +0.013 (θ_ii = 3/2) at λ_ph → 0. **(iii)** Phonon shot noise is not the leading term either: 𝒱_> is 7× Poisson. Replace (ii)–(iii) by (EF6), (EF6′), (EF7) with the §1.6 table (errata R-6 for row 2). Action **S**: rewrite §6.4(ii)–(iii); relabel WP5v3-C4b "N fixed"; L23 note |
| IF-EF2 | unchanged | — |
| IF-EF3 | unchanged | The §3 table is not affected by the errata |
| **IF-EF4** | **re-issued (V-3)** | Owner: WP7-E (IF-E9). (EF12) holds only under (H-cap); otherwise use (EF12′). In both, **each captured electron raises ℋ_eff by exactly E_g**, split among ℋ, E_trap^{pr} and E_pairs^{unp} (errata R-12, GAP-EF-v2-C26). (EF13) is in the (W4′)-consistent form; §4.3 spec. Action: close IF-E9 at the formula level; numbers stay open (GE-4) |
| IF-EF5 | unchanged, plus one row | Add S_t ≡ ρ_ts_t (local to §1) |
| IF-EF6 | unchanged | k₂ range unchanged; the Si value 1.87 eV is not in the flag |
| IF-EF7 | unchanged | — |

**Proposed LIMITS rows** (return-local labels; the coordinator assigns numbers):

| # | Status | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|---|
| **L-EF1** | **re-issued (V-1; R1)** | (W3) → (H-EF1)–(H-EF4) → (EF3)–(EF4) with a_DOS = 0, δ hole DOS, θ_ii = 1, no phonons: Rényi parking, ρ∞ = 0.74759792, F = 0.0510387; renewal value F_unc = 0.04439766 | 0911.1532 Eqs. (2), (23) [FT]. Eq. (23) prints ρ∞ = 0.7475987 (7th-digit misprint) and p.4 prints F_unc = 0.0439766 (dropped-digit misprint); both corrected by independent evaluation (GAP-EF-v2-C1, GAP-EF-v2-C2) | narrow valence band, constant conduction DOS, θ_ii = 1, no phonons | parabolic DOS, phonons | DERIVED (GAP-EF-v2-C1, GAP-EF-v2-C2) |
| **L-EF2** | **re-issued (V-11)** | (EF8) + (K1) θ_ii = 3/2 + (K2) uniform-in-k population → Klein ε = (14/5)E_g + rω₀ | 2610.16949 p.2; 1602.08005 Eq. (3) [FT] | θ_ii = 3/2; uniform-in-k terminal population; λ_ph → 0 for c₀; (K2) attribution to Klein UNRESOLVED | exact jamming population (EF3): (K2) overstates c₀ by 39% (θ_ii = 1) / 36% (θ_ii = 3/2) at λ_ph → 0 (GAP-EF-v2-C11) | DERIVED (truncation) |
| **L-EF3** | **re-issued, consequential to V-8** (VER: STANDS) | (EF6) with (R-iid): renewal (final-state) F^{ren} = σ_pair²/ε_eh² | 0911.1532 Eq. (7), p.2 "lower-bound estimate" [FT] | iid per-pair costs | correlations beyond iid per-pair costs (sibling, e–h, longer-range, non-identical laws), computed via (EF7): F^{ren}/F_eh ∈ [0.12, 0.87] in all computed cases | DERIVED (GAP-EF-v2-C10); lower bound in all computed cases (GAP-EF-v2-C19), not proven in general [C] |
| **L-EF4** | **re-issued (V-5)** | (EF3)–(EF4) with a_DOS = ½, θ_ii = 1, B_h, one 𝒜_ph, against R&K's random-k model: F_∞ = 0.1145 (Si, 300 K, E_g = 1.124 eV); ε and F **agree with R&K Eqs. (12)–(13) to ≤ 1.1% (ε), ≤ 2.4% (F)** at five points, four slopes ≤ 7.7%. R&K's model has a P(E, E_r) first split, a hole re-split for E_h > W and plasmons [FT 2004.10709 p.6 steps 1–4], none of which are in (H-EF3)–(H-EF7) | 2004.10709 Eq. (8) p.3, Eqs. (12)–(13) and F_∞ = 0.115 p.6, MC-scatter attribution Fig. 3 caption p.7 [FT] | universal 𝒜_ph; plasmon channel effect on F UNRESOLVED | per-material 𝒜_ph (C +14%, GaN +25%) | **CROSS-CHECKED** at ≈ 2% (GAP-EF-v2-C8); not DERIVED: two different models agree numerically |
| L-EF5 | unchanged | — | — | — | — | — |
| L23 ✎ | unchanged | — | — | — | — | — |

---
## 4. Rebuttals

**R1. VER §5 row L-EF1: "Eq. (23) 'ρ∞ = 0.7475987' (p.4) CONFIRMED", reported together with its own (V1) value 0.7475979.** The verifier
confirmed that the paper prints 0.7475987, which is true (extract l.277, p.4). It did not reconcile that number with its own evaluation, and
L-EF1 and GAP-EF-v2-C1 kept the printed value as the exact one. **The printed value is not the exact value.**
- Rényi's constant is ρ∞ = ∫₀^∞ exp[−2Ein(t)] dt with Ein(t) = γ + ln t + E₁(t). Evaluated with mpmath at 30 digits it is
  **0.74759792025341143518**, and the gap law reproduces it two ways: ∫₀¹G = ρ∞, and coverage ∫₀¹(1 + g)G = 1 to 10⁻²⁰ (GAP-EF-v2-C1).
- Eq. (23) therefore carries a second misprint, in its 7th digit: 0.7475987 against 0.7475979, a difference of 8 × 10⁻⁷.
- This does not affect any v2 conclusion. The solver's 0.7475992 is 1.3 × 10⁻⁶ from the true value, and v2's C1 tolerance was 3 × 10⁻⁴.
- It does change L-EF1's source cell and C1's target (§3, R-14).
- F_exact = 0.0510387 (Eq. (2)) is **not** independently re-evaluated here. It is cited as printed; the solver agrees to 1.6 × 10⁻⁶.

**R2. VER #5 and V-2: "an O(h) grid artefact".** The mechanism (cascade.py l.74) is right; the order is wrong.
- The artefact is a step of size h taken with probability O(h): only carriers landing exactly on the grid point x = E_g take it. Its mean is
  therefore **O(h²)**: ⟨ℋ_>⟩/carrier = 1.80 × 10⁻⁴, 4.50 × 10⁻⁵ and 1.13 × 10⁻⁵ at h = 0.01, 0.005 and 0.0025, ratio 4.00. Its variance is
  O(h³), ratio ≈ 8.
- The order matters for the verifier's own diagnosis. Richardson extrapolation for an O(h) scheme, 2f(h/2) − f(h), would cancel an O(h)
  artefact exactly. It maps an O(h²) artefact ch² to −ch²/2 (sympy, GAP-EF-v2-C23). That is the observed −8.98 × 10⁻⁵ ≈ −½ × 1.80 × 10⁻⁴.
- This sign flip is what produces the "negative variance" and the 1.8 × 10⁻⁴ defect. An O(h) artefact would leave neither after
  extrapolation.
- Corrected wording: "an O(h²) threshold artefact", which is the wording used in R-6, R-7 and R-13 (p2).
- A minor point: C23's 2 × 10⁻³ is **20×**, not 10×, the text's 10⁻⁴.

**R3. VER §(4)(ii): "with 10 meV bins, ω₀ = 10–20 meV (CsI, NaI, PbTe) is off-grid by up to 50%".** The pitfall is real and is adopted as (p1).
The number and the examples are wrong.
- For ω on [10, 20] meV, the off-grid fraction |10·round(ω/10) − ω|/ω equals (ω − 10)/ω on [10, 15] and (20 − ω)/ω on [15, 20]. Its maximum is
  **1/3**, at ω = 15 meV (sympy, GAP-EF-v2-C28), not 1/2.
- 50% occurs only below 10 meV, for example at ω = 6.7 meV.
- For the named rows (ω₀ from data/results.json, i.e. the WP8-U inputs): CsI 10.0 meV is 0% off, NaI 20.0 meV is 0%, and PbTe 13.5 meV is
  26%.
- The worst survivors are PbTe (26%) and PbSe (17.1 meV, 17%).
- v1's CsI bug was not a 10 meV-bin effect. It was the per-E_g grid of model.grid running below its tolerance (n_w/N = 2.04w; REF-B 2.7).

**No other VER claim is contested.**
- Items 6, 8, 11, 12, 14, 17 and 20 and notes a.1–a.4 are conceded above, each with the derivation or the source that decides it.
- In item 17 the sympy check (C26) confirms the verifier's ledger argument.
- In item 11 the verifier's 0.0507 is the unrounded exponent and is right.

---
## 5. Changes to code/GAP-EF-v2/checks.py (32/32 PASS, ≈ 18 s; solver and data unchanged)
- **Circular checks removed.** C2's typed target 0.0443977 and its arithmetic identity are replaced by the independent mpmath F_unc. C13's
  json-against-json comparison is replaced by statistics computed from the typed §2 measurements and compared with the numbers quoted in the
  text.
- **Tolerances tightened** to just above the quoted values:
  - C1: 3 × 10⁻⁴ → 3 × 10⁻⁶ (ρ∞) and 10⁻⁴ → 5 × 10⁻⁶ (F);
  - C2: 10⁻⁵ → 5 × 10⁻⁶;
  - C5: to 6 × 10⁻⁴ / 10⁻³ / 1.5 × 10⁻³;
  - C8: slopes 10% → 8%, points F 3% → 2.5%;
  - C10: 2% → 10⁻³;
  - C15: from "within 10%" to the quoted values ±0.005;
  - C23: 2 × 10⁻³ → 5 × 10⁻⁴ and 10⁻⁸;
  - C25: ranges pinned to ±0.005.
- **Checks added for each correction:**
  - V-1: C2 (dropped digit);
  - R1: C1 (ρ∞);
  - V-2 and R2: C23 (per-grid exactness, h² scaling, Richardson image);
  - V-3: C26;
  - V-4: C29;
  - V-7: C27;
  - V-12: C8 (∂F/∂E_g);
  - V-13: C25 (k₂(Si));
  - R3: C28.
- C11's λ → 0 cascades now also carry the R, P and C deposits, which C23 reuses, so no extra solver runs are needed.

---
## 6. Closing table: verifier item → resolution → location
| VER item | Verdict | Resolution | Location |
|---|---|---|---|
| #1 IF-EF1 numbers | STANDS | no action; wording per a.4 | §3 IF-EF1 |
| #2 F^{ren} lower bound | STANDS | no action | — |
| #3 (EF6′) | STANDS | no action | — |
| #4 (K2) percentages | STANDS | no action; percentages unchanged with artefact-free r̄_c | R-8 |
| #5 λ → 0 closure | STANDS WITH CORRECTION | conceded (1.8 × 10⁻⁴; artefact); order corrected to O(h²) | §1, R-6, R-7, R-15, C23; Rebuttal R2 |
| #6 0911.1532 F_unc | STANDS WITH CORRECTION | dropped digit; independent mpmath value; second misprint (ρ∞) found | §1, R-1, R-5, R-15, L-EF1, C1, C2; Rebuttal R1 |
| #7 eV³ | STANDS | no action | — |
| #8 R&K cross-check | STANDS WITH CORRECTION | p.7 locator; four slopes (∂F/∂E_g = −0.030) | R-1, R-9, L-EF4, C8 |
| #9 plasmon UNRESOLVED | STANDS | no action | — |
| #10 F_Si | STANDS | no action | — |
| #11 k₂ | STANDS WITH CORRECTION | 1.87 eV; exponent 0.0507 | R-10, C25 |
| #12 validation / SiO₂ | STANDS WITH CORRECTION | §5 made consistent with §2 | R-13, C13, C29 |
| #13 ab initio residuals | STANDS | no action | — |
| #14 β-Ga₂O₃ ω₀ | STANDS WITH CORRECTION | zone-edge flag; Γ-LO alternative quantified (+56.4%) | R-11, C27 |
| #15 4H-SiC floor | STANDS | no action | — |
| #16 CsI grid fix | STANDS | no action | — |
| #17 (EF12) ledger | STANDS WITH CORRECTION | ℋ_eff += E_g per capture; split derived | R-1, R-12, IF-EF4, C26 |
| #18 (EF13) | STANDS | no action | — |
| #19 (EF9)–(EF11) | STANDS | no action (C15 pinned to the quoted values) | C15 |
| #20 §0 row 11 tag | STANDS WITH CORRECTION | composite tag restored | R-1 |
| #21 Klein attribution | STANDS | no action | — |
| a.1 seed | W | stated (S1–S3) | R-2 |
| a.2 ⟨Σs_i⟩ | N | written | R-2 |
| a.3 asymptote tag | N | rows 1, 3 re-tagged; all steps A1–A5 stated | R-1, R-3 |
| a.4 "sibling effect" | W | "correlations beyond iid per-pair costs" | R-7, IF-EF1, L-EF3 |
| (4)(i) convergence | W | (c1)–(c5) | R-13 |
| (4)(ii) ω₀-on-grid | W | (p1) adopted; magnitude rebutted | R-13, C28; Rebuttal R3 |
| (4)(iii) n_gen = 1 | W | estimator, N_s, batch errors | R-13 |
| (4)(iv) acceptance | W | (a1)–(a4) | R-13 |
| L-EF1 | STANDS WITH CORRECTION | dropped digit + ρ∞ misprint | §3 |
| L-EF2 | STANDS WITH CORRECTION | Validity / Leading correction swapped | §3 |
| L-EF3 | STANDS | re-issued only for the a.4 phrase | §3 |
| L-EF4 | STANDS WITH CORRECTION | "agree to ≤ 1.1% / ≤ 2.4%"; CROSS-CHECKED | §3 |
| L-EF5, L23 ✎ | STANDS | unchanged | §3 |
| V-1 … V-14 | — | V-1 R-5/R-15/L-EF1; V-2 R-6/R-7/C23; V-3 R-12/C26; V-4 R-13; V-5 L-EF4; V-6 R-1; V-7 R-11/C27; V-8 R-7/IF-EF1; V-9 R-2; V-10 R-13; V-11 L-EF2; V-12 R-9/C8; V-13 R-10/C25; V-14 R-1/R-2/R-3 | as listed |
| checks (brief item 4) | — | circular checks removed, tolerances tightened, C26–C29 added; 32/32 PASS ≈ 18 s | §5, code/GAP-EF-v2/checks.py |
