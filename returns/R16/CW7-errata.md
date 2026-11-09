# R16 / CW7-errata: verification corrections to returns/R16/CW7.md (with WP8-U-v3, WP8-U-table-v4, WP8-F-v3)

Agent ERR-CW7, brief briefs/R16/ERR-CW7.md. **Read together with returns/R16/CW7.md, which is not edited.** Every item below that a verifier row
touched supersedes the CW7 text it names; every CW7 item not named here stands as written. Read: CW7.md (all), referees/R16/VER-CW7.md (all),
REF-WP8-S-A.md, REF-WP8-S-B.md, WP8-U-v2.md, WP8-F-v2.md, the v3 CSV, code/CW7/* (all), CONVENTIONS (§1–§14, R8/R13 amendments), NOTATION v4
(greps for every symbol introduced here), WP0-v3 (3.3)–(3.6), WP4-v3 K34 and I12, WP6-v3 §5.2 (l.448–451), GAP-EF §1.6 and (K1).
**Literature** (lit.py into literature/papers-ERR-CW7/, PDFs and HTML deleted, pdftotext `.txt` kept; page = PDF page): 1910.10716 (Eq. (35) p.9,
Eqs. (36)–(37) p.9–10, Table II p.12), 1908.06755 (p.4, p.11), 1607.04560 (p.3, p.10). Other sources are quoted from the CW7 and VER-CW7 reads.
**Deliverables.** This file; returns/R16/WP8-U-v3.md, WP8-U-table-v4.csv, WP8-F-v3.md (standalone; they supersede the R16 v2 files);
code/CW7/cascade_gf.py (fixed), build_v4.py (new), checks.py (revised, **40/40 PASS, 5–25 s**), data/v4_changes.json, christoffel_v4.json,
coverage_v4.json. `rank.py` and CW7 §12 are untouched (the WP8-S ranking is revised by a separate agent; see §5). Nothing was committed.
No heavy numerics: every number is [E] from tagged inputs or [D], computed in checks.py.

---
## 0. Verdict map
| VER row | Verdict | Resolution here | Section |
|---|---|---|---|
| V1 WP8-U-v2 + table v3 | STANDS WITH CORRECTION | applied: v4 table (55 [E] rows: 44 retagged, 11 dropped with 2 more superseded rows; 13 keys unique), TeO₂/γ-LiAlO₂ ρ proxy flag, V1–V6, CaWO₄ ³H | §1.1; WP8-U-v3 |
| V2 WP8-F-v2 | STANDS WITH CORRECTION | applied: A-§E(c) as asked (C23), A-§E(a) for S_LO (C21), C20 withdrawn as cross-check, one r^M, 𝓡/ℛ | §1.2; WP8-F-v3 |
| V3 Theorem G8′ | STANDS WITH CORRECTION | (iv) lab frame; (c) (H4) on {φ > 0}; C3, C4 replaced | §1.3 |
| V4 LE-153 | STANDS WITH CORRECTION | solver fixed (ΣP = 1 at θ_ii = 3/2, 2); (CW7-153b) reworded; spec completed (asymmetric DOS) | §1.4 |
| V5 LE-154 | **FALLS (as stated)** | re-derived: (CW7-154′) with max([A_X+]_−, [A_X0]_−); counterexample in C11 | §1.5 |
| V6 LE-155 | STANDS WITH CORRECTION | one-body sum rule, divergent for Coulomb V; exact replacement check; full 𝒟^γ in the polar term; n_e row v_DM/v_e | §1.6 |
| V7 LE-156 | STANDS WITH CORRECTION | r^M = ΔS/S **derived** (Casimir sum rule, C14b); σ_ln defined; WP4 text rewritten | §1.7 |
| V8 LE-157 | STANDS WITH CORRECTION | "cites I12 but not its directives"; mask from the KK-∞ column, y_mask = 3.8; one C.L. convention | §1.8 |
| V9 LE-160 | STANDS WITH CORRECTION | signed-elasticity rule derived (C16); row 29 re-issued | §1.9 |
| V10 LE-176 | STANDS WITH CORRECTION | PbTe 2.8–5.6%, PbS 10.3%, χ⁻¹ a fit parameter, "unusable" withdrawn for PbS/PbSe; C18 replaced | §1.10 |
| V11 LE-177 | STANDS WITH CORRECTION | CaWO₄ ³H inferred; Ge L-lines above the ROI; Geant4 convergence target | §1.11 |
| V12 WP8-F derived changes | STANDS | unchanged | – |
| V13 owed corrections | STANDS WITH CORRECTION | all re-issued or marked unchanged | §2 |
| V14 status upgrades | STANDS | unchanged | – |
| V15 G-F6 | STANDS WITH CORRECTION | spec rebuilt: incoherent SD response, two missing steps | §1.12 |
| V16 LIMITS rows | STANDS WITH CORRECTION | L-H1, L-H2, L-H3, L-F3 re-issued (+ L-F1, L-F2 from the REF-WP8-S findings) | §2.3 |
| §F checks | – | tautological checks replaced, tolerances tightened, C5b, C12b, C12c, C14b, C33–C36 added | §4 |

---
## 1. Item-by-item corrections
### 1.1 V1 — WP8-U-v2 and table v3 (VER-CW7 §A)
- **[E] screening evidence (A-G8 / B-(e)(ii)).** Of the 55 `screen_S*` rows with "[E]" evidence, 11 belong to the 13 duplicated keys and are dropped
  (with the 2 non-[E] GaAs rename rows superseded by the [FT] rows); the other 44 are retagged in v4: "[E]" → "[UNVERIFIED]", tag UNVERIFIED, and a
  PASS/FAIL that rested on [E] alone reads COND (the one rule of WP8-U-v2 §2, now applied in the table). Al₂O₃ S2 keeps PASS on its [ABS 1704.04320] item.
  No SURVIVOR verdict changes (every flipped cell belongs to a SURVIVOR-COND, EXCLUDED-RADIO or REFERENCE material). CW7-C29.
- **13 contradictory keys.** v4 keeps for every (material, screen_S*) key the last superseding row and drops the rest (listed verbatim in
  code/CW7/data/v4_changes.json); the `verdict` column now carries the final verdict on every row (158 cells changed, e.g. NiPS₃ EXCLUDED → SURVIVOR-COND).
  Rule for every other property, stated in WP8-U-v3 §0: **the last row with a "supersedes" note wins**.
- **B-(e)(v) TeO₂ ρ.** `flag_rho_T_DFT_proxy` rows for TeO₂ and γ-LiAlO₂ (both ρ_T from the OptB88vdW cell); WP8-U-v3 §4.1 prints "5.92ᵈ (DFT proxy)".
- §0 row 8 "V1–V5" → "V1–V6". CaWO₄ `cosmo_identified` corrected in place (§1.11).
### 1.2 V2 — WP8-F-v2 (VER-CW7 §A)
- **A-§E(c) as requested.** Per-branch light-mediator weight K_ν(m_χ) ≡ ∫_{q₋}^{q₊}(dq/q)η(v_min(q, ω_Lν)) with the CONVENTIONS §8 SHM, sapphire branches 48 and
  112.4 meV: K(48)/K(112.4) = **13.3 at 2×** and **5.5 at 3×** the 112-meV edge (2ω/v_max² = 32 keV), 1.41 at 1 MeV (the ln-ratio estimate gives 1.18).
  The band-uniform reading 𝓡_pol ∝ 𝓘_pol fails by an order of magnitude near the edge (CW7-C23). WP8-F-v3 §2.5.
- **A-§E(a) for S_LO itself.** (2.3c) is now derived, not only its angle average: two-site cell, c_κ = A_κ = M_κ/m_p, LO eigenvector (√(M₂/M), −√(M₁/M)),
  amplitude (q/m_p)√(M₁M₂/M)(1 − e^{iq·r₂}); the O(q²) term cancels identically and the O(q⁴) term is 2205.02250 Eq. (31) (CW7-C21, sympy).
- **C20 is not a cross-check of (2.7′).** Withdrawn as such; L-F3 cites the R14 referees' recomputation (REF-WP8-F-A F14, REF-WP8-F-B §4(ii)) and C20 now
  tests the plasmon-pole 𝓠_Mig (§2.3 of WP8-F-v3).
- **MAG nuisance.** One width: **r^M = ΔS/S** in both WP8-F-v3 §4 and the WP6 row (§1.7).
- **𝓡 vs ℛ (REF-B §9).** WP8-F-v3 Symbols: ℛ is a physical rate (events per mass per time); 𝓡_a is the material functional at fixed |𝒱_a(q₀)|², ℛ = C_χ𝓡_a σ̄.
### 1.3 V3 — Theorem G8′ (VER-CW7 §B1)
Replacement statements (the proof of (i)–(iii) stands as written):
- **(iv)** "If, **in the lab frame**, 𝔎_i depends only on |v| (hypothesis (I)) and φ(v) = Θ(|v| − u₀)/|v| with F the **lab-frame** velocity measure, then for one bin
  Φ_max = N_i^{up}/inf_{v≥u₀}𝒜_i(v)." In the galactic frame the kernel depends on |w − v_E(t)|; CW7-C4 now shows the galactic-|w| weight misses N/inf𝒜 by 12.9%.
- **(c)** "a modulation amplitude with signed φ: (ii) holds by weak duality and (iii) holds, **provided (H4) holds on {φ > 0}**; otherwise Φ is unbounded
  (mass can be placed where φ > 0 and no bin sees it)."
- **Checks.** C3 now tests the semi-infinite statement: the coarse-grid dual is infeasible on a nested refined grid (scale 1.063), the scaled coarse dual
  certifies the refined optimum, and one column-generation round raises the coarse optimum monotonically to the refined value (609.50 ≤ 612.10 ≤ 612.10 ≤
  648.08). The computation specification stands (VER: sufficient). Novelty stays UNRESOLVED.
### 1.4 V4 — LE-153 (VER-CW7 §B2)
- **Code defect (blocking for the spec): FIXED.** `CascadeGF.solve_gf` now forms C2, C3 for q < n_th − n_G before the main loop (those f = ρ are final,
  G = 1). Reproduced first: the R16 solver gave ΣP = 0.9529 and mean 1.970 vs 2.096 at θ_ii = 3/2 (λ 3.55, w 0.054, X 8, h 0.02). Fixed: ΣP − 1 = −3×10⁻¹⁶,
  mean 2.095629 = moment recursion at θ_ii = 3/2 and 2 (CW7-C5); seeding at θ_ii = 3/2 (C8); Richardson ε_eh/E_g = 2.0561 at θ_ii = 3/2, λ → 0 (GAP-EF (K1):
  2.056, C6). moments_fast was not affected (m = 0 below threshold).
- **(CW7-153b) replacement:** "P(N) = N_z⁻¹Σ_kz_k^{−N}·(·)(z_k) returns Σ_{j≥0}P(N + jN_z); it is exact **iff P(N′) = 0 for N′ ≥ N_z**, so N_z ≥ N̄ + 8σ_N
  (the aliased tail is then < 10⁻¹⁰ for the near-Gaussian P of property (c))." CW7-C5b: at N_z = 4 the DFT equals the aliased sum to 3×10⁻¹⁷ while P(N ≥ 4) = 0.002.
- **Specification completed.** The coded solver is the symmetric case ρ_e = ρ_h (one table 𝔊). General case: two coupled tables,
  𝔊_e = p_e z ⟨𝔊_e𝔊_e𝔊_h⟩_e + (1 − p_e)𝔊_e(x − ω₀), 𝔊_h likewise with e ↔ h, ⟨·⟩_t = [(ρ_t𝔊_t)*(ρ_t𝔊_t)*(ρ_t̄𝔊_t̄)](x − E_g)/Φ_t; cost ×2. Convergence
  criteria: h-Richardson (C6: O(h)), N_z doubling until max|ΔP| < 10⁻¹⁰, X doubling until the matched-Gaussian tail changes P by < 10⁻⁶. Pitfall added:
  for θ_ii > 1 every convolution below the ii threshold must be formed (the R16 defect). The "5 θ values × 27 survivors" run is now valid with the fixed code.
- L-H2 leading correction: re-issued (§2.3).
### 1.5 V5 — LE-154 FALLS as stated; corrected bound [D] (VER-CW7 §B3)
**Re-derivation.** With A_tot = A_X0 + A_X+ ≥ 0, P ∈ [0, 1] and ΔP ≡ P_X+ − P_X0:
- where ΔP ≥ 0: Σ_ΛA P = P_X0A_tot + ΔP·A_X+ ≥ −ΔP[A_X+]_−;
- where ΔP < 0: P_X0 = P_X+ + |ΔP|, so Σ_ΛA P = P_X+A_tot + |ΔP|A_X0 ≥ −|ΔP|[A_X0]_−.
Hence

  ∫dω[Σ_ΛA^{(n)}P(i|Λ)]_− ≤ ∫dω|P(i|ω) − P(i|ω − ω_Q)|·max([A^{(n)}_{X+}]_−, [A^{(n)}_{X0}]_−) ≤ 2ω_max·sup_ω max([A^{(n)}_{X+}]_−, [A^{(n)}_{X0}]_−),   (CW7-154′)

with the lemma and TV(P(i|·)) ≤ 2 under (M) unchanged; **λ_i ≤ (2ω_max/Δ_i)ϱ_−, ϱ_− ≡ sup_ω max([A_X+]_−, [A_X0]_−)/⟨A_tot⟩_i**. The R16 bound used only
[A_X+]_− and fails whenever A_X+ > A_tot somewhere in a ΔP < 0 window; for an interior bin both signs of ΔP occur (P(i|E) rises, then falls).
**Counterexample (CW7-C11, own construction; VER-CW7's 4.9×10⁻⁴ was built differently and is not reproduced digit for digit):** step bin [2ε_eh, 3ε_eh), Si
ε_eh, ω_Q = 62.3 meV, A_tot > 0, A_X+ ≥ 0 with a narrow peak above A_tot at the lower edge: negative part 4.70×10⁻³ while the R16 bound is 0; (CW7-154′)
gives 5.6×10⁻² and holds. **Size [E]** (Si single-electron bins) is unchanged in form: λ_i ≤ 0.033ϱ_−, with ϱ_− now containing the X0 negative part.
**Remedy row** (common P_X0 seeding, θ_seedP, r ≤ (2ω_max/Δ_i)ϱ with |A_X+|) stands as written (VER: correct). **Gate specification (replacement):**
"the WP6-v3 (4.2) gate adds per bin, model and m_χ the three numbers sup[A_X+]_−, sup[A_X0]_− and sup|A_X+|, each relative to ⟨A_tot⟩_i (one extra pass over the
library cells); pitfalls: bins narrower than ω_max (λ_i is then O(ϱ_−), not small); the edge shell (use O4 d11, Λ-independent P, where (P) holds by construction)."
### 1.6 V6 — LE-155 (VER-CW7 §B4)
- **Sum rule, restated [D].** "For a **one-body** Hamiltonian H = p²/2m_e + V with V local and **regular** (bounded ∇V on the support of |ψ_i|²), Σ_f(E_f − E_i)|⟨f|𝒯|i⟩|² =
  ⟨(∇V)²⟩/(2m_e³). Electron–electron terms add cross commutators [[p_i², V_ee], p_j²] for 𝒯 = Σ_i. For the bare Coulomb nucleus the right side **diverges** for
  every state with s density at the nucleus (hydrogenic 1s: ⟨(∇V)²⟩_{r>ε} → 4Z⁵/ε, CW7-C12b), i.e. the high-energy tail of |⟨f|p²|1s⟩|² is not summable with
  weight E_f." The FOM itself, Im R̃_{𝒯𝒯}(0, m_φ) at fixed m_φ, is finite. C12/C13 (smooth V) stay as tests of the regular case.
- **Pitfall (3), replacement.** "The f-sum and the (CW7-155) sum rule are not usable checks all-electron (divergent) and are pseudopotential-dependent otherwise.
  Use the exact identity ⟨c|p²|v⟩ = −2m_e⟨c|V|v⟩ (c ≠ v, eigenstates of the same H, V local **or nonlocal**, from p² = 2m_e(H − V)) as the matrix-element check;
  it compares the kinetic route Σ_G|k+G|²c*_{c,G}c_{v,G} (+ PAW one-centre term) with the potential route on the same wavefunctions." CW7-C12c: exact to 6×10⁻¹⁴
  for a random nonlocal V.
- **Polar mixing term, replacement [D].** WP0-v3 (3.6) uses the full in-medium propagator (Coulomb part v_C/ε_L, transverse part 1/(ω² − k² − Π^γ_T)), checked
  at l.171–173. At k_φ → 0 (k ≪ ω√ε_T), n = k·j/ω turns the Coulomb piece into (e²/ω²)k̂_ik̂_j/ε_L, and the transverse piece is (e²/ω²)(δ_ij − k̂_ik̂_j)/ε_T
  (Π^γ_T = ω²(1 − ε_T)). Both combine into the optical tensor: the mixing term is
  **−(y_φ²e²/m_φ³) Im[R̃_{𝒯i}(ε⁻¹)_{ij}R̃_{j𝒯}](0, m_φ)**, summed over all Cartesian i, j and independent of k̂ (sign convention of WP0-v3 (3.6)). The R16 form
  k̂·R̃ε⁻¹R̃·k̂ is the longitudinal component only. Non-polar groups: R̃_{𝒯j}(0, ω) = 0 for every j, so (CW7-155a) is unchanged.
- **n_e row.** "suppressed by v_DM/v_e (≈ 0.1–0.2 in amplitude for valence electrons, before 1/|ε|)", not by v_DM alone: the n_e amplitude is
  (|k|/ω)⟨j⟩ ∼ v_DM·v_e, the 𝒯 amplitude ⟨p²⟩/m_e² ∼ v_e².
- L-H3 re-issued (§2.3); WP0 owed row re-issued (§2.1). Literature status unchanged (2106.12586 [ABS]).
### 1.7 V7 — LE-156 (VER-CW7 §B5)
- **r^M derived [D for the size, E as a width].** The Casimir identity S(S+1) = ⟨S^xS^x + S^yS^y⟩ + ⟨(S^z)²⟩ holds exactly; with S^z = S − n and the
  Bogoliubov-vacuum ⟨n²⟩ = ΔS(1 + 2ΔS) (Wick, same-site ⟨aa⟩ = 0), the transverse weight is **W_⊥ = (S − ΔS)(1 + 2ΔS)**, whereas LSWT (S^+ ≈ √(2S)a)
  gives S(1 + 2ΔS). The O(S⁰) truncation therefore overstates the one-magnon weight by the relative amount **ΔS/S** (0.156, 0.052, 0.031 at S = ½, 3/2, 5/2,
  simple-cubic AFM; CW7-C14b) — the size of the first omitted HP term in the transverse vertex. **r^M ≡ ΔS/S** is the one M width of the residual magnon
  row (WP6 row and WP8-F-v3 §4); it dominates r_2m/(2S) for every S ≥ ½, so the R16 "max(ΔS/S, r_2m/(2S))" and "r_2m/(2S)" both collapse onto it.
- **(a) width defined.** "(a) A-type on S^{(2m)}: a^A median 1, σ_ln = 0.5 [E] on the two-magnon template; its effect on the total is ≤ r_2m(e^{0.5} − 1)."
- **Objects distinguished.** r_2m is an equal-time, q-integrated local ratio; 1/(2|𝐒|) of WP4-v3 is an expansion parameter. "Far below the heuristic" is
  withdrawn; r_2m and ΔS/S are the computed sizes, 1/(2S) the order-counting parameter.
- WP4 text re-issued without the contradiction (§2.1).
### 1.8 V8 — LE-157 (VER-CW7 §B6)
- **Wording.** "It does not carry I12" → "WP6-v3 (5.2) l.450 carries I12 by reference ('(WP4-v3 [4.2′], I12)') but not its directives — one-sided (downward)
  and exclusion of y ≲ 3.5 (WP4-v3 l.621)."
- **Mask column.** The mask is defined by the **KK-to-∞ column** of WP4-v3 K34 (the larger reduction, conservative): |δL/L| > 0.3 for y < **y_mask = 3.8**
  (log–log interpolation between y = 3 (0.53) and y = 5 (0.16)); on the cut column the same threshold sits at y = 3.0 (CW7-C15). y_mask = 3.8 contains I12's
  "y ≲ 3.5". σ_BCS(y) is the edge value (q = ω/v_max) applied to all q of a cell: conservative (|δL/L| falls with q at fixed ω), stated.
- **C15** uses one convention (Poisson 90%: −2lnL = 2μ at n = 0, Δ(−2lnL) = 4.605); profiled limits 2.324, 2.305 ≥ 2.303.
### 1.9 V9 — LE-160 (VER-CW7 §B7)
**Derivation (replaces (a), (b)) [D].** With signed elasticities e_A, e_B (s_X → s_X(1 + δ)^{e_Xθ_X}) and r_mat ∈ [0, 1]: Var(s_A + s_B) ∝ e_A²s_A² + e_B²s_B² +
2r e_Ae_Bs_As_B and Var ln(s_A/s_B) ∝ e_A² + e_B² − 2r e_Ae_B. For **e_Ae_B > 0** the combination is conservative at r = 1 and the ranking at r = 0 (R16 result);
for **e_Ae_B < 0** both flip (combination at r = 0, ranking at r = 1). CW7-C16 tests four sign patterns. Method nuisances (XC, 𝒳 rung) can move two materials'
FOMs in opposite directions, so the sign is a property of each (nuisance, material pair) and is read from the library's elasticities. Row 29 re-issued (§2.1).
### 1.10 V10 — LE-176 (VER-CW7 §B8)
Replacement sentence: "replacing the DFPT ε₀ by the measured one moves the POL weight by **2.8–5.6%** (PbTe; ε₀ from 1000 to ∞, '> 1000' being a bound),
1.3% (KTaO₃), **10.3%** (PbS, ε₀ → ∞), and by ×2.75 for SrTiO₃'s failed-run 9.96 (CW7-C17)." 0903.1445's χ⁻¹ "is a fit parameter of the equation of state
(polarisation in a field at 0.3 K), so ε₀ ≈ 2×10⁴ (SrTiO₃), 5×10³ (KTaO₃) are model-inferred [FT]". PbS, PbSe: "unusable" withdrawn → "no measured low-T ε₀
in the texts read (DFPT 161, 174 pass V2: IR 66.8/46.1 cm⁻¹; not quantum paraelectrics); the FOMs are insensitive to it (≤ 10.3%)". C18 now derives the
regularity from the rigid-ion model (ε₀ = ε_∞ + S_osc/ω_T² → ∞ while ω_L² → S_osc/ε_∞) instead of substituting the conclusion.
### 1.11 V11 — LE-177 (VER-CW7 §B9)
- **CaWO₄** (CW7 §11 "³H identified"): "¹⁷⁹Ta and ¹⁸¹W (EC) observed in CRESST data; ³H **inferred** from the ¹⁸¹W activity — 'It is hard to be observed
  experimentally … the observed ¹⁸¹W should be accompanied by a ³H component' [FT 1908.06755 p.4]; rate GAP." v4 row corrected.
- **EC lines.** "L- and M-shell captures produce lines at ≈ 1 and 0.1 keV [FT 1607.04560 p.3], but the Ge L-lines are at 1.1–1.3 keV (⁶⁵Zn, ⁶⁸Ge) [p.10],
  above the < 1 keV ROI: only M-lines and the resolution tails of the L-lines enter the sub-keV rate." v4 row `cosmo_EC_lines_subkeV`.
- **Specification, convergence criterion added.** "Geant4 route: run until every nuclide that contributes ≥ 1% of the sub-keV rate has a production rate with
  ≤ 10% statistical error (≥ 100 produced nuclei; 10⁸ primaries is the first estimate, doubled until met); report the ACTIVIA–Geant4 spread as the model band."
- CW7-C19 now computes f_<1 keV(³H) = 0.0892 from the Fermi-corrected spectrum instead of hard-coding it.
### 1.12 V15 — G-F6 (VER-CW7 §C): the spin-dependent nucleon class, specification rebuilt
**Strongest statement [D].** For unpolarised nuclear spins ⟨𝐒_κ⟩ = 0 and ⟨S_κ^aS_κ′^b⟩ = δ_κκ′δ^{ab}J_κ(J_κ+1)/3 (no nuclear order at mK and zero field), so the
coherent one-phonon amplitude Σ_κ c_κe^{iq·r_κ}(q·e_κν) of a spin-dependent operator averages to zero and **only the incoherent response survives**
(CW7-C36): S^{SD}(q, ω)/ρ_T = (1/M_cell)Σ_κΣ_{iso∈κ} x_iso w_iso S^{inc}_κ(q, ω), w_iso = (4/3)((J+1)/J)[a_p⟨S_p⟩ + a_n⟨S_n⟩]²_iso, with S^{inc}_κ the incoherent
phonon/impulse response of WP8-F-v3 §2.4(a) (e^{−2W_κ} included). A coherent piece survives only ∝ P_κ² (nuclear polarisation P_κ ≈ μ_κB/(k_BT): zero in zero field, but ≈ 0.1 for ¹H at 1 T and 10 mK)
[E], so a magnetised (B ≠ 0) target needs the coherent term back. **Missing steps (two):** (i) per-isotope ⟨S_p⟩, ⟨S_n⟩ (and the spin structure functions S_ij(q) for the impulse regime) from shell-model full texts;
(ii) the incoherent SD one-phonon response, which needs the partial phonon DOS D_κ(ω) (`GAP:phonon_DOS` rows): S^{inc,(1)}_κ = (q²/2M_κ)D_κ(ω)/ω at T = 0.
**Specification.** *What:* w_iso for the odd-A isotopes of every survivor (⁶Li, ⁷Li, ¹⁷O, ¹⁹F, ²³Na, ²⁷Al, ²⁹Si, ⁶⁹,⁷¹Ga, ⁷³Ge, ⁷⁵As, ¹²³,¹²⁵Te, ¹²⁷I, ¹³³Cs, ¹⁸³W,
⁹⁵,⁹⁷Mo; abundances and J from the v4 `isotopes[El]` rows); D_κ(ω). *Level:* q → 0 spin form factor for the phonon regime (q ≪ 1/R_N), shell-model S_ij(q)
above; harmonic incoherent approximation. *Method:* literature step for ⟨S_{p,n}⟩ (lit.py, ≥ 2 shell-model interactions per isotope); D_κ(ω) from DFPT on the
COMP-PH layout (qe-rtsc `rtsc/bench`: scf → ph.x on a q-grid → matdyn DOS projected on κ). *Convergence:* q-grid until ⟨ω⁻¹⟩_{D_κ} changes < 1%; DOS bin ≤ ω_th/4.
*Pitfalls:* the coherent term vanishes (do not reuse WP2-v3 (2.2) with c_κ → spin weights, the R16 spec); the shell-model spread of ⟨S_{p,n}⟩ (factor ≈ 2 for some
isotopes [UNVERIFIED]) is an A-type nuisance; spins are unscreened at SOC = 0; even-even isotopes contribute zero. Status: GAP (exact, two steps).

---
## 2. Owed corrections of CW7.md, re-issued (the merger uses only this list)
### 2.1 Changed by the verifier — complete replacement texts
- **WP6-v3 §4.5 (G8′)** → "G8′ is closed by CW7 Theorem G8′ (returns/R16/CW7.md §3, corrected by CW7-errata §1.3): in the velocity measure F ≥ 0 the counts are
  linear with stream kernels 𝔎_i(w); admissible Radon data form the weak-* closed cone dual to {g : R*g ≥ 0 on B}; the conservative bound is the semi-infinite LP
  sup{∫φdF : ∫𝔎_idF ≤ N_i^{up}} = min{Σλ_iN_i^{up} : Σλ_i𝔎_i ≥ φ}, attained by ≤ N_bins streams, under 𝔎_i ≥ 0 (anisotropic (P)) and visibility
  max_i𝔎_i > 0 on {φ > 0}; under (I) **in the lab frame** it reduces to (4.2); signed φ (modulation amplitudes) need visibility on {φ > 0}."
- **WP6-v3 §11 OW6-1, OW6-3, OW6-6** → "OW6-1 CLOSED (CW7 §3 with errata §1.3); OW6-3 CLOSED (CW7 §4 (CW7-153a), (CW7-153b) as reworded in errata §1.4; solver
  code/CW7/cascade_gf.py as fixed for θ_ii > 1); OW6-6 CLOSED (errata §1.5 (CW7-154′); the R16 (CW7-154) fell)."
- **WP6-v3 §4.2, sentence "The affected fraction is O(ω_Q/ε_eh) ≈ 1–2% of pairs in Si …, sign unbounded"** → "The negative part is bounded by (CW7-154′):
  λ_i ≤ (2ω_max/Δ_i)ϱ_−, ϱ_− ≡ sup_ω max([A_X+]_−, [A_X0]_−)/⟨A_tot⟩_i (stochastic monotonicity of N in E; both pieces are needed because P_X+ − P_X0 takes both
  signs in an interior bin); 3.3%·ϱ_− for Si single-electron bins."
- **WP6-v3 §5.2** → add the magnon row and the seeding row, and replace the "Superconducting targets" row, by:
  | Magnon reference LSWT (ref = LSWT; HP order) | (a) S^{(2m)}_αβ of WP4-v3 [2.4] in the central value (AFM/ferri; ≡ 0 for a FM at T = 0); (b) residual magnon–magnon interaction and one-magnon weight renormalisation; (c) magnetic form factor F^{mag}_j(q) (dipole ⟨j₀⟩ + (1 − 2/g_J)⟨j₂⟩) and ligand covalency; (d) Δ_mag, J^{ex} | (a) A (PSD); (b) M on contracted scalars; (c) M; (d) E | (a) a^A median 1, σ_ln 0.5 [E] on the two-magnon template; (b) **r^M = ΔS/S** (Casimir sum-rule defect of LSWT, CW7-errata §1.7) from the Bogoliubov coefficients; (c) σ_ln 0.2 [E]; (d) σ_E = measured-gap error (Cr₂O₃ 0.696, MnO 3.39, NiO 4.76/5.33 meV [FT via WP8-U-TOP]) or the DFT+U spread | material (θ_mag, θ_Fmag) | WP4-v3 [2.1]–[2.4]; CW7 LE-156; errata §1.7 |
  | Superconducting targets (Al, Nb; WSi without a quoted factor) | L^{BCS} = 𝔤_IL^{nor}[1 − 2(Δ_BCS/qv_F)𝔰_BCS] (WP4-v3 [4.2′], I12), central with the KK cut at ω′ = qv_F | **M one-sided (downward)**, θ_BCS half-normal: s = s_c e^{−\|θ\|σ_BCS(y)} | σ_BCS = 0.09 (y = 5), 0.03 (y = 10), interpolated in ln y, evaluated at the edge q = ω/v_max and applied to all q of the cell (conservative); **cells with \|δL/L\|_{KK-∞}(y) > 0.3, i.e. y < 3.8 (contains I12's y ≲ 3.5), masked from the signal (conservative) until RG9** | material | WP4-v3 K34, I12; CW7 LE-157; errata §1.8 |
  | Seeding (P) | P_{X0} for X0 and X+ of the same pair | M | r ≤ (2ω_max/Δ_i)ϱ, ϱ ≡ sup\|A_X+\|/⟨A_tot⟩_i | material | CW7 LE-154 (remedy, unchanged) |
- **WP4-v3 §2.1(c) and [2.2](b)** → "1/(2|𝐒_j|) is the LSWT expansion parameter: 0.2 for YIG (|𝐒| = 5/2); = 1 at |𝐒| = ½, where LSWT is qualitative only. The
  computed sizes are r_2m = ΔS(1 + ΔS)/(S(1 + 2ΔS)) (local two-/one-magnon ratio; 0.146 at S = ½, simple-cubic AFM) and the one-magnon weight defect ΔS/S
  (0.156 at S = ½; CW7-errata §1.7)."
- **WP0-v3 (3.5)–(3.6), scalar row** → "closed form: Γ_φ = −(y_φ²/m_φ)Im R̃_{𝒯𝒯}(0, m_φ) for non-polar point groups; polar groups add
  −(y_φ²e²/m_φ³)Im[R̃_{𝒯i}(ε⁻¹)_{ij}R̃_{j𝒯}](0, m_φ) (longitudinal + transverse parts of 𝒟^γ, full optical ε tensor) (CW7-155a,b; errata §1.6). The per-electron sum rule
  Σ_f(E_f − E_i)|𝒯_fi|² = ⟨(∇V)²⟩/(2m_e³) holds for a one-body regular V only and diverges for the Coulomb nucleus; the matrix-element check is
  ⟨c|p²|v⟩ = −2m_e⟨c|V|v⟩."
- **CONVENTIONS §13 new row 29** → "| 29 | r_mat and profile/envelope (2026-11-01) | WP6-v3 default r_mat = 0 (1 as a variant); OW6-4 | **method nuisances (𝒳 rung, XC PCs,
  pair-screening factor, yield model, 𝒜_ph) r_mat = 1 across materials computed with the same method and version; independently measured inputs r_mat = 0. The
  conservative choice depends on the sign of the two elasticities: for same-sign elasticities combined limits use r_mat = 1 and rankings report r_mat = 0 bands;
  for opposite signs combined limits use r_mat = 0 and rankings r_mat = 1; the sign is read per (nuisance, material pair) from the library. Headline = profile
  (WP6-R2), band = envelope (WP6-R3), declared in the library header.** *Why:* over r ∈ [0, 1] the variance of a sum is maximal at r = 1 and that of a ratio at
  r = 0 exactly when e_Ae_B > 0, and the reverse when e_Ae_B < 0 (CW7-errata §1.9, CW7-C16) |".
- **CONVENTIONS §12 provenance** (pointer change only) → "[DB] database entry with ID and field (JARVIS-DFT `JVASP-n`, MP/Alexandria OPTIMADE, NIST, IAEA); ranks
  below [FT] and [CALC]; DB fields obey the vetting rules V1–V6 of returns/R16/WP8-U-v3.md §1.3 (JARVIS `elastic_tensor` shear order (xy, yz, zx), re-indexed
  to Voigt before use)."
- **NOTATION** → the rows of the Symbols table of CW7.md plus: c_NR1 (heavy-mediator NR-1ph speed ⟨Σ_ν(q̂·ê_ν)²/c_ν⟩⁻¹), r^M (residual magnon width ΔS/S),
  y_mask (SC mask boundary 3.8), K_ν (per-branch light-mediator weight), ϱ_− redefined (max of the X+ and X0 negative parts), w_iso (SD isotope weight).
- **SOTA (WP8 block)** → "WP8-U/F revised (R16 CW7 + ERR-CW7): **WP8-U-v3, table v4, WP8-F-v3** supersede R13 and the R16 v2 files; yield rows released;
  WP8-S synthesis in CW7 §12 pending its revision (separate agent) and R×2."
### 2.2 Unchanged by the verifier
LIMITS L4 note ("✔ data cross-check … ≤ 1.2% with A₁ = ∥, E₁ = ⊥ (CW7-C28)") — **unchanged**. The seeding-row remedy — **unchanged** (re-listed above only
for completeness of §5.2). Every other CW7 statement not named in §1 — **unchanged**.
### 2.3 Proposed LIMITS rows, re-issued
| # | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L-H1 | WP6-v3 (1.7) linear in F ≥ 0 → stream kernels → semi-infinite LP; (I) **in the lab frame** → WP6-v3 (4.2) | internal derivation; NR stream method of 1403.4606, 1703.09168 **[ABS] only** (structure, not checked) | first Born; 𝔎_i ≥ 0; visibility on {φ > 0}; compact velocity support | (P) leakage (CW7-154′) with max([A_X+]_−, [A_X0]_−); grid refinement certified by the dual (C3) | DERIVED (C1–C4) |
| L-H2 | (CW7-153a) p.g.f. recursion → z-derivatives = GAP-EF (EF3)–(EF4); → P_casc(N\|Λ) | GAP-EF §1.3 (internal); R&K 2004.10709 moments not re-read here | (H-EF1)–(H-EF7); symmetric-DOS solver (general case specified, §1.4) | θ_{R-k}; T beyond E_g(T); excitons; aliasing iff P(N ≥ N_z) ≠ 0 | DERIVED (C5, C5b, C6–C8; θ_ii = 1, 3/2, 2) |
| L-H3 | ψ̄ψ → n_e − 𝒯_e; charge conservation; ℓ = 1 selection → Γ_φ = −(y²/m_φ)Im R̃_{𝒯𝒯}(0,m_φ); polar term with the full 𝒟^γ | internal; 2106.12586 **[ABS] only** | non-polar point groups (else the tensor mixing term); first order in y_φ; NR DM | n_e row O(v_DM/v_e) in amplitude; target relativistic corrections; sum rule one-body and regular V only (divergent for Coulomb) | DERIVED (C12, C12b, C12c, C13) |
| L-H4 | LSWT/HP to O(S⁰) → W_∥/W_⊥ = ΔS(1 + ΔS)/(S(1 + 2ΔS)) | WP4-v3 [2.4] | T ≪ T_N; two-sublattice AFM | O(1/S): one-magnon weight defect ΔS/S (C14b) | DERIVED (C14) — unchanged except the correction column |
| L-F1, L-F2, L-F3, L-F4 | as WP8-F-v3 "Proposed LIMITS rows" (L-F1 validity split light/heavy; L-F2 lossless consistent-pair bound; L-F3 cross-check = R14 referees' recomputation, not C20; L-F4 new: light-mediator target independence, 1910.10716 Eq. (35) [FT p.9]) | | | | |

---
## 3. Rebuttals
**No claim of VER-CW7 is rebutted.** Every number it states that could be recomputed offline was reproduced: ΣP = 0.9529 and mean 1.970 vs 2.096 (old solver,
θ_ii = 3/2); 55 [E]-evidence screen_S rows and 13 duplicated keys; GaAs JVASP-1174 field; WP6-v3 l.450 cites I12; K34 mask positions (y ≈ 3.0 cut, 3.8
KK-∞); PbTe 2.8–5.6%, PbS 10.3%; f_<1 keV(³H) = 0.0892; ⟨(∇V)²⟩_{1s} → 4Z⁵/ε; ΔS = 0.0782, r_2m(½) = 0.1458; 2.056 at θ_ii = 3/2; the WP0-v3 (3.6) full
propagator; the 1908.06755 and 1607.04560 quotes. Its B3 counterexample value (4.9×10⁻⁴) could not be reproduced without its construction; an independent
counterexample (C11) confirms the verdict. One refinement, not a rebuttal: the G-F6 coherent term vanishes only at zero nuclear polarisation; it reappears
∝ P_κ² in an applied field (P ≈ 0.1 for ¹H at 1 T, 10 mK; §1.12).
**Refinements of the REF-WP8-S referees' claims used in the v3 files** (not verifier claims; each with a check): (a) 1910.10716 Eq. (35) is on PDF p.9 (REF-B: p.10);
(b) REF-A §6a / REF-B §G1 compare the R16 "upper" route 9.15 with the *damped* o-ray integral 9.40 (WP8-F checks C4c, ∫₀^{1500 meV}); the bound in question is a
lossless one, and the lossless o-ray mode sum is 9.12 < 9.15. The conclusion still stands on the correct comparison: the lossless **axis-averaged** mode sum
(1/3)(2L_o + L_e) (1807.10291 Eq. (40)) is 9.27 > 9.15, and the consistent bound (same factorised model: ε₀ = ε_∞Π(ω_L/ω_T)² per axis, ω_L,max) is 9.52 ≥ 9.27 (CW7-C31). Damping adds O(γ_L/ω_L) above any lossless bound (+3% for the
sapphire o-ray); (c) Li₂MoO₄ is not in "no channel" (REF-A §2): it enters the Migdal nuclear-factor row (1.05 in ranking.json) and lacks inputs for the other
four (v4 `GAP:channel_inputs`); (d) TeO₂ ⟨Σ(q̂·ê)²/c⟩⁻¹ with the R16 tensor is 3.780 (REF-A: 3.77), 3.759 after re-indexing (CW7-C34).

---
## 4. Checks (code/CW7/checks.py, 40 checks, all PASS, 5–25 s)
Replaced (tautological or circular per VER-CW7 §F): **C3** (cross-grid dual certificate + column generation), **C4** (lab vs galactic frame), **C11** (counterexample
+ corrected bound), **C15** (one C.L. convention + mask positions), **C16** (signed elasticities), **C18** (rigid-ion model), **C19** (f computed), **C20** (Migdal
plasmon pole + f-sum bound), **C21** (S_LO derived), **C23** (per-branch K at 2–3× edge), **C27** (light/heavy NR-1ph scaling, replaces the solve-for-σ floor),
**C29** (v4 integrity), **C31** (POL bound as an inequality; no rank.py rerun, so checks.py no longer rewrites data/ranking.json). Tightened: C1 (relative 1e-9),
C5 (1e-13; θ_ii = 1, 3/2, 2), C6 (6×10⁻⁴; adds θ_ii = 3/2), C7 (10⁻³), C13 (3×10⁻³), C14, C17 (2×10⁻⁴), C23 (0.1), C25. Added: C5b (aliasing), C12b (Coulomb
divergence), C12c (exact matrix-element identity, nonlocal V), C14b (Casimir r^M), C33 (JARVIS shear order; [001] degeneracy), C34 (Σ(q̂·ê)² = 1, c_NR1),
C35 (²¹⁰Pb S4 threshold), C36 (G-F6 incoherence). Kept as written: C2, C8–C10, C12, C22, C24, C26, C28, C30. C32 is a record check (API-verified IDs; the three
ERR-CW7 quotes found in the fetched texts), labelled as such.

## 5. Interfaces
| # | Owner | Item | Action |
|---|---|---|---|
| IF-ERR7-1 | WP8-S agent | rank.py still reads v3: point it at WP8-U-table-v4.csv; NR-1ph: light mediator unranked by c (rank by the edge), heavy mediator by `c_NR1_heavy` in 0.1 ≲ m_χ ≲ q_BZ/2v_max; POL ε route only as the consistent bound; Migdal row × 𝓠_Mig (plasmon pole ∝ (ω_p^{val})⁻³); `GAP:channel_inputs` lists; Pb salts S4-COND (²¹⁰Pb) | apply in the §12 revision |
| IF-ERR7-2 | WP6 | §2.1 texts (G8′, (4.2) sentence, §5.2 rows) | apply |
| IF-ERR7-3 | WP0 / WP4 | scalar row; 1/(2\|𝐒\|) sentence | apply |
| IF-ERR7-4 | coordinator | CONVENTIONS row 29, §12 pointer; NOTATION rows; SOTA block | apply |
| IF-ERR7-5 | literature agent | G-F6 step (i): shell-model ⟨S_p⟩, ⟨S_n⟩ full texts; measured C_ij (TeO₂, CsI, CaWO₄, hexagonal set); low-T E_g of Ge, GaAs, GaSb; ²¹⁰Pb of available lead | fetch |
| IF-ERR7-6 | referees (R17) | R×2 of this errata + WP8-U-v3 + WP8-F-v3 | launch |
The LE-159 status ("single missing step R×2") is outside this brief; REF-WP8-S-B §J lists two further missing steps (uncertainty bands; light-mediator
NR-1ph re-ranking), passed on through IF-ERR7-1.

## 6. Closing table (verifier item → resolution → location)
| Verifier item | Resolution | Location |
|---|---|---|
| V1 / RC9: 55 [E] rows, 13 keys, TeO₂ ρ, V1–V6 | APPLIED (v4: 44 retagged, 13 dropped, verdict column, proxy flag) | §1.1; WP8-U-v3 §0, §2, §4.1; C29 |
| V1 trace defect: CaWO₄ ³H "observed" / RC8 | CORRECTED ("inferred") | §1.11; v4 row; WP8-U-v3 §4.4 |
| V2 A-§E(c), A-§E(a) | APPLIED (C23, C21) | §1.2; WP8-F-v3 §2.3, §2.5 |
| V2 C20 / RC12 L-F3 | C20 withdrawn as cross-check; L-F3 cites R14 referees | §1.2, §2.3; WP8-F-v3 LIMITS |
| V2 MAG nuisance / RC4 | ONE width r^M = ΔS/S, derived | §1.7; WP8-F-v3 §2.6, §4; §2.1 row |
| V2 𝓡 vs ℛ | DEFINED | §1.2; WP8-F-v3 Symbols |
| V3 (iv) lab frame, (c) (H4), C3/C4 | APPLIED | §1.3; §2.1 G8′ text; C3, C4 |
| V4 / RC2 solver θ_ii > 1, (CW7-153b), spec | FIXED / REWORDED / COMPLETED | §1.4; cascade_gf.py; C5, C5b, C6, C8 |
| V5 / RC1 (CW7-154) FALLS | RE-DERIVED (CW7-154′); WP6 §4.2 text and L-H1 re-issued; ΔP < 0 test | §1.5, §2.1, §2.3; C11 |
| V6 / RC3 sum rule, polar mixing, n_e row | RESTRICTED + exact replacement check; full 𝒟^γ; v_DM/v_e | §1.6, §2.1, §2.3; C12b, C12c |
| V7 / RC4 r^M, (a) width, WP4 text | DERIVED / DEFINED / RE-ISSUED | §1.7, §2.1; C14b |
| V8 / RC5 I12 wording, mask column | APPLIED (KK-∞, y_mask 3.8; one C.L.) | §1.8, §2.1; C15 |
| V9 / RC6 same-sign elasticities | DERIVED general rule; row 29 re-issued | §1.9, §2.1; C16 |
| V10 / RC7 PbTe, PbS, χ⁻¹ | APPLIED | §1.10; WP8-U-v3 §4.3; C17, C18 |
| V11 / RC8 ³H, Ge L-lines, Geant4 convergence | APPLIED | §1.11; v4 rows; C19 |
| V12, V14 | STAND | unchanged |
| V13 owed list | RE-ISSUED (changed) / marked unchanged | §2 |
| V15 / RC10 G-F6 | SPEC REBUILT; two missing steps | §1.12; WP8-F-v3 §7; C36 |
| V16 / RC11 L-H1, L-H3 [ABS], L-H2, L-F3 | RE-ISSUED ([ABS]-level status stated) | §2.3 |
| §F tautological checks | REPLACED / TIGHTENED / ADDED | §4 |
| Brief item 0: REF-WP8-S FOM findings (light-mediator c-independence; heavy 1/c window ≈ 0.1–0.43 MeV; polar bound; 𝓠_Mig plasmon pole; uniaxial C_ij; GAP-input dropouts; ²¹⁰Pb) | APPLIED | WP8-F-v3 §0, §2.3, §2.5, §2.7, §5, §8; WP8-U-v3 §4.1′, §4.4, §4.5; C20, C27, C31, C33–C35 |

## Symbols introduced/used
| Symbol | Meaning | Status |
|---|---|---|
| ϱ_− | sup_ω max([A_X+]_−, [A_X0]_−)/⟨A_tot⟩_i | redefined (was the X+ part only) |
| ΔP | P_X+ − P_X0 | new (local) |
| r^M | residual magnon M width ΔS/S | new |
| y_mask | SC mask boundary (KK-∞ column, threshold 0.3): 3.8 | new |
| K_ν(m_χ) | ∫(dq/q)η(v_min(q, ω_Lν)) per polar branch | new |
| c_NR1 | ⟨Σ_ν(q̂·ê_ν)²/c_ν(q̂)⟩⁻¹ (heavy-mediator NR-1ph speed) | new |
| w_iso | SD isotope weight (4/3)((J+1)/J)[a_p⟨S_p⟩ + a_n⟨S_n⟩]² | new (G-F6) |
| P_κ | nuclear spin polarisation | new (local) |
| used | 𝔎_i, F, φ, Φ, λ_i, N_i^{up}, 𝔊_t, θ_ii, N_z, A_X0, A_X+, A_tot, TV, ω_max, Δ_i, 𝒯_e, R̃_{𝒯𝒯}, R̃_{𝒯j}, 𝒟^γ, ε_L, ε_T, ΔS, r_2m, W_⊥, W_∥, σ_BCS, 𝔰_BCS, y_BCS, r_mat, e_A, ε₀, ε_∞, f_<1, 𝓠_Mig,κ, ω_p^{val}, c_LA | CW7.md Symbols, NOTATION v4 |
