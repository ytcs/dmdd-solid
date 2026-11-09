# R17 / ERR-WP8: final corrections to the WP8 chain (WP8-U-v3, WP8-F-v3, table v4, CW7-errata, WP8-S-v2)

Agent ERR-WP8, brief briefs/R17/ERR-WP8.md. Read with returns/R16/WP8-U-v3.md, WP8-F-v3.md, WP8-U-table-v4.csv, CW7-errata.md and WP8-S-v2.md; none of them is
edited. This file applies **referees/R17/VER-ERR-CW7.md** (RC1–RC10 and every non-STANDS row) and **referees/R16/VER-WP8-S-v2.md** (every non-STANDS row), plus
three coordinator inputs received during the pass: (a) the CW8-LIT supersessions in state/DATA-ADDENDA.csv (Al and Ir C_ij, YIG a), (b) CONVENTIONS §13 row 38
(the S2 array rule), (c) a next-target guide over the full pool. Closing table: §19.
**Deliverables.** This file; code/CW7/cascade_gf.py (commensurate-grid guard; BLAS speed-up of `moments_fast`, same arithmetic) and code/CW7/checks.py
(C5, C5b, C7, C8 on the commensurate grid; new C5c) — **41/41 PASS, 19 s**; code/REV-WP8-S/rank.py (v3) → **data/ranking_v3.json** (+ rank_stdout_v3.txt), with
data/ranking_v2.json and code/CW7/data/ranking.json byte-unchanged (md5 in S2-C15); code/REV-WP8-S/checks.py — **31/31 PASS, 4.5 s** (S2-C1…C15 updated, S3-C1…C16 new).
Nothing committed.
**Numerics.** One MC of 20 000 draws per input, run at r_mat = 0, 0.5, 0.9, 1 (≈ 20 s total); one cascade MC of 2×10⁵ histories (< 1 s); the rest closed form or
1-D quadrature. No heavy numerics.
**Literature** (lit.py → literature/papers-ERR-WP8/; PDFs and HTML deleted, `.txt` kept; page = PDF page):
- **used:** 2508.08858 (p.16: measured CaWO₄ C_ij, quoting J. M. Farley & G. A. Saunders, J. Phys. C 5, 3021 (1972), via its ref. [63] — a **secondary quote**; temperature
  not stated); cond-mat/9408044 (Table I, p.18: CsI B₀ "expt. 13.5" GPa, a₀ 4.56 Å, citing its ref. [11] (Mao et al.) — **secondary quote**); 1607.04560 reused from
  literature/papers-r17-VER-ERR-CW7/ (Table 1 p.25: E_K, E_L);
- **fetched, no usable data:** 0710.1057 (no CsI), 2603.24230 (CaWO₄ HBAR, no C_ij); 1610.04890: 404 (not fetched).
**Status.** CLAIMED (errata; R×2 owed, IF-EW-6).

---
## 0. Verdict map (what changed, where)
| # | Item | Corrected statement (short) | § |
|---|---|---|---|
| 1 | RC1 shear wording; C33 tolerance | cyclic shear mis-indexing (C₄₄ ↔ C₆₆ only for uniaxial); max C33-identity deviation 0.050 GPa | §1 |
| 2 | RC2 dropped rows | 11 dropped rows had [E]; the 2 non-[E] are GaAs S1 and SiO₂-q S1 | §2 |
| 3 | CaWO₄ width | measured tensor [FT, secondary] replaces the proxy: c_NR1 4.58 km/s, FOM 1.90; CaWO₄ leaves NR-heavy tier 1 | §3 |
| 4 | CsI width / floor | 1910.10716 c_LA 1.379 km/s is 20% **below** the bulk-modulus floor 1.73 km/s [D + FT]; replaced by a B-floor model, FOM 3.89 (was 6.39) | §4 |
| 5 | RC3 cascade_gf.py | h must divide E_g, θ_iiE_g, ω₀; code now enforces it; the coded h = 0.02 gave −1.6% on N̄ and +1.3% on ε/E_g | §5 |
| 6 | RC4 heavy window | pairwise, η-weighted: 1/c onset ≈ 4.2 m_min^{ac}(c_NR1); survivors 0.063–0.33 MeV (f.u. q_BZ) / 0.063–0.25 (primitive); 42-pool 0.10–0.27 / 0.10–0.25 | §6 |
| 7 | RC4 light correction | ℛ_light ∝ (η₀/ω_th)[1 − (1 + κ_η)m_min^{ac}/m_χ], κ_η = 3.14 (SHM) for m_χ ≲ m_hi | §7 |
| 8 | RC5 polar ε route; sapphire width | (8.1) interval for ε-only materials; interlacing hypothesis stated; sapphire σ 3% (𝓘 ∝ 1/ε_∞) | §8 |
| 9 | RC6 r^M | [D] as the sum-rule defect, [E] (lower estimate) as the one-magnon width | §9 |
| 10 | RC7 Ge EC L-lines | the L-lines of the light-daughter EC nuclides (⁴⁹V, ⁵¹Cr, ⁵⁴Mn, ⁵⁵Fe, ⁵⁶⁻⁵⁸Co) lie inside the sub-keV ROI | §10 |
| 11 | RC8 G-F6 | full isotope list generated from the table (⁴³Ca included), q̂-resolved projected DOS, normalisation, e^{−2W} | §11 |
| 12 | RC9 1910.10716 c_LA | GaN, AlN, ZnO CONFIRMED-inconsistent; **CsI CONFIRMED-inconsistent** (below the floor); CaWO₄ marginal (−2.3%); α-SiO₂, NaCl pending | §12 |
| 13 | Row 38; DATA-ADDENDA | diamond promoted to SURVIVOR (only material whose sole COND was S2); Al, YIG inputs superseded | §13 |
| 14 | VER-WP8-S rows 2, 3, 4, 5, 9, 11, 12 | r_mat wording; statement (ii) "excluding Migdal"; L-S3 factor on the whole FOM; tier count 117; R13 phrasing; Si ε_eh ±0.01; Ge/Si cosmogenics | §14 |
| 15 | L(k, ω) gap | computation specification | §15 |
| 16 | Ranking | r_mat variants, final readings, next-target guide, survivor table | §16 |
| 17 | Owed corrections | LIMITS, NOTATION, CORRECTIONS exact texts | §17 |
**No SURVIVOR verdict is reversed by the referee corrections.** Ranking changes (all from input changes): NR heavy (S) tier 1 = {TeO₂} only; NR edge (S) leader Al₂O₃ → C (row 38);
42-pool NR heavy CsI keeps the lead on a new, floor-respecting [E] model (FOM 6.39 → 3.89).

---
## 1. RC1 — JARVIS shear order: wording for PE, C33 tolerance (VER-ERR-CW7 row 0a, §A)
**Corrected statement.** The R14–R16 reading took JARVIS indices (3, 4, 5) as Voigt (yz, zx, xy); the true order is (xy, yz, zx). For uniaxial crystals (C₄₄ = C₅₅) this is a
C₄₄ ↔ C₆₆ swap; for orthorhombic PE it is a **cyclic shift**: old (C₄₄, C₅₅, C₆₆) = true (C₆₆, C₄₄, C₅₅) = (4.0, 8.8, 2.4) GPa vs true (8.8, 2.4, 4.0).
**Derivation.** Identity map old C_{(3+k)(3+k)} = J[3+k][3+k]; true Voigt yz ← J4, zx ← J5, xy ← J3 (build_v4 PERM [0, 1, 2, 4, 5, 3]). Hence old C₄₄ = J3 = true C₆₆,
old C₅₅ = J4 = true C₄₄, old C₆₆ = J5 = true C₅₅ (S3-C11, from jarvis_top.json and christoffel_v4.json). Max over the hexagonal/trigonal entries of
|J[3][3] − (J[0][0] − J[0][1])/2| = **0.050 GPa** (S3-C11), so the printed "0.05 GPa" is right and the code tolerance 0.11 is loose.
**Replacement texts.**
- WP8-U-v3 §0 row 10 and the build_v4.py note, for "C₄₄ and C₆₆ were swapped for every non-cubic entry": **"the shear block was cyclically mis-indexed (xy, yz, zx read as
  yz, zx, xy); for uniaxial crystals this is a C₄₄ ↔ C₆₆ swap, for orthorhombic PE the cyclic shift old (C₄₄, C₅₅, C₆₆) = true (C₆₆, C₄₄, C₅₅)."**
- CORRECTIONS §19.13 row "R14–R16 non-cubic elastic tensors", "built with C₄₄ ↔ C₆₆ swapped and C₁₄ misplaced" → "built with the shear block cyclically mis-indexed
  (C₄₄ ↔ C₆₆ for uniaxial; cyclic for PE) and C₁₄ misplaced".
- code/CW7/checks.py CW7-C33 (owed to its owner; outside this pass's write set only for build_v4.py): tolerance `ident < 0.11` → `round(ident, 3) <= 0.05` — **applied**
  as S3-C11 in code/REV-WP8-S; build_v4.py's docstring sentence is owed (§17.3).

## 2. RC2 — identity of the dropped rows (row 0b, §B)
**Corrected statement.** Of the 13 dropped duplicate screening rows, 11 carried [E]; the 2 non-[E] are **GaAs screen_S1 ([ABS]) and SiO₂-q screen_S1 ([UNVERIFIED])**.
GaAs S2's dropped row contained "[E]". Verified from code/CW7/data/v4_changes.json (S3-C10).
**Replacement (CW7-errata §1.1, first bullet):** "(with the 2 non-[E] GaAs rename rows superseded by the [FT] rows)" → **"(the 2 non-[E] dropped rows are GaAs S1 [ABS]
and SiO₂-q S1 [UNVERIFIED], each superseded by the kept row of its key)"**. CW7-errata §0 row V1 and WP8-U-v3 §0 likewise ("11 dropped with 2 more superseded rows" stands).

## 3. CaWO₄: measured elastic tensor replaces the proxy (VER-WP8-S-v2 rows 9–10; brief "justify or widen")
**Corrected statement.** CaWO₄ (Laue class 4/m) has measured C₁₁ 145.9, C₃₃ 127.4, C₁₂ 62.6, C₁₃ 39.2, C₁₆ −19.2 (C₂₆ = −C₁₆), C₄₄ 33.5, C₆₆ 38.7 GPa [FT 2508.08858
p.16, quoting Farley & Saunders 1972 — secondary, T not stated]. With ρ_T 6.115 g/cm³ (a_exp [FT] + NIST masses) the Christoffel solve gives **c_NR1 = 4.58 km/s, c̄_LA 4.65,
LA range [4.36, 5.17], c_LA,max 5.17 km/s** (S3-C1; the sign of C₁₆ changes no speed statistic, it is a rotation about c). Width σ_ln 0.02 [E] (ultrasonic C_ij, secondary
quote, unstated T). Heavy-mediator FOM **1.90 [1.86, 1.94]** (v2 proxy 2.07 [1.53, 2.79]); NR edge 11.0 keV (v2 12.8).
**Derivation.** ρω² = C_ijklq_jq_l (LT1), eigenvectors ê_ν; c_NR1 = ⟨Σ_ν(q̂·ê_ν)²/c_ν⟩⁻¹ on 4×10⁴ random q̂ (the CW7-C34 construction); tensor positive definite
(min eigenvalue 25.9 GPa).
**Consequence.** R10 changes: NR heavy (S) tier 1 = {TeO₂} (P₁ 0.951); CaWO₄ joins Ge and GaAs in tier 2. A-5's request (one tier TeO₂/CaWO₄/Ge/GaAs) is now met for
CaWO₄/Ge/GaAs, and TeO₂ separates on the MC (P(TeO₂ ≻ CaWO₄) = 0.987).
**Replacement texts.** WP8-S-v2 §0 row 3 → "**TeO₂, P = 0.951** (then CaWO₄/Ge/GaAs one tier); CaWO₄ on its measured tensor [FT 2508.08858 p.16, secondary]"; §2.3 table
row CaWO₄ → "1.90 [1.86, 1.94] | 2 | 0.007 | 2–3 | 4.58 from measured C_ij (Farley & Saunders 1972 via 2508.08858 p.16) + Christoffel; σ_ln 0.02 [E]"; delete the
"Proxy width (R10)" paragraph; §6 item 2 → "Measured C_ij for TeO₂ and CsI (CaWO₄: measured, secondary quote; primary to be read)".

## 4. CsI: the 1910.10716 c_LA lies below the bulk-modulus floor (VER-WP8-S-v2 row 9)
**Corrected statement [D + FT].** For a cubic crystal c_LA(q̂) ≥ √(B/ρ_T) in every direction. CsI's measured B = 13.5 GPa [FT cond-mat/9408044 Table I p.18, secondary]
and ρ_T = 4.529 g/cm³ give **c_LA ≥ 1.726 km/s**; 1910.10716's c_LA = 1.379 km/s (a sphere average of ω_LA/q, App. A3) is **20% below** it and is rejected.
**Derivation.** Rayleigh: the largest Christoffel eigenvalue satisfies ρc_qL² ≥ q̂·Γ·q̂ = C_ijklq̂_iq̂_jq̂_kq̂_l. For cubic symmetry this quartic form is
C₁₁ − 2(C₁₁ − C₁₂ − 2C₄₄)Σ_{i<j}q̂_i²q̂_j², a convex combination of its [100] value C₁₁ and its [111] value (C₁₁ + 2C₁₂ + 4C₄₄)/3. With B = (C₁₁ + 2C₁₂)/3:
C₁₁ − B = 2(C₁₁ − C₁₂)/3 ≥ 0 and (C₁₁ + 2C₁₂ + 4C₄₄)/3 − B = 4C₄₄/3 ≥ 0 under Born stability (sympy, S3-C2). Hence ρc_qL² ≥ B for every q̂, and the sphere average too.
**Replacement model [E].** c_LA = √(3B(1 − ν)/((1 + ν)ρ_T)) (isotropic, Voigt-type), ν ∈ U[0.20, 0.35] around the Cauchy value **ν = 1/4** [D: central pair forces give
C₁₂ = C₄₄; with isotropy C₁₁ − C₁₂ = 2C₄₄ this is λ = μ, ν = λ/(2(λ + μ)) = 1/4; sympy S3-C2], σ_ln(B) 0.07, an isotropic-to-sphere-average σ_ln 0.05, × the
median cubic branch factor c_NR1/c̄_LA = 0.964. Central c_LA 2.32 km/s, **FOM 3.89 [3.61, 4.21]** (v2: 6.39). The model respects the floor for every ν ≤ 1/2 (ν = 1/2 is the floor).
**Robustness.** CsI leads the 42-pool heavy row against Bi₂Se₃ (3.04) for any ν ≳ 0.01 at the medians (ν → 0, the stiffest isotropic solid allowed, ties it); at the floor
FOM = 5.2. P₁ = 0.974 (r_mat = 0), 0.984 (r_mat = 1); it is still **[E]-driven** (ν), and it applies only in CsI's window, m_χ ≳ 0.10 MeV (§6).
**Replacement texts.** WP8-S-v2 §0 row 3, 42-pool column: "CsI 3.89× Si, P = 0.974 (B-floor model: measured B [FT, secondary] + ν [E]; the 1910.10716 c_LA violates the
floor)"; §2.3 42-pool tiers: "t1 CsI 3.89 (P₁ 0.974; c_LA = √(3B(1 − ν)/((1 + ν)ρ)), B 13.5 GPa [FT cond-mat/9408044 p.18], ν U[0.20, 0.35] [E]: **[E]-driven**); t2
Bi₂Se₃ 3.04, NaI 2.98, PbTe† 2.80, PbSe† 2.60"; delete "For CsI the same proxy sits in the 1910.10716 'suspect' class (WP8-U-v3 §5)" (VER-WP8-S-v2: CsI was never in that list);
R13 → "CsI leads on a floor-respecting [E] model (B measured, ν declared); 1910.10716's c_LA is rejected (below √(B/ρ))". The NR-edge (39.4 → 24.0 keV, from c_max) and the
light-mediator factor inherit the same model.

## 5. RC3 — cascade_gf.py: commensurate grid (row 0c-ii, 1.4; §C2)
**Corrected statement.** The LE-153 solver reads G, ρ and p at x − E_g, x − ω₀ and x ≥ θ_iiE_g on the grid, so **h must divide E_g, θ_iiE_g and ω₀**. Otherwise it solves the
problem with ω₀,eff = h·round(ω₀/h) (0.054 → 0.06 at h = 0.02, 0.05 at h = 0.01), the h-sequence is non-monotone and h-Richardson is invalid.
**Fix (code/CW7/cascade_gf.py).** `check_grid(h, w, theta, strict)` is called by `CascadeGF` and `moments_fast` (for λ > 0; at λ = 0 ω₀ does not enter): a non-commensurate
grid raises `ValueError` (default) or, with strict=False, runs and records ω₀,eff in `.w_eff`. `commensurate_h(w, θ, h_max)` returns the largest h = 1/N ≤ h_max dividing 1,
θ, w (ω₀ = 0.054, θ 3/2 → h = 0.002, 0.001). `moments_fast` now uses BLAS dot products on a pre-reversed ρ (same sums; X = 40 at h = 0.002 in 12 s instead of 130 s).
**Rerun (code/CW7/checks.py, 41/41 PASS).**
- CW7-C5c: independent MC of the exact cascade (Dirichlet(3/2, 3/2, 3/2) split of x − 1, p = 1/(1 + λρ(x − ω₀)/Φ(x − 1)), 2×10⁵ histories, x = 8, λ 3.55, θ_ii 3/2):
  ω₀ = 0.054: MC **2.1288 ± 0.0012**, grid 2.12998 (h 0.002) / 2.13002 (h 0.001) — monotone and converged to 4×10⁻⁵; VER's MC 2.1326 ± 0.0027 agrees (1.3σ).
  ω₀ = 0.05: MC 2.1545 ± 0.0012, grid 2.15336/2.15340. The old h = 0.02 run (ω₀,eff 0.06) is biased by **−1.61%**; the guard raises on it.
- CW7-C7 (Si case λ 3.55, ω₀ 0.054, θ 1, X 40): commensurate h = 0.002: **F = 0.1139, ε/E_g = 3.2185**; the h = 0.02 run (ω₀,eff 0.06) gives F 0.1147, ε/E_g 3.2610 (**+1.3%**).
  The GAP-EF 0.114 still holds to its last digit; the agreement "C7 = GAP-EF 0.1147" was code-to-code on the same quantised grid.
- C5, C5b, C8 now run at h = 0.002 (ΣP − 1 ≤ 2×10⁻¹⁶; means = moment recursion to 10⁻⁹).
**Interface (IF-EW-1, out of write scope).** code/GAP-EF/cascade.py and code/GAP-EF-v2 quantise ω₀ the same way (`self.nw = round(w/h)`, `self.w = nw·h`): every GAP-EF(-v2)
ε_eh, F prediction at h = 0.02 is for ω₀,eff, not ω₀. For the Si case the bias is +1.3% in ε_eh (inside the GAP-EF −6.5/+24.6% band, so no ranking changes); per material it
depends on ω₀/h mod 1 (up to |Δω₀|/ω₀ ≤ h/(2ω₀)). Owed: rerun GAP-EF-v2 on commensurate grids.
**Replacement texts.**
- CW7-errata §1.4 "Convergence criteria: h-Richardson (C6: O(h)) …" → append: **"Pitfall: h must divide E_g, θ_iiE_g and ω₀ (ρ and p are also read at x − ω₀); otherwise the
  solver solves the problem with ω₀,eff = h·round(ω₀/h) and h-Richardson is invalid (at h = 0.02, ω₀ = 0.054E_g: N̄(x = 8) −1.6%, ε/E_g +1.3%). The code raises on a
  non-commensurate grid; commensurate_h gives the grid (0.002 for ω₀ = 0.054)."**
- cascade_gf.py docstring: done (ERR-WP8 paragraph).
- L-H2 leading-correction column: append "; grid commensurate with E_g, θ_iiE_g, ω₀ (else ω₀,eff = h·round(ω₀/h))" (§17.1).

## 6. RC4 — heavy-mediator single-phonon window, pairwise (row 0d-ii; VER-WP8-S-v2 row 1, §A; B-1)
**Corrected statement.** For two materials A, B the heavy-mediator rate ratio equals c_NR1,B/c_NR1,A to 10% for m_χ in the pairwise window
W_AB = [max(m_on,A, m_on,B), min(m_up,A, m_up,B, m_hi,A, m_hi,B)], with
- **m_on ≈ 4.2 m_min^{ac}(c_NR1)** (η-weighted 10% onset; 4.0–4.5 over the survivors, S3-C4), m_min^{ac}(c) = ω_th/(2c(v_max − c)) the (2.3b) kinematic edge (rate → 0 there);
- m_hi = q_BZ/(2v_max) (above it the q ≪ q_BZ form (2.3a″) fails: Umklapp, multiphonon), with q_BZ either the f.u.-Debye upper estimate or the primitive-cell value
  q_BZ/Z_prim^{1/3};
- m_up the computed 10% upper end below m_hi.
The **common windows** (every ranked material vs Si, ω_th = 1 meV, CONVENTIONS §8 SHM): **survivors 0.063–0.33 MeV (f.u.) / 0.063–0.25 MeV (primitive)** (TeO₂ sets the lower,
CaWO₄ / TeO₂ the upper end); **42-pool 0.104–0.274 MeV (f.u.) / 0.104–0.250 MeV (primitive)** (CsI lower, Bi₂Se₃ / TeO₂ upper). Pairwise windows of every adjacent pair are in
data/ranking_v3.json (`NR_heavy_window_adjacent_{fu,prim}_MeV`), e.g. TeO₂/CaWO₄ 0.052–0.33 (f.u.), CsI/Bi₂Se₃ 0.091–0.274.
**Derivation.** (2.3a″) with F_DM = 1 and u = q/(2m_χ): ℛ_A ∝ (8m_χ³/c_A)∫_{u₋}^{u₊}u²η(c_A + u)du, u₋ = ω_th/(2m_χc_A), u₊ = min(v_max − c_A, q_BZ,A/(2m_χ)). The 1/c scaling
needs the integral to be its m_χ- and c-independent value I₀ = ∫₀^{v_max}u²η(u)du; the dominant loss is the lower cut δ_lo = ∫₀^{u₋}u²η du/I₀, which reaches 10% at
u₋ ≈ 0.24 v_max because η falls steeply toward v_max (the integrand is weighted to low u, so the flat-η "1/8" of WP8-S-v2 was too optimistic). With u₋ = (v_max − c)m_min^{ac}/m_χ
this is m_on ≈ 4.2 m_min^{ac}. For a pair the errors partly cancel (ratio error ≈ δ_A − δ_B), so W_AB is wider than either per-material window when c_A ≈ c_B.
**Reconciliation of the two referees.**
- VER-ERR-CW7: "(2.3b) = 6.5 keV (Si), 41 keV (CsI)" is the **kinematic edge** m_min^{ac}, not the onset; "0.1 MeV" in WP8-F-v3 was 1910.10716's regime boundary (p.10).
  Its CsI/Si ratios (3.42, 6.09, 6.48, 5.60 at 0.1, 0.2, 0.3, 0.43 MeV; c 1.379, Γ–X q_top) are reproduced (S3-C4) and give 10% agreement for ≈ 0.2–0.4 MeV with that q_top.
- VER-WP8-S-v2: "≈ 0.065–0.34 MeV (S), CsI 0.17" used the same η-weighted criterion with f.u.-Debye q_BZ; TeO₂/Si 0.83, 2.31 at 0.03, 0.1 MeV reproduced (S3-C4).
- Both are the same criterion; they differ only by q_top (Γ–X vs f.u.-Debye vs primitive) at the upper end and by the per-material vs pairwise reading. This errata adopts the
  pairwise criterion with the m_hi cap and prints both q_BZ conventions. **CsI's lower end moved 0.17 → 0.10 MeV** because its c changed (§4); the survivor lower end
  (TeO₂, 0.063) agrees with VER-WP8-S-v2's 0.065.
**Replacement texts.**
- WP8-F-v3 §0 NR-1ph row, §2.3(a″), §5.1 and L-F1: "only for ≈ 0.1 ≲ m_χ ≲ q_BZ/(2v_max) (Si 0.43 MeV)" and "**m_χ,edge ≈ 0.1 MeV (1 meV, (2.3b)) ≲ m_χ ≲ q_BZ/(2v_max)**"
  → **"for a pair of materials when m_χ ≳ 4.2 m_min^{ac}(c_NR1) of the softer one (η-weighted, 10%) and m_χ ≲ q_BZ/(2v_max) of the heavier cell (ω_th = 1 meV: survivors
  0.063–0.33 MeV with f.u.-Debye q_BZ, 0.063–0.25 MeV with primitive cells; CsI ≳ 0.10 MeV); m_min^{ac} of (2.3b) is the kinematic edge (6.6 keV for Si at c_NR1), not the
  onset; 0.1 MeV is 1910.10716's regime boundary (p.10)."**
- WP8-S-v2 §0 row 3 "(window ≈ 0.03–0.34 MeV)" → "(pairwise window; survivors 0.063–0.33 MeV f.u. / 0.063–0.25 primitive)"; §2.3 "Validity window [E]" paragraph → the
  corrected statement above; R13 "window 0.083–0.27 MeV" → "0.104–0.27 MeV (f.u.) / 0.104–0.25 (primitive)"; closing-table row B-1 "S 0.030–0.34, 42-pool 0.083–0.27" →
  "S 0.063–0.33, 42-pool 0.104–0.27 MeV (pairwise, η-weighted)".

## 7. RC4 — light mediator: the O(m_min^{ac}/m_χ) correction (row 0d-i, §D1)
**Corrected statement [D to first order].** With F_DM² ∝ q⁻⁴, for m_min^{ac} ≪ m_χ ≤ m_hi,
  ℛ_NR1^{light} ∝ (η₀/ω_th)·[1 − (1 + κ_η)·m_min^{ac}/m_χ + O((m_min^{ac}/m_χ)²)],  κ_η ≡ (u₊/η₀)∫₀^{u₊}(η₀ − η(u))u⁻²du,  u₊ = v_max − c,   (EW-7.1)
and for m_χ > m_hi the same with m_min^{ac}/m_χ → ω_th/(c q_BZ) and u₊ → q_BZ/(2m_χ) (the WP8-F-v3 residual factor). **κ_η = 3.14** for the CONVENTIONS §8 SHM. The material
enters through m_min^{ac}; the per-mass rate is target-independent only for **m_χ ≫ (1 + κ_η)m_min^{ac}** of every compared material.
**Derivation.** ∫_{q₋}^{q₊}q²q⁻⁴η(c + q/2m)dq/c = (1/(2mc))∫_{u₋}^{u₊}η(c + u)u⁻²du, u₋ = ω_th/(2mc). Write η = η₀ − (η₀ − η): ∫η/u² = η₀/u₋ − η₀/u₊ − ∫_{u₋}^{u₊}(η₀ − η)/u²
= (η₀/u₋)[1 − (u₋/u₊)(1 + κ_η)] + O(u₋) because the lab-frame η is flat at the origin (η₀ − η = O(u²), so the integral from 0 to u₋ is O(u₋)); the prefactor η₀/(2mcu₋) = η₀/ω_th.
For m_χ ≤ m_hi, u₋/u₊ = m_min^{ac}/m_χ exactly. sympy on η = η₀ − a₂u² − a₃u³: the remainder → 0 as u₋ → 0 (S3-C5). The η-shift by c is O(c²/v₀²) (also flat).
**Numbers (S3-C5, data/ranking_v3.json `NR_light`).** Old inputs (c 1.379, Γ–X q_top): CsI/Si = 0.11, 0.42, 0.58, 0.69, 0.82 at 0.1, 0.2, 0.3, 0.43, 1 MeV — VER-ERR-CW7
reproduced. v3 inputs: CsI/Si 0.37, 0.65, 0.76, 0.83, 0.91, 0.93 at 0.1, 0.2, 0.3, 0.43, 1, 10 MeV; TeO₂/Si 0.66, 0.83, 0.88, 0.92, 0.96, 0.98. The first-order form is within 3%
of the full integral for m_χ ≥ 10 m_min^{ac} (Ge, TeO₂, GaAs at 0.3 MeV) and fails near the edge (CsI at 0.1 MeV ≈ 4 m_min). Large-m_χ spread of the residual factor
1 − ω_th/(c q_BZ): 0.922 (CsI) – 0.996, **×1.08** (v2 ×1.15).
**Replacement texts.**
- L-F4 leading-correction column: "O(ω_th/(c q_up)) band-top/kinematic term (CsI/Si 0.85); O(c/v_max) in η" → **"O(m_min^{ac}/m_χ): factor 1 − (1 + κ_η)m_min^{ac}/m_χ,
  κ_η = 3.14 (SHM), dominant within ≈ 30× the softer material's edge; above m_hi the band-top term ω_th/(c q_BZ); the c-shift of η is O(c²/v₀²)"**.
- WP8-F-v3 §0 NR-1ph row and §5.1, and WP8-S-v2 §0 row 4 / §1.2: "target-independent above the edge" → **"target-independent for m_χ ≫ (1 + κ_η)m_min^{ac} of every compared
  material (κ_η = 3.14); material factor spread ×1.08 at large m_χ"**.
- WP8-F-v3 §2.3(a″): "ℛ_NR1 ∝ πq₀⁴η̄/(m_u²ω_th)·[1 − O(ω_th/(c q_up)) − O(c/v_max)]" → "ℛ_NR1 ∝ πq₀⁴η₀/(m_u²ω_th)·[1 − (1 + κ_η)min(m_min^{ac}/m_χ, ω_th/(c q_BZ)) + O(·²)]".

## 8. RC5 — polar ε-route bound; sapphire width (row 0d-iii, §D2; VER-WP8-S-v2 row 8)
**Corrected statement.** (i) The per-axis bound (π/2)(1/ε_∞ − 1/ε₀)ω_max ≥ 𝓘_pol requires a lossless factorised ε **with interlacing** ω_T1 < ω_L1 < ω_T2 < … (all partial-fraction
residues of 1/ε positive) and ε₀ of that model; ε₀ of the model is ε_∞Π(ω_L/ω_T)², i.e. it needs the mode list, which already gives 𝓘_pol exactly. With measured ε₀ (9.3 ⊥, 11.5 ∥)
and ε_∞ = 3.26 the same formula gives 9.05 < 9.27 (VER-ERR-CW7 §D2). So the ω_L,max form is a **consistency statement for materials with mode data, not a ranking input**.
(ii) **ε-route materials (no mode data) are ranked by the (8.1) interval** [(π/2)Δε⁻¹ω_T,min, (π/2)Δε⁻¹ω_T,max√(ε₀/ε_∞)]/ρ_T, with ω_O,min ≤ ω_T,min as the available lower
frequency. rank.py already does this (SiO₂-q, MgF₂ intervals; TeO₂, h-BN bound-only on the upper end) — S3-C6 asserts it. (iii) "Damping adds O(γ_L/ω_L)" is [E].
(iv) **Sapphire:** at fixed mode frequencies every residue of 1/ε scales as 1/ε_∞ (sympy, S3-C6), so 𝓘_pol ∝ 1/ε_∞ exactly; ε_∞ 3.1–3.3 moves it by ±3%. Width now
σ_ln 0.03 (⊕ damping U[1, 1.03]): **9.40 [9.12, 9.71]** (v2 [9.31, 9.51]). NaF–Al₂O₃ still tie (P(NaF ≻ Al₂O₃) = 0.587).
**Replacement texts.**
- WP8-F-v3 §2.5, last sentence ("Rank ε-route materials by this bound as an interval (with the (8.1) lower end), never against central Z*-route values."), IF-ERR7-1 and IF-F1′:
  → **"For ε-route materials (no mode data) rank by the (8.1) interval [(π/2)Δε⁻¹ω_T,min, (π/2)Δε⁻¹ω_T,max√(ε₀/ε_∞)]/ρ_T; the ω_L,max bound holds for a lossless factorised,
  interlacing ε with ε₀ of that model (mode data) and is a consistency statement, not a ranking input. Damping adds O(γ_L/ω_L) [E]."**
- L-F2 validity: insert "interlacing (all residues of 1/ε ≥ 0)" after "lossless factorised ε per principal axis"; append "; the ω_L,max form only with mode data".
- WP8-S-v2 §1.3 row "[FT] measured, stated error … sapphire modes < 0.5%" → add "sapphire 𝓘_pol σ_ln 0.03 from ε_∞ (𝓘 ∝ 1/ε_∞ at fixed modes)"; §2.5 Al₂O₃ row "9.41 [9.31, 9.51]"
  → "9.40 [9.12, 9.71]".

## 9. RC6 — r^M status (row 1.7, §C4)
**Corrected statement.** r^M ≡ ΔS/S is the **LSWT defect of the total equal-time transverse sum rule** (Casimir identity, LSWT vacuum) **[D]**. W_⊥ contains the one-magnon and the
three-magnon weight, so the exact one-magnon weight is ≤ W_⊥: as the width of the one-magnon weight ΔS/S is a **lower estimate [E]**. ⟨n²⟩ is evaluated in the LSWT vacuum,
so W_⊥ is itself O(S⁰)-accurate. Its use as the single M width of the residual magnon row is a declared choice. The magnon-velocity renormalisation (edges) is a separate nuisance.
**Replacement texts** (CW7-errata §1.7 first bullet head; WP8-F-v3 §2.6 "Residual width [D for the size]"; WP8-F-v3 §4 MAG row; L-H4; WP6 §5.2 row via CW7-errata §2.1):
- "r^M derived [D for the size, E as a width]" / "Residual width [D for the size]" → **"r^M ≡ ΔS/S is the LSWT defect of the transverse sum rule (Casimir identity, LSWT vacuum)
  [D]; as the width of the one-magnon weight it is a lower estimate [E] (W_⊥ includes the three-magnon weight)."**
- "the O(S⁰) truncation overstates the one-magnon weight by r^M = ΔS/S" → "the O(S⁰) truncation overstates the transverse weight by ΔS/S; the one-magnon overstatement is
  ≥ ΔS/S".
- L-H4 leading correction: "O(1/S): one-magnon weight defect ΔS/S (C14b)" → **"O(1/S): transverse sum-rule defect ΔS/S (C14b), a lower estimate of the one-magnon defect"**.
- CW7-errata §0 / VER row 1.14 status: "r^M [D]" → "r^M [D] as sum-rule defect, [E] as width".

## 10. RC7 — Ge EC L-lines inside the sub-keV window (row 1.11, §E1)
**Corrected statement.** The L-lines of ⁶⁵Zn, ⁶⁸Ga, ⁶⁸Ge, ⁷¹Ge (1.10–1.30 keV [FT 1607.04560 p.10, Table 1 p.25]) lie above 1 keV; the L-lines of the lighter-daughter EC nuclides
**⁴⁹V (→Ti), ⁵¹Cr (→V), ⁵⁴Mn (→Cr), ⁵⁵Fe (→Mn) and ⁵⁶,⁵⁷,⁵⁸Co (→Fe)**, all in 1607.04560 Table 1, and all M-lines lie **inside** the sub-keV ROI. ⁴⁹V and ⁵⁵Fe are in WP8-U-v3's own
Ge production table (2.8 and 4.6 /(kg·d)).
**Derivation [E from FT].** Table 1 gives E_L/E_K = 1.10/8.98 = 0.1225 (Cu), 1.19/9.66 = 0.1232 (Zn), 1.30/10.37 = 0.1254 (Ga): increasing with Z. Extending the monotone trend
downward, E_L ≤ 0.1225 E_K for the lighter daughters: Ti ≤ 0.61, V ≤ 0.67, Cr ≤ 0.73, Mn ≤ 0.80, Fe ≤ 0.87 keV, all < 1 keV (S3-C12). Standard L₁ tables give ≈ 0.56, 0.63,
0.70, 0.77, 0.85 keV [UNVERIFIED], consistent.
**Replacement texts.** CW7-errata §1.11 "EC lines" bullet, WP8-U-v3 §4.4 lines 163–164 ("… above the < 1 keV ROI: only M-lines and resolution tails of the L-lines enter the sub-keV
rate") and v4 row `Ge cosmo_EC_lines_subkeV` value → **"K lines ≈ 5–11 keV; the dominant ⁶⁵Zn, ⁶⁸Ga, ⁶⁸Ge, ⁷¹Ge L-lines (1.10–1.30 keV) lie above 1 keV; the L-lines of the
lighter-daughter EC nuclides (⁴⁹V, ⁵¹Cr, ⁵⁴Mn, ⁵⁵Fe, ⁵⁶⁻⁵⁸Co; ≤ 0.61–0.87 keV from the E_L/E_K trend of 1607.04560 Table 1) and all M-lines (~0.1 keV) are inside the sub-keV ROI"**.

## 11. RC8 — G-F6 specification completed (row 1.12, §F)
**Corrected specification** (replaces the *What* and adds to *Level*, *Pitfalls* of CW7-errata §1.12):
- **What.** w_iso for every J ≠ 0 isotope of every pool material, generated from the v4 `isotopes[El]` rows (S3-C13: 42 materials, 104 material–isotope entries). Survivors:
  Al₂O₃ ¹⁷O, ²⁷Al · **CaWO₄ ¹⁷O, ⁴³Ca, ¹⁸³W** · GaAs ⁶⁹,⁷¹Ga, ⁷⁵As · Ge ⁷³Ge · Li₂MoO₄ ⁶,⁷Li, ¹⁷O, ⁹⁵,⁹⁷Mo · γ-LiAlO₂ ⁶,⁷Li, ¹⁷O, ²⁷Al · LiF ⁶,⁷Li, ¹⁹F · NaF ¹⁹F, ²³Na ·
  Si ²⁹Si · TeO₂ ¹⁷O, ¹²³,¹²⁵Te · **C ¹³C** (row 38). SURVIVOR-COND: AlN ¹⁴,¹⁵N, ²⁷Al · Al ²⁷Al · Bi₂Se₃ ⁷⁷Se, ²⁰⁹Bi · CaF₂ ¹⁹F, ⁴³Ca · Cr₂O₃ ¹⁷O, ⁵³Cr · CsI ¹²⁷I, ¹³³Cs ·
  GaN ¹⁴,¹⁵N, ⁶⁹,⁷¹Ga · GaSb ⁶⁹,⁷¹Ga, ¹²¹,¹²³Sb · MgF₂ ¹⁹F, ²⁵Mg · MgO ¹⁷O, ²⁵Mg · MnO ¹⁷O, ⁵⁵Mn · NaCl ²³Na, ³⁵,³⁷Cl · NaI ²³Na, ¹²⁷I · Nb ⁹³Nb · NiO ¹⁷O, ⁶¹Ni ·
  NiPS₃ ⁶¹Ni, ³¹P, ³³S · PE ¹H, ¹³C · PbS ³³S, ²⁰⁷Pb · PbSe ⁷⁷Se, ²⁰⁷Pb · PbTe ¹²³,¹²⁵Te, ²⁰⁷Pb · SiC (3 polytypes) ¹³C, ²⁹Si · SiO₂-q ¹⁷O, ²⁹Si · SrTiO₃ ¹⁷O, ⁴⁷,⁴⁹Ti, ⁸⁷Sr ·
  YIG ¹⁷O, ⁵⁷Fe, ⁸⁹Y · ZnO ¹⁷O, ⁶⁷Zn · ZnS ³³S, ⁶⁷Zn · ZrTe₅ ⁹¹Zr, ¹²³,¹²⁵Te · c-BN, h-BN ¹⁰,¹¹B, ¹⁴,¹⁵N. **Do not print a partial list; regenerate from the table.**
- **Response (normalisation and e^{−2W}).** S^{inc,(1)}_κ(q, ω) = e^{−2W_κ(q)}(1/(2M_κ))Σ_ν|q·e_κν|²δ(ω − ω_ν)/ω_ν at T = 0, with Σ_ν over the 3N modes and e_κν normalised on
  the κ sublattice. For a **cubic site** this reduces to (q²/(6M_κ))D_κ(ω)/ω with ∫D_κ dω = 3 (equivalently (q²/2M_κ)D̃_κ/ω with ∫D̃_κ = 1). e^{−2W_κ} is kept (it is not ≈ 1 at
  q ~ q_BZ for light κ).
- **Anisotropy.** For non-cubic sites (the uniaxial survivors Al₂O₃, TeO₂, γ-LiAlO₂, CaWO₄; also the layered/chain COND materials) use the q̂-resolved projected DOS
  D_κ(q̂, ω) = Σ_ν|q̂·e_κν|²δ(ω − ω_ν), not D_κ/3. Pitfall added: "the angle-averaged D_κ/ω is exact only for cubic sites".
- Missing steps (two) and the status GAP stand as in CW7-errata §1.12.

## 12. RC9 — 1910.10716 Table I c_LA ratings (row 2a, §E2; extended)
| Material | 1910.10716 c_LA (km/s) | Test | Rating |
|---|---|---|---|
| GaN, AlN, ZnO | 12.50, 17.09, 12.53 | above the measured-C_ij LA maximum (8.18, 11.34, 6.18; ×1.53, 1.51, 2.03) [FT 1110.1346 p.2, cond-mat/0507217 p.7] (VER-ERR-CW7) | **CONFIRMED inconsistent** |
| **CsI** | 1.379 | below the floor √(B/ρ) = 1.726 km/s [D + FT cond-mat/9408044 p.18] (§4) | **CONFIRMED inconsistent** (−20%) |
| CaWO₄ | 4.257 | 2.3% below the measured LA minimum 4.36 (§3) | marginal: within the C_ij/temperature uncertainty of a secondary quote |
| α-SiO₂, NaCl | – | no measured C_ij read | pending |
**Replacement (WP8-U-v3 §0 row 7, §5):** "1910.10716 hexagonal/NaCl c_LA **suspect, pending measured C_ij**" → **"1910.10716 Table I c_LA: GaN, AlN, ZnO and CsI CONFIRMED
inconsistent with measured elasticity (GaN, AlN, ZnO above every Christoffel LA speed [FT 1110.1346 p.2, cond-mat/0507217 p.7]; CsI below √(B/ρ) with measured B
[FT cond-mat/9408044 p.18]); CaWO₄ 2.3% below its measured LA range (marginal); α-SiO₂, NaCl pending"**. v4 rows `c_LA` of CsI and CaWO₄: note "superseded for ranking by
WP8-errata §3–§4".

## 13. Coordinator inputs: CONVENTIONS §13 row 38 and the DATA-ADDENDA supersessions
### 13.1 Row 38 (S2 = ≥ 1 g total as an array of ≥ ~0.1 g instrumented crystals with demonstrated mK readout)
**Re-evaluation of every S2-COND material** (18 in the pool; S3-C16). A material is promoted only if S2 was its sole non-PASS screen (S1, S3 PASS, S4 PASS) and the array
rule is met on evidence:
| Material | S2 under row 38 | Other screens | Verdict |
|---|---|---|---|
| **C (diamond)** | **PASS**: 0.175 g CVD crystals with mK W-TES readout at 16.8 eV [FT 2310.05815 p.1] | S1 PASS, S3 PASS, S4 PASS | **SURVIVOR** (promoted) |
| YIG | not shown (mm spheres; no ≥ 0.1 g crystal with mK readout in the texts read) | S3 COND | SURVIVOR-COND |
| Al, Nb | metal targets: ≥ 0.1 g pieces exist; mK SC readout of bulk crystals not shown in the texts read [UNVERIFIED] | S3 COND (Nb also S1) | SURVIVOR-COND |
| PbTe, Cr₂O₃ | not shown | S3 COND, S4-COND | SURVIVOR-COND |
| SiC-3C, AlN, ZnO, NaCl, ZnS, PbS, PbSe, ZrTe₅, NiO, MnO, NiPS₃ | not shown (and/or purity, not size) | S1 and S3 COND | SURVIVOR-COND |
| h-BN, c-BN (S2 FAIL) | mm-scale / sub-mm crystals: < 0.1 g per crystal | S1, S3 COND | SURVIVOR-COND (unchanged) |
| PE | (S2 COND) | S3 FAIL | SURVIVOR-COND (unchanged) |
**Only diamond changes status.** The promotion is implemented in rank.py (`ROW38_PROMOTED`); the v4 `verdict` and `screen_S2` rows of C are an owed WP8-U correction (§17.3).
**Array caveats (carried as caveat columns, not FAILs; `ARRAY_CAVEAT`):** diamond needs ≥ 6 × 0.175 g crystals for 1 g: per-crystal readout channels and thresholds (the 16.8 eV is
per crystal); surface-to-volume ratio ×(1/0.175)^{1/3} = 1.8 for surface backgrounds; per-crystal low-energy-excess and stress-release rates (GAP).
**Leader changes among survivors.** NR edge: **Al₂O₃ (5.16 keV) → C (3.15 keV [2.90, 3.43], P₁ 1.000, P(C ≻ Al₂O₃) = 1.000)**; both on DB tensors [E], diamond on its
isotropic-ish stiff tensor (no directional caveat, unlike h-BN). No other survivor leader changes: C is t5 in ER edge (1.56 MeV), t5 in ER quanta (13.1 eV), last in NR heavy (0.48),
non-polar (POL not ranked), t2 in Migdal.
### 13.2 DATA-ADDENDA (state/DATA-ADDENDA.csv, CW8-LIT R17) — supersessions applied in the rerun
- **Al:** measured C₁₁/C₁₂/C₄₄ = 114.3/61.9/31.6 GPa [FT 2109.13551 Table 2 p.5, quoting Kamm & Alers 1964, 0 K] and ρ_T = 2.698 g/cm³ from a_exp 4.05 Å (fcc, 4 atoms) replace
  the v4 DB tensor (C₄₄ 16.2 GPa, ×1.95) and ρ_DFT 2.663: c_NR1 5.89 → **6.63 km/s**, c_LA,max 5.92 → 6.71 km/s (S3-C3). Al NR heavy 1.31 (t6, was 1.48 in t5), NR edge
  accordingly; Migdal ρ updated. Al stays SURVIVOR-COND.
- **YIG:** ρ_T 4.9475 → **5.173 g/cm³** (a = 12.3750 Å, COD 2101364) in the Migdal row (the only YIG row that uses ρ); the n_e^{val} density scales the same way (×1.045).
- **Ir:** not in the pool; no ranking input touched.
- **Not touched by the rerun and owed (§17.3):** christoffel_v4.json Al and Ir entries; v4 Al `c_L_iso`, `c_T_iso`, `n_e_val`, `v_F_free_E`, `E_F_free_E`, `k_TF_free_E` (all built on
  ρ_DFT or the DB tensor); v4 YIG `a_exp` 12.56, `rho_T_from_a_exp`, `n_e_val`, and 𝓃_spin (×1.045) in the MAG row; the Al/Ir AMM/DMM film inputs of WP8-R-v2.

## 14. VER-WP8-S-v2 rows 2, 3, 4, 5, 9, 11, 12 and §E — texts
- **Row 2 (r_mat).** WP8-S-v2 §1.3 "By CONVENTIONS row 29 (CW7-errata §2.1) this is the conservative choice for a ranking …" → **"r_mat = 0 is conservative for resolved orderings
  only. Tiers are built from marginal 68% intervals and are correlation-blind; ties and 'no reading' statements are reported at r_mat = 0 and at the row-29 same-method value
  r_mat = 1 (family-wise: c_DB, ρ_DB, ε_DB, ω_DB, FT-DFT, GAP-EF, X_pole, room→0 K shift; independently measured [FT] inputs stay independent). The Migdal and 42-pool NR-edge
  ties resolve at r_mat → 1 (§16.1)."** rank.py and checks.py docstrings updated. L-S1 validity "inputs independent across materials (r_mat = 0, same-sign elasticities)" →
  "family-wise r_mat ∈ {0, 0.5, 0.9, 1} per CONVENTIONS row 29"; leading correction "correlated method errors (r_mat = 1 variant narrows ratios)" → "… narrows ratios **and
  resolves r = 0 ties (Migdal, NR edge 42-pool)**". This variant is family-wise (row 29), not VER-WP8-S-v2's global common mode; the qualitative findings agree.
- **Row 3 (statement (ii)).** Recomputed (S3-C15): survivors in the leading tier of two channels are Ge (ER floor, ER quanta), LiF (POL rate, Migdal) and GaAs (POL reach, Migdal).
  Replacement: **"(ii) Survivors in the leading tier of two channels, excluding the Migdal row (no reading): Ge (ER floor and ER quanta, both P = 1.000)."**
- **Row 4 (L-S3).** sympy (S3-C9): F′/F = [(Z′² + ΣZ_o²)/(Z² + ΣZ_o²)]·(n′/n)^{−3/2}; the density factor multiplies the **whole** FOM (NiO Ni 10 → 2: ×0.832, → 18: ×1.441; the
  "ion's term only" reading would give ×0.35). L-S3 chain text → "valence-convention shift ×[(Z′² + ΣZ_o²)/(Z² + ΣZ_o²)](n′/n)^{−3/2} on the whole FOM". L-S3 validity: append
  "X_pole ≥ 1 is a prior [E], not a bound (loss weight above ω_p gives X_pole < 1); the f-sum gives only the upper bound (π/2)ω_p²/E_g⁵".
- **Row 5 (tier count).** WP8-S-v2 §1.4 / S2-C4 "93 tiers": the v2 JSON had 111; v3 has **117** (7 channels × 2 pools; S2-C4).
- **Row 9 (R13).** As §4 (CsI never in the WP8-U-v3 §5 suspect list; now rejected on the floor).
- **Row 11 (Si ε_eh).** §1.3 "Si ε_eh ±0.01 as stated" was true of the text, not the code (σ 0.02). rank.py now uses the stated ±0.01 (68% width 0.0198 eV, S3-C8); no reading moves.
- **Row 12 (Ge vs Si cosmogenics).** WP8-S-v2 §4 ER-quanta row "Ge cosmogenics (³H 82, ⁶⁸Ge ≥ 74, ⁶⁵Zn 106 /(kg·d)) vs Si (³H 124) are within this factor" → **"Ge's listed
  activation sum (≥ 262 /(kg·d)) is ×2.1 Si's (124), above the 1.22 tolerance, so the background-limited order would reverse if these activities enter the ROI; in a < 1 keV
  ROI the listed K- and Ge/Zn L-lines fall outside and the ³H β tail (f_<1keV = 0.0892, both) plus the light-daughter L-lines (§10) and M-lines enter: ³H alone gives
  Ge/Si 0.66 (Ge favoured). The comparison is ROI- and exposure-dependent (S3-C14)."**
- **A-5 / B-1 / B-8 closing-table wording.** A-5 → "met for CaWO₄/Ge/GaAs (one tier on the measured CaWO₄ tensor); TeO₂ separates on the MC"; B-1 → "resolved (pairwise
  η-weighted window, §6)"; B-8 → "resolved (§15 specification)".

## 15. The L(k, ω) gap: computation specification (VER-WP8-S-v2 §D; WP8-S-v2 §6 item 1; `GAP:L_eps2_data`)
**What is computed.** The loss function L(k, ω) = Im[−1/ε(k, ω)] (the G = G′ = 0 element of ε⁻¹, CONVENTIONS §2) of each survivor, for |k| from 0 to ≈ 5 keV (covering the Migdal
soft-limit k ∈ 1BZ and the ER window) and ω from E_g to ≈ 5 ω_p^{val} (ω_p^{val} 15–30 eV), on a direction set sufficient for the angular average (cubic: 3 directions; uniaxial:
∥, ⊥ c and one oblique). Outputs: 𝓠_Mig,κ = ∫d³k Z_κ(k)²L(k, ω)/(3(2π)³ω⁴) and ∫𝓠dω per κ (replacing the pole prior X_pole), and w_acc⟨1/ω⟩ for ER. Explainable form: "how
strongly the electrons of the crystal absorb energy ω at momentum k", whose inverse-fourth moment sets the Migdal yield.
**Approximation level.** RPA with local fields (full ε_{GG′}, so that L = Im[−(ε⁻¹)₀₀] ≠ Im ε₀₀/|ε₀₀|²) on a DFT ground state with a scissor (or GW) gap matched to the measured
E_g; TDDFT-ALDA kernel as the cross-check rung (𝒳 rung of CONVENTIONS row 29: same-method nuisance, r_mat = 1). Semicore states included where they lie within 5 ω_p^{val}
of the gap (Ga 3d, Ge 3d, W 5p/4f, Pb 5d, Te 4d, Cs 5p, I 4d, Mo 4p).
**Method.** Plane-wave DFT (the COMP-PH layout of code/COMP-*: scf → nscf on a dense k-mesh) → independent-particle χ⁰_{GG′}(k, ω) with unoccupied bands to ≥ 5 ω_p^{val} above the
VBM → Dyson ε = 1 − v_Cχ⁰ (RPA) or with f_xc (TDDFT) → invert, take the 00 element at the unreduced k (k = k_r + G_k) → Lorentzian broadening δ.
**Convergence.** (i) f-sum: ∫ωL dω = (π/2)ω_p² to ≤ 2% with the counted electrons (valence + included semicore) — this also fixes the valence split used for Z_ion and n_e^{val}
(L-S3); (ii) bands until ∫L/ω⁴ changes < 1%; (iii) k-mesh doubling until ∫L/ω⁴ changes < 1%; (iv) G-vector cutoff of ε_{GG′} (local fields) until < 1%; (v) broadening
δ ≤ E_g/20, extrapolated δ → 0 (∫L/ω⁴ is weighted to the gap edge).
**Pitfalls.** (a) Missing semicore weight biases ∫L/ω⁴ low at fixed f-sum (weight moves to high ω); (b) the scissor shift moves the E_g⁻⁵-weighted onset — compare with the f-sum bound
(π/2)ω_p²/E_g⁵; (c) anisotropy: average over k̂, never take one direction; (d) the G = 0 element at |k| > q_BZ must use the unreduced-k convention (CONVENTIONS §2); (e) excitonic
weight below E_g (absent in RPA) adds to ∫L/ω⁴ — the BSE rung bounds it; (f) X_pole < 1 is possible (weight above ω_p), so the [1, 3] prior is not a bound.
Status: GAP with specification (CLOSED-AS-EXACT-GAP once accepted). Items 2–6 of WP8-S-v2 §6 are data fetches (source class in IF-S2-2/3); item 2 now reads "TeO₂, CsI".

---
## 16. Ranking (code/REV-WP8-S/rank.py v3 → data/ranking_v3.json; checks 31/31)
**Input changes vs v2:** CaWO₄ measured tensor (§3); CsI B-floor model (§4); Al measured tensor and ρ, YIG ρ (§13.2); diamond in the survivor pool (§13.1); Si ε_eh ±0.01 (§14);
sapphire σ 3% (§8); family-wise r_mat (§14); pairwise heavy window and light correction (§6–§7). Pool 42 = **11 SURVIVOR** + 31 SURVIVOR-COND.
### 16.1 r_mat variants (CONVENTIONS §13 row 29; P(first) for every material with P₁ ≥ 0.02 at some r)
Medians, 68% intervals and tiers do not depend on r (marginals are unchanged; one MC-noise boundary flip, γ-LiAlO₂ in Migdal-42, S3-C7); only joint probabilities move.
| Channel | Pool | Material (tier) | P₁ r=0 | r=0.5 | r=0.9 | r=1 |
|---|---|---|---|---|---|---|
| ER_edge | S | Ge (t1) | 1.000 | 1.000 | 1.000 | 1.000 |
| ER_edge | 42 | PbSe (t1) | 1.000 | 1.000 | 1.000 | 1.000 |
| ER_quanta | S | Ge (t1) | 1.000 | 1.000 | 1.000 | 1.000 |
| ER_quanta | 42 | PbTe (t1) | 0.467 | 0.492 | 0.534 | 0.722 |
| ER_quanta | 42 | PbSe (t1) | 0.437 | 0.459 | 0.465 | 0.278 |
| ER_quanta | 42 | PbS (t1) | 0.096 | 0.049 | 0.001 | 0.000 |
| NR_heavy | S | TeO2 (t1) | 0.951 | 0.983 | 0.986 | 0.986 |
| NR_heavy | S | Ge (t2) | 0.021 | 0.002 | 0.000 | 0.000 |
| NR_heavy | S | GaAs (t2) | 0.021 | 0.002 | 0.000 | 0.000 |
| NR_heavy | 42 | CsI (t1) | 0.974 | 0.977 | 0.982 | 0.984 |
| NR_edge | S | C (t1) | 1.000 | 1.000 | 1.000 | 1.000 |
| NR_edge | 42 | hBN (t1) | 0.606 | 0.723 | 0.956 | 1.000 |
| NR_edge | 42 | C (t1) | 0.241 | 0.201 | 0.043 | 0.000 |
| NR_edge | 42 | PE (t1) | 0.108 | 0.061 | 0.001 | 0.000 |
| NR_edge | 42 | cBN (t1) | 0.045 | 0.014 | 0.000 | 0.000 |
| POL_rate | S | LiF (t1) | 0.996 | 0.996 | 0.996 | 0.996 |
| POL_rate | 42 | LiF (t1) | 0.905 | 0.905 | 0.907 | 0.908 |
| POL_rate | 42 | SiO2-q (t2) | 0.076 | 0.078 | 0.078 | 0.077 |
| POL_edge | S | GaAs (t1) | 1.000 | 1.000 | 1.000 | 1.000 |
| POL_edge | 42 | CsI (t1) | 0.997 | 1.000 | 1.000 | 1.000 |
| Migdal | S | NaF (t1) | 0.322 | 0.378 | 0.531 | 0.987 |
| Migdal | S | Si (t1) | 0.287 | 0.315 | 0.357 | 0.013 |
| Migdal | S | LiF (t1) | 0.150 | 0.123 | 0.052 | 0.000 |
| Migdal | S | LiAlO2 (t1) | 0.123 | 0.096 | 0.034 | 0.000 |
| Migdal | 42 | NaCl (t1) | 0.494 | 0.649 | 0.933 | 1.000 |
| Migdal | 42 | PE (t1) | 0.185 | 0.145 | 0.043 | 0.000 |
| Migdal | 42 | NaI (t1) | 0.137 | 0.096 | 0.016 | 0.000 |
| Migdal | 42 | CsI (t1) | 0.112 | 0.074 | 0.008 | 0.000 |
Reading: at r = 1 a whole method family moves together, so ratios within it become exact and ties "resolve" — this resolution is only as good as the assumption that the method
error is common. The r = 1 values are therefore reported, not adopted, for the Migdal and NR-edge-42 rows.

### 16.2 Survivor-only ranking (11 SURVIVORs; medians [68%], tier, rank interval)
| Channel | Leader | Then (tiers) | Not ranked |
|---|---|---|---|
| ER floor (MeV) | **Ge 0.210 [0.208, 0.212]** t1, rank 1–1 | Si 0.333 (t2), GaAs 0.423 (t3), CaWO₄ 1.50, **C 1.56**, Al₂O₃ 2.52, NaF 3.29, LiF 4.06 | TeO₂, Li₂MoO₄, γ-LiAlO₂ (no measured E_g) |
| ER quanta (eV) | **Ge 3.37 [3.32, 3.42]** t1 | Si 3.72, GaAs 4.34, {TeO₂ 9.69, CaWO₄ 10.8}, C 13.1, {Al₂O₃ 16.7, NaF 20.7}, LiF 25.2 | Li₂MoO₄, γ-LiAlO₂ |
| NR heavy (×Si) | **TeO₂† 2.31 [2.12, 2.52]** t1, rank 1–1 | {CaWO₄ 1.90, Ge 1.82, GaAs 1.82} t2, NaF 1.46, {LiF, γ-LiAlO₂, Si}, Al₂O₃ 0.81, C 0.48 | Li₂MoO₄ |
| NR edge (keV) | **C 3.15 [2.90, 3.43]** t1, rank 1–1 (array caveats) | Al₂O₃ 5.16 (t2), {Si 6.29, γ-LiAlO₂ 6.80, LiF 7.38}, NaF 8.82, {CaWO₄ 11.0, GaAs 11.2, Ge 11.3}, TeO₂ 12.4 | Li₂MoO₄ |
| POL rate (meV cm³/g) | **LiF 19.0 [15.5, 23.3]** t1 | {NaF 9.72, Al₂O₃ 9.40} t2, GaAs 0.149 | Si, Ge, C (non-polar); TeO₂ (bound ≤ 5.88); CaWO₄, Li₂MoO₄, γ-LiAlO₂ |
| POL reach (keV) | **GaAs 9.94** t1 | NaF 14.2, LiF 22.0, Al₂O₃ 31.1 | as POL rate |
| Migdal (×Si pole) | no reading at r = 0 (max P₁ 0.32) | t1 {NaF, Si, LiF, γ-LiAlO₂, Li₂MoO₄, GaAs}; t2 {Ge, Al₂O₃, TeO₂, CaWO₄, C} | – |
| Light-mediator NR-1ph | no ranking (×1.08 spread; §7) | | |
**Statements.** (i) No material leads every channel; survivor leaders: Ge (ER floor, ER quanta), TeO₂ (heavy NR-1ph, S4-COND ¹²³Te, DB tensor), **C (NR edge; promoted by row 38,
array caveats)**, LiF (POL rate), GaAs (POL reach); no Migdal leader; no light-mediator ranking. (ii) Excluding Migdal, Ge is the only survivor in the leading tier of two channels.
(iii) Every Pb-salt lead is conditional (ε_eh [E] outside the validated range, SURVIVOR-COND screening, S4-COND ²¹⁰Pb). (iv) CsI's 42-pool heavy and reach leads rest on [E]
(ν) and on S1/S3 COND.

### 16.3 Final readings (machine-checked against data/ranking_v3.json by S2-C14; "S" = the 11 SURVIVORs; r=1 column = family-wise r_mat = 1; "–" = not an adjacent pair)
| # | Channel | Pool | Material | Quantity | Value (r=0) | r=1 | vs | Statement and flags |
|---|---|---|---|---|---|---|---|---|
| R1 | ER_edge | S | Ge | P_first | 1.000 | 1.000 | – | Ge has the lowest ER floor among survivors (0.210 MeV), measured gaps [FT] |
| R2 | ER_edge | S | Ge | P_pair | 1.000 | 1.000 | Si | Ge ≻ Si |
| R3 | ER_edge | S | Si | P_pair | 1.000 | 1.000 | GaAs | GaAs's room-T gap + [E] shift cannot close the gap to Si |
| R4 | ER_edge | all | PbSe | P_first | 1.000 | 1.000 | – | Pb salts hold the three lowest floors (COND; S4-COND ²¹⁰Pb) |
| R5 | ER_edge | all | Ge | P_pair | 0.988 | 0.998 | GaSb | **[E]-driven**: rests on GaSb's room→0 K shift |
| R6 | ER_quanta | S | Ge | P_first | 1.000 | 1.000 | – | **conditional** on the model-dependent 50 mK fit 3.37 eV |
| R7 | ER_quanta | S | Si | P_pair | 1.000 | 1.000 | GaAs | Si ≻ GaAs at T_op |
| R8 | ER_quanta | all | PbTe | tier | 1 | 1 | – | PbTe, PbSe, PbS one tier and lead: **[E]**, GAP-EF outside its validated range |
| R9 | ER_quanta | all | PbTe | P_pair | 0.516 | 0.722 | PbSe | unresolved at r = 0; r_mat-driven |
| R10 | NR_heavy | S | TeO2 | P_first | 0.951 | 0.986 | – | TeO₂ alone in tier 1 (DB tensor, ρ proxy, S4-COND ¹²³Te); window 0.063–0.33 MeV (f.u.) / 0.063–0.25 (prim) |
| R11 | NR_heavy | S | TeO2 | P_pair | 0.987 | 0.986 | CaWO4 | CaWO₄ on its measured tensor drops to tier 2 (v2: one tier on the proxy) |
| R12 | NR_heavy | S | CaWO4 | tier | 2 | 2 | – | CaWO₄, Ge, GaAs one tier (A-5's single tier restored for these three) |
| R13 | NR_heavy | S | Ge | P_pair | 0.503 | 1.000 | GaAs | Ge ≡ GaAs at r = 0; the r = 1 value is the common-DB-tensor artefact (same method), not a resolution |
| R14 | NR_heavy | all | CsI | P_first | 0.974 | 0.984 | – | **[E]-driven**: B-floor model (B [FT, secondary], ν [E]); holds for ν ≳ 0.01; window 0.104–0.27 MeV |
| R15 | NR_heavy | all | CsI | P_pair | 0.984 | 0.984 | Bi2Se3 | CsI ≻ Bi₂Se₃ on the floor-respecting model |
| R16 | NR_edge | S | C | P_first | 1.000 | 1.000 | – | diamond (promoted by row 38) has the lowest survivor NR edge, 3.15 keV (DB tensor); array caveats §13.1 |
| R17 | NR_edge | S | C | P_pair | 1.000 | 1.000 | Al2O3 | replaces the v2 reading "sapphire leads" |
| R18 | NR_edge | S | Al2O3 | P_pair | 0.951 | 1.000 | Si | sapphire second |
| R19 | NR_edge | all | hBN | P_first | 0.606 | 1.000 | – | h-BN, C, PE, c-BN one tier at r = 0; h-BN resolves only at r = 1 (common DB family); h-BN, PE directional |
| R20 | POL_rate | S | LiF | P_first | 0.996 | 0.996 | – | Z* route on FT DFT inputs |
| R21 | POL_rate | S | LiF | P_pair | 0.996 | 0.996 | NaF | LiF ≻ NaF |
| R22 | POL_rate | S | NaF | P_pair | 0.587 | 0.582 | Al2O3 | tie (sapphire width now 3%) |
| R23 | POL_rate | all | LiF | P_first | 0.905 | 0.908 | – | the rest is mostly SiO₂-q's (8.1) interval |
| R24 | POL_edge | S | GaAs | P_first | 1.000 | 1.000 | – | the reach reverses the rate order |
| R25 | POL_edge | all | CsI | P_first | 0.997 | 1.000 | – | soft polar lattice; CsI S1/S3 COND |
| R26 | Migdal | S | NaF | P_first | 0.322 | 0.987 | – | **no Migdal reading at r = 0** (max 0.32); at r = 1 (common X_pole) NaF 0.987: r_mat- and GAP-driven |
| R27 | Migdal | S | NaF | P_pair | 0.524 | 0.987 | Si | r_mat-driven |
| R28 | Migdal | all | NaCl | P_first | 0.494 | 1.000 | – | 0.49 at r = 0, 1.000 at r = 1: r_mat- and GAP-driven |

### 16.4 Next-target guide (full 42-pool; S1–S4 status is a column, not a filter)
For each channel, the leading materials of the whole pool (P₁ at r_mat = 0, rank 68% interval), what is still missing to make each a next-generation target, and the one measurement
that would most change its rank. Screens: P = PASS, C = COND, F = FAIL (v4 table + row 38). "Array" = row-38 array route.
| Channel | Material | P₁ (rank 68%) | S1/S2/S3/S4 | Missing demonstration | Single most rank-changing measurement |
|---|---|---|---|---|---|
| ER floor | PbSe | 1.000 (1–1) | C/C/C/P (+²¹⁰Pb cond.) | ≥ 0.1 g crystal with mK readout; ²¹⁰Pb ≲ 1.5 mBq/kg in the lead used | a(²¹⁰Pb) of available low-background lead (decides whether the floor lead is usable) |
| ER floor | PbTe, PbS | 0 (2–2, 3–3) | PbTe P/C/C/C; PbS C/C/C/P | as PbSe; PbTe EC limit (S4) | as PbSe |
| ER floor | Ge (survivor) | 0 (4–4) | P/P/P/P | – | low-T gap of GaSb (decides Ge vs GaSb, R5) |
| ER quanta | PbTe, PbSe, PbS | 0.47, 0.44, 0.10 (1–3) | as above | as above; ε_eh is GAP-EF [E] outside its validated range | a measured ε_eh (pair energy) of one Pb salt at mK |
| ER quanta | GaSb | 0 (4–5) | C/P/C/P | mK operation (S1), phonon readout (S3) | low-T gap and measured ε_eh |
| NR heavy | CsI | 0.974 (1–1) | C/P/C/P | mK operation of a CsI crystal (hygroscopic, S1); direct TES readout (S3, remote-TES route) | **measured C_ij of CsI** (fixes ν; the 1910.10716 value is rejected) |
| NR heavy | Bi₂Se₃, NaI | 0.015, 0.009 (2–4) | C/P/C/P | Bi₂Se₃: mK operation, readout; NaI: direct TES (remote-TES route) | measured C_ij (both rest on DB tensors) |
| NR heavy | TeO₂ (survivor) | 0.951 in S (6–8 in 42) | P/P/P/C (¹²³Te) | ¹²³Te EC background below budget | measured C_ij of TeO₂ (DB tensor, ρ proxy) |
| NR edge | h-BN | 0.606 (1–2) | C/F/C/– | ≥ 0.1 g crystals (S2 FAIL even as an array: mm-scale); mK operation; readout | measured C_ij (DB tensor, stiff-axis-only edge) |
| NR edge | C (diamond, survivor) | 0.241 in 42; 1.000 in S (1–3) | P/P (array)/P/P | array of ≥ 6 × 0.175 g with per-crystal thresholds; LEE per crystal | measured C_ij (DB tensor; separates C from h-BN/PE/c-BN at r = 0) |
| NR edge | PE, c-BN | 0.108, 0.045 (2–4) | PE C/C/F/–; c-BN C/F/C/– | PE: any phonon readout (S3 FAIL); c-BN: ≥ 0.1 g crystals | measured C_ij |
| POL rate | LiF (survivor) | 0.905 (1–1) | P/P/P/P | – (⁶Li(n,α)³H activation is an open background) | measured ε₀ of LiF (DB ε₀ fails V2; Z* route is DFT) |
| POL rate | SiO₂-q | 0.076 (2–12) | C/P/C/P | mK operation (S1), readout (S3) | mode-resolved ω_T,min / ω_L of α-quartz (collapses the (8.1) interval) |
| POL reach | CsI | 0.997 (1–1) | C/P/C/P | as NR heavy | measured ω_LO of CsI at low T |
| POL reach | MgF₂ | 0.003 (2–2) | C/P/C/P | mK operation, readout | lowest LO frequency (currently ω_O,min, a lower estimate) |
| Migdal | NaCl | 0.494 (1–4) | C/C/C/P | encapsulated mK operation (hygroscopic), crystal mass with readout, purity | **L(k, ω) of NaCl** (§15: replaces X_pole; r_mat-driven at present) |
| Migdal | PE, NaI, CsI | 0.185, 0.137, 0.112 (1–10) | as above | as above | L(k, ω) (or measured EELS) |
| Light NR-1ph | – | – | – | no ranking (target-independent above (1 + κ_η)m_min^{ac}) | – |

---
## 17. Owed corrections (exact texts; the merger applies them, nothing here is edited in place)
### 17.1 LIMITS.md
- **L-F1 (l.183)**, Validity: "heavy mediator ∝ 1/c_NR1 only for 0.1 ≲ m_χ ≲ q_BZ/2v_max (Si 0.43 MeV)" → **"heavy mediator ∝ 1/c_NR1 for a pair of materials when
  m_χ ≳ 4.2 m_min^{ac}(c_NR1) of the softer one and m_χ ≲ q_BZ/(2v_max) of the heavier cell (ω_th = 1 meV: survivors 0.063–0.33 MeV f.u. / 0.063–0.25 MeV primitive;
  WP8-errata §6); m_min^{ac} of (2.3b) is the kinematic edge"**; Status: append "; window corrected R17 (ERR-WP8)".
- **L-F2 (l.184)**, Validity: "lossless factorised ε per principal axis **with ε_∞, ε₀ of that axis and model and ω ≥ ω_L,max**" → "lossless factorised, **interlacing** ε per principal
  axis with ε_∞, ε₀ of that axis and model and ω ≥ ω_L,max; **the ω_L,max form only with mode data (consistency statement); ε-only materials ranked by the (8.1) interval**".
- **L-F4 (l.186)**, Leading correction: → "O(m_min^{ac}/m_χ): factor 1 − (1 + κ_η)m_min^{ac}/m_χ, κ_η = 3.14 (SHM), dominant within ≈ 30× the softer edge; above m_hi the band-top
  term ω_th/(c q_BZ); η c-shift O(c²/v₀²)"; Status: append "; first-order correction DERIVED R17 (S3-C5)".
- **L-H2 (l.248)**, Leading correction: append "; grid commensurate with E_g, θ_iiE_g, ω₀ (else ω₀,eff = h·round(ω₀/h), −1.6% on N̄ at h = 0.02; CW7-C5c)".
- **L-H4 (l.250)**, Leading correction: "O(1/S): one-magnon weight defect ΔS/S (C14b)" → "O(1/S): transverse sum-rule defect ΔS/S (C14b), a lower estimate [E] of the one-magnon defect".
- **New rows (WP8-S block, proposed numbers):** L-S1 | WP8-S | WP8-F-v3 §5.1 scalars × provenance widths → MC → P(first), rank intervals, interval-order tiers | WP8-S-v2 + WP8-errata;
  code/REV-WP8-S v3 | family-wise r_mat ∈ {0, 0.5, 0.9, 1} (CONVENTIONS row 29); one scalar per channel in its validity window (pairwise window for NR heavy) | [E] widths of the
  DB families; correlated method errors (r_mat = 1 narrows ratios and resolves r = 0 ties: Migdal, NR edge 42-pool) | CROSS-CHECKED (S2-C6) |
  L-S2 | WP8-S | interval order on 68% intervals → tiers as heights | order theory [D] | any family of intervals; correlation-blind | choice of 68% | DERIVED (S2-C4) |
  L-S3 | WP8-S | (2.7′) + plasmon pole with one Z_ion/n_e^{val} split → shift ×[(Z′² + ΣZ_o²)/(Z² + ΣZ_o²)](n′/n)^{−3/2} on the whole FOM | WP8-F-v3 §2.7 | pole-dominated L;
  small-k Z_ion; X_pole ≥ 1 a prior [E] | interband weight ≤ (π/2)ω_p²/E_g⁵ (f-sum) | DERIVED for the scaling (S3-C9); ranking GAP |
  L-EW1 | WP8-U | cubic Rayleigh bound ρc_qL² ≥ q̂·Γ·q̂ ≥ B → c_LA ≥ √(B/ρ) | internal [D]; B [FT cond-mat/9408044 p.18, secondary] | cubic, Born-stable | anisotropy enters only above the floor | DERIVED (S3-C2) |
### 17.2 NOTATION.md (append to "Rows added R17")
| Symbol | Meaning | Source |
|---|---|---|
| r^M_mag (note on l.767) | status: [D] as the LSWT transverse sum-rule defect ΔS/S; [E] (lower estimate) as the one-magnon width | WP8-errata §9 |
| κ_η | (u₊/η₀)∫₀^{u₊}(η₀ − η(u))u⁻²du, light-mediator first-order constant; 3.14 for the CONVENTIONS §8 SHM | WP8-errata (EW-7.1) |
| m_on, m_hi, W_AB | heavy-mediator 1/c onset (≈ 4.2 m_min^{ac}(c_NR1)), upper end q_BZ/(2v_max), pairwise window | WP8-errata §6 |
| Z_prim | formula units per primitive cell (q_BZ,prim = q_BZ,fu/Z_prim^{1/3}) | WP8-errata §6 |
| P₁, P(A ≻ B), rank_68, tier, X_pole | as WP8-S-v2 "Symbols"; tier = height in the interval order (correlation-blind) | WP8-S-v2, WP8-errata §14 |
| ω₀,eff | h·round(ω₀/h), the phonon step a non-commensurate cascade grid actually uses | WP8-errata §5 |
| ν_CsI | Poisson-ratio band of the CsI B-floor model, U[0.20, 0.35] around the Cauchy 1/4 [E] | WP8-errata §4 |
### 17.3 state/CORRECTIONS.md
- **§19.13 (WP8-U) new rows:** (a) "v4 `screen_S1` rows: dropped non-[E] rows are GaAs S1 and SiO₂-q S1 (not 'two GaAs rename rows')" | W | WP8-errata §2; (b) "§0 row 10 /
  build_v4.py: cyclic shear mis-indexing text of WP8-errata §1; CW7-C33 tolerance 0.11 → 0.05" | W; (c) "v4 `cosmo_EC_lines_subkeV` (Ge): replacement of WP8-errata §10" | S;
  (d) "§0 row 7, §5: 1910.10716 c_LA ratings of WP8-errata §12 (CsI CONFIRMED inconsistent)" | S; (e) "CaWO₄, CsI `c_LA` rows superseded for ranking by WP8-errata §3–§4; add
  `C_ij_exp` CaWO₄ [FT 2508.08858 p.16] and `B_exp` CsI 13.5 GPa [FT cond-mat/9408044 p.18]" | S; (f) "C (diamond): `screen_S2` PASS and `verdict` SURVIVOR under CONVENTIONS row 38
  [FT 2310.05815]; array caveat row" | S; (g) "Al, Ir, YIG: state/DATA-ADDENDA.csv supersedes v4 Al tensor-derived rows (`c_L_iso`, `c_T_iso`), ρ-derived rows (`n_e_val`, free-electron
  rows), christoffel_v4 Al/Ir entries, YIG `a_exp`, `rho_T_from_a_exp`, `n_e_val`, 𝓃_spin (×1.045)" | S.
- **§19.14 (WP8-F) new rows:** heavy window (§6 text) at §0, §2.3(a″), §5.1, L-F1 | S; light-mediator correction (EW-7.1) at §0, §2.3(a″), §5.1, L-F4 | S; ε-route (§8 text) at §2.5,
  IF-ERR7-1, IF-F1′, L-F2 | S; r^M status (§9 text) at §2.6, §4 | W.
- **§19.15 / CW7-errata rows:** §1.1 (dropped rows), §1.4 (commensurate-grid pitfall), §1.7 (r^M), §1.11 (EC lines), §1.12 (G-F6 spec of WP8-errata §11) | S/W.
- **New §19.18 WP8-S (returns/R16/WP8-S-v2.md):** "read through WP8-errata: §0 rows 3–5, 8; §1.3 (r_mat wording, Si ε_eh, sapphire width); §1.4 (117 tiers); §2.3 (window, CaWO₄,
  CsI, R10, R13); §2.4 (NR edge: C leads S, Al₂O₃ second); §4 ER-quanta row; §5 (readings replaced by WP8-errata §16.3; statement (ii)); §6 item 1 (spec §15), item 2; L-S1–L-S3
  (§17.1). code/REV-WP8-S/data/ranking_v3.json supersedes ranking_v2.json." | S.
- **New interface row (GAP-EF, IF-EW-1):** "code/GAP-EF(-v2)/cascade.py runs at ω₀,eff = h·round(ω₀/h): rerun on commensurate grids (Si case +1.3% in ε_eh at h = 0.02)" | W.

## 18. Checks
**code/CW7/checks.py — 41/41 PASS (19 s):** C5, C5b, C8 on h = 0.002; **C5c** (MC vs commensurate solver; guard; old bias −1.61%); **C7** (F 0.1139, ε/E_g 3.2185; quantised +1.3%).
**code/REV-WP8-S/checks.py — 31/31 PASS (4.5 s)** (run `python3 rank.py` first; it writes ranking_v3.json with the r_mat variants):
| # | Tests |
|---|---|
| S2-C1…C12 | as v2, on v3 (pool 42 = 11 S + 31 C; tiers recomputed from ranking_v3.json; light spread < 1.10) |
| S2-C13 | the orderings stated in §16 (TeO₂ alone t1 S; CaWO₄/Ge/GaAs t2; CsI leads 42 heavy; C leads S NR edge; …) |
| S2-C14 | the 28 rows of §16.3 equal the run (r = 0 to 0.006; r = 1 column to 0.01) |
| S2-C15 | CW7 ranking.json and ranking_v2.json byte-unchanged (md5); runtime |
| S3-C1 | CaWO₄ measured tensor: pos. def., c_NR1 4.58, 1910 c_LA below LA min |
| S3-C2 | CsI floor (sympy), Cauchy ν = 1/4 (sympy), 1910 value below the floor |
| S3-C3 | DATA-ADDENDA: Al tensor and ρ, YIG ρ used |
| S3-C4 | heavy window: both referees' numbers reproduced; onset/m_min^{ac} ≈ 4.2; common windows |
| S3-C5 | light-mediator first order (sympy); VER-ERR-CW7 sequence reproduced; κ_η = 3.14 |
| S3-C6 | 𝓘 ∝ 1/ε_∞ (sympy residues); sapphire width ≥ 3%; ε-only entries on (8.1) |
| S3-C7 | r_mat variants: tiers and medians r-independent; P₁ moves; ties resolve at r = 1 |
| S3-C8 | Si ε_eh width = stated ±0.01 |
| S3-C9 | L-S3 factor (sympy); NiO ×0.832/×1.441 |
| S3-C10 | dropped non-[E] rows = GaAs S1, SiO₂-q S1 |
| S3-C11 | PE cyclic shift; C33 identity ≤ 0.05 GPa |
| S3-C12 | Ge EC L-lines < 1 keV for Ti…Fe daughters (E_L/E_K trend, 1607.04560 Table 1) |
| S3-C13 | G-F6 isotope list generated (⁴³Ca in CaWO₄) |
| S3-C14 | Ge vs Si cosmogenics ×2.11 > 1.22; ³H-only 0.66 |
| S3-C15 | 117 tiers; statement (ii) sets |
| S3-C16 | row 38: only C promoted; C leads the survivor NR edge |

## 19. Closing table (verifier item → resolution → location)
| Verifier item | Resolution | Location |
|---|---|---|
| VER-ERR-CW7 0a / RC1 | PE cyclic-shift wording; C33 max 0.050 GPa, tolerance text owed | §1; S3-C11; §17.3 |
| 0b, 1.1 / RC2 | dropped non-[E] rows = GaAs S1, SiO₂-q S1 | §2; S3-C10 |
| 0c-ii, 1.4 / RC3 | cascade_gf.py guard + commensurate_h; checks rerun; pitfall text; GAP-EF flag | §5; CW7-C5, C5b, C5c, C7, C8 |
| 0d-i / RC4 (light) | (EW-7.1) with κ_η = 3.14; L-F4, §0 texts | §7; S3-C5 |
| 0d-ii / RC4 (heavy) | pairwise η-weighted window; both referees reconciled; L-F1, §0, §2.3, §5.1 texts | §6; S3-C4 |
| 0d-iii / RC5 | (8.1) interval for ε-only materials; interlacing; damping [E] | §8; S3-C6 |
| 1.7, 1.14 / RC6 | r^M [D] sum-rule defect, [E] width; L-H4 | §9 |
| 1.11 / RC7 | light-daughter L-lines inside the ROI | §10; S3-C12 |
| 1.12 / RC8 | isotope list generated (⁴³Ca), projected DOS, normalisation, e^{−2W} | §11; S3-C13 |
| 2a / RC9 | GaN, AlN, ZnO CONFIRMED; plus CsI CONFIRMED, CaWO₄ marginal | §12 |
| RC10 | content may move to VERIFIED after R×2 of this errata; no SURVIVOR verdict reversed by the referee corrections | §0; IF-EW-6 |
| L-H2, L-F1, L-F2, L-F4, L-H4 (§G) | exact texts | §17.1 |
| VER-WP8-S-v2 row 1 / B-1 | window ≈ 0.063–0.33 (S), 0.104–0.27 MeV (42), both q_BZ conventions | §6 |
| row 2 | r_mat variants 0/0.5/0.9/1 family-wise; wording; tiers correlation-blind | §14, §16.1; S3-C7 |
| row 3 | statement (ii) "excluding Migdal" (Ge only) | §14, §16.2; S3-C15 |
| row 4 | L-S3 factor on the whole FOM | §14, §17.1; S3-C9 |
| row 5 | tier count 117 (v2 text 93, JSON 111) | §14; S2-C4, S3-C15 |
| row 8 | sapphire σ 3% | §8; S3-C6 |
| row 9 | CsI: rejected below the floor; B-floor [E] model; R13 rephrased | §4; S3-C2 |
| row 10 (conditional) | CaWO₄ on measured C_ij: tier 2 | §3; S3-C1 |
| row 11 | Si ε_eh ±0.01 in code | §14; S3-C8 |
| row 12 | Ge/Si cosmogenics ×2.1 > 1.22; ROI-dependent | §14; S3-C14 |
| §C A-5, B-1, B-8 | wording | §14 |
| §D (scope 4) | L(k, ω) specification | §15 |
| §E L-S1, L-S3 (X_pole [E]) | texts | §14, §17.1 |
| Coordinator: DATA-ADDENDA | Al, YIG used; Ir not in pool; untouched superseded rows listed | §13.2; S3-C3; §17.3 |
| Coordinator: CONVENTIONS row 38 | diamond promoted (only one); NR-edge survivor leader Al₂O₃ → C; array caveats | §13.1; S3-C16 |
| Coordinator: next-target guide | full-pool table with screens as a column and the most rank-changing measurement | §16.4 |
| Brief 3 (ranking) | rank.py v3, ranking_v3.json, variants, readings, checks 31/31 | §16, §18 |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-EW-1 | GAP-EF | cascade.py ω₀ quantisation (Si +1.3% in ε_eh) | rerun on commensurate grids |
| IF-EW-2 | WP8-U | v4 rows of §17.3 (a)–(g) (diamond verdict, CsI/CaWO₄ elastic data, Al/YIG supersessions, EC lines) | add rows (v5) |
| IF-EW-3 | literature agent | primary Farley & Saunders 1972 (CaWO₄ C_ij, T); measured C_ij of CsI, TeO₂, diamond; low-T gaps GaAs, GaSb | fetch |
| IF-EW-4 | COMP | L(k, ω) per §15 | run |
| IF-EW-5 | coordinator | LIMITS, NOTATION, CORRECTIONS texts of §17 | merge |
| IF-EW-6 | referees | R×2 of this errata and code/REV-WP8-S v3 | launch |

## Symbols introduced/used
New: κ_η, m_on, W_AB, Z_prim, ω₀,eff, ν_CsI (§17.2). Used: c_NR1, c_LA,max, m_min^{ac}, m_hi, η, v_max, 𝓘_pol, ε_∞, ε₀, ω_L, ω_T, r^M_mag, ΔS, W_⊥, P₁, rank_68, tier, X_pole,
r_mat, ε_eh, F_eh, ω₀, θ_ii, h, N_z (NOTATION v4 and the R16 returns' tables).
