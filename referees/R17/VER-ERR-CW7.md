# R17 / VER-ERR-CW7: hostile verification of returns/R16/CW7-errata.md, WP8-U-v3.md, WP8-U-table-v4.csv, WP8-F-v3.md

Referee VER-ERR-CW7 (brief briefs/R17/VER-ERR-CW7.md). **Read:** the four files under review; code/CW7/* (build_v4.py, cascade_gf.py, checks.py, data/*);
referees/R16/VER-CW7.md, REF-WP8-S-A.md, REF-WP8-S-B.md; CONVENTIONS.md (§12, §13 rows 26–36, amendments); returns/R8/WP4-v3.md, WP6-v3.md (grep of the
owed-correction targets); code/WP8-U-TOP/data/jarvis_top.json. Nothing else under returns/R16, referees/ or briefs/ was read.
**Reruns:** `checks.py` 40/40 PASS in 4.5 s (reproduced). Independent scratch checks (own code, not the return's): Christoffel speeds of all 11 non-cubic
JARVIS tensors in both index orders; Monte-Carlo cascade vs the fixed solver; heavy/light NR-1ph ratios vs m_χ; sapphire polar bounds with alternative inputs;
β fractions for ³H, ²¹⁰Pb, ²¹⁰Bi; the CW7-154′ case split; the Casimir algebra. All ≤ 2 min.
**Literature** (lit.py → literature/papers-r17-VER-ERR-CW7/, PDFs and HTML deleted, `.txt` kept; page = PDF page): 1910.10716, 2408.04732, 1912.10270, 1110.1346,
cond-mat/0507217, 1607.04560, 1908.06755 (used); 0803.4056, 1607.04584, 1804.07432, 1108.2770, cond-mat/0011434, cond-mat/9812293 (fetched, no usable C_ij).
**Primary source for JARVIS:** usnistgov/jarvis `jarvis/io/vasp/outputs.py`, `Outcar.elastic_props` (raw GitHub, master, fetched 2026-11-01).

---
## 0. Verdict table (scope items 0–3)
| # | Item | Verdict | Reason (section) |
|---|---|---|---|
| 0a | JARVIS shear order (xy, yz, zx); build_v4.py re-indexing; §4.1′ values | **STANDS WITH CORRECTION** | Order confirmed: JARVIS source code, a symmetry proof, and measured C_ij for 4 materials; build_v4 reproduced to 10⁻³ km/s. Fix the wording: for orthorhombic PE the error was a cyclic shift, not a C₄₄↔C₆₆ swap (§A) |
| 0b | 55 [E] screening rows; 13 keys; verdict column | **STANDS WITH CORRECTION** | All 44 retagged and all 13 dropped rows checked (more than the required 15): correct. One misdescription: the 2 non-[E] dropped rows are GaAs S1 and SiO₂-q S1, not "2 GaAs rename rows" (§B) |
| 0c-i | (CW7-154′) [D] | **STANDS** | The case split re-derived; the bound is sharp per case (§C1) |
| 0c-ii | cascade_gf.py fix for θ_ii > 1 | **STANDS WITH CORRECTION** | Fix is correct: ΣP = 1, and the solver matches MC to 0.1% on a commensurate grid. The convergence spec needs a pitfall: the grid step h must divide ω₀ and E_g, or Richardson extrapolation is invalid (1.8% bias at the coded h; §C2) |
| 0d-i | Light-mediator NR-1ph target independence (2.3a″), L-F4 | **STANDS WITH CORRECTION** | Derivation and 1910.10716 quote confirmed. The dominant correction below ≈ 1 MeV is O(m_min^ac/m_χ) in the η argument; it is missing from the row (§D1) |
| 0d-ii | Heavy-mediator window "m_χ,edge ≈ 0.1 MeV (1 meV, (2.3b))" | **STANDS WITH CORRECTION** | (2.3b) gives 6.5 keV (Si) and 41 keV (CsI) at 1 meV, not 0.1 MeV. In this model 0.1 MeV is the 1910.10716 regime boundary. The 1/c window is pairwise (§D1) |
| 0d-iii | Polar ε-route bound 9.52 and its conditions | **STANDS WITH CORRECTION** | Arithmetic reproduced (9.27 ≤ 9.52 ≤ 11.84). But condition (ii) can only be met with mode data: with measured ε₀ and ε_∞ = 3.26 the same formula gives 9.05 < 9.27. For ε-route materials only the (8.1) upper end is a usable bound (§D2) |
| 0d-iv | 𝓠_Mig plasmon pole and f-sum bound | **STANDS** | (π/2)ω_p⁻³ and ≤ (π/2)ω_p²/E_g⁵ re-derived; ratio 3.89, net 0.87 reproduced (§D3) |
| 0d-v | ²¹⁰Pb S4 condition, LU5′ | **STANDS** | 0.0438, 9.65×10⁻⁴, 689 /(kg·d·keV) per Bq/kg, 1.45 mBq/kg reproduced; containment argument sound (§D4) |
| 1.1 | V1 table corrections | STANDS WITH CORRECTION | as 0b |
| 1.2 | V2 WP8-F items (K-ratios, S_LO, C20 withdrawn, r^M, 𝓡/ℛ) | STANDS | C21, C23 rerun; S_LO cancellation as stated |
| 1.3 | G8′ (iv) lab frame; (c) (H4) on {φ > 0} | STANDS | weak duality holds for signed φ; invisible mass in {φ > 0} gives sup = ∞ |
| 1.4 | LE-153 (153b) aliasing wording; general-case spec | STANDS WITH CORRECTION | as 0c-ii (grid commensurability) |
| 1.5 | (CW7-154′), gate spec | STANDS | §C1 |
| 1.6 | LE-155 sum rule restriction; ⟨c\|p²\|v⟩ check; polar tensor term; v_DM/v_e | STANDS | at k ≪ ω√ε the full propagator → −(ε⁻¹)_ij/ω², independent of k̂; 1s divergence 4Z⁵/ε re-derived (§C3) |
| 1.7 | r^M = ΔS/S "derived [D for the size]" | **STANDS WITH CORRECTION** | The algebra is right. What is derived is the defect in the *total* transverse equal-time sum rule. The one-magnon weight also loses weight to the 3-magnon continuum, so ΔS/S is a *lower bound* on the one-magnon overstatement, evaluated in the LSWT vacuum. Status for the one-magnon reading is [E] (§C4) |
| 1.8 | I12 wording, y_mask 3.8, one C.L. | STANDS | log–log interpolation 3·(5/3)^0.475 = 3.83 reproduced |
| 1.9 | signed-elasticity rule, row 29 | STANDS | variance extrema re-derived; CONVENTIONS row 29 already carries the text verbatim |
| 1.10 | LE-176 PbTe/PbS shifts, χ⁻¹ fit parameter | STANDS | C17, C18 rerun |
| 1.11 | LE-177: CaWO₄ ³H inferred; Ge EC lines | **STANDS WITH CORRECTION** | CaWO₄ quote confirmed [FT 1908.06755 p.4]. But "only M-lines … enter the sub-keV rate" is false: ⁴⁹V and ⁵⁵Fe, both in the return's own Ge production table, have L-lines below 1 keV (§E1) |
| 1.12 | G-F6 incoherent SD class, spec | **STANDS WITH CORRECTION** | Physics right. The isotope list omits ⁴³Ca (survivor CaWO₄) and many COND-material isotopes. D_κ/ω holds only for cubic sites, and the normalisation and e^{−2W} are unstated (§F) |
| 1.13 | Owed corrections §2.1 (targets, texts) | STANDS | every target located (WP6-v3 l.321, l.450, l.584–588; WP4-v3 l.99, l.117); WP4-v3's "0.5 for \|𝐒\| = ½" is indeed wrong (= 1); row 29 and the §12 [DB] pointer already merged |
| 1.14 | Status upgrades: (CW7-154′) [D]; r^M [D]; signed-elasticity [D]; L-F4 DERIVED; G-F6 [D] | STANDS except r^M | §C4 |
| 2a | 1910.10716 Table I c_LA (GaN, AlN, ZnO) "suspect, pending measured C_ij" | **CONFIRMED (defect)** | With measured C_ij the fastest LA speed is 8.2, 11.3 and 6.2 km/s. The paper prints 12.5, 17.1 and 12.5 km/s (×1.53, 1.51, 2.03) for an average taken at q ≈ 10 eV ≪ q_BZ, so no direction can reach them. NaCl and α-SiO₂: UNRESOLVED (no measured C_ij read) (§E2) |
| 2b | 1910.10716 Eq. (35) on PDF p.9 (REF-B said p.10) | CONFIRMED | quote "the dependence on the target properties drops out" p.9; Eq. (37) "Between 10⁻¹ and 1 MeV" p.10 |
| 2c | 2008.08560 n_e column; 1910.02091 Δ half-gap | not new in this return (R14 adjudications); not re-rated | – |
| 3 | New derived results: c_NR1 scalar; (2.3a″); polar bound conditions; 𝓠_Mig bounds; r^M; ²¹⁰Pb rate; G-F6 incoherence | as rows 0d, 1.7, 1.12 | – |

---
## A. JARVIS shear order (scope 0a)
**Documentation/source.** `Outcar.elastic_props` reads the six rows after "TOTAL ELASTIC MODULI (kBar)" and stores c[i][j] = OUTCAR[i][j]/10 with **no
reordering** (fetched source). So `elastic_tensor` is in VASP's OUTCAR order. That order is XX YY ZZ XY YZ ZX ([UNVERIFIED]: the VASP-wiki
"Phonons from finite differences" page shows the header line but not the column labels). The return's [D] symmetry argument does not depend on this and is
decisive. In all 10 hexagonal/trigonal tensors, JARVIS index 3 = (C₁₁ − C₁₂)/2 (GaN 107.2 vs 107.15; SiO₂-q 34.4 vs 34.45; h-BN 342.7 vs 342.7). In the trigonal
entries the identity reading also gives C₄₄ ≠ C₅₅ (Al₂O₃ 158.3 vs 140.9), which symmetry forbids. After re-indexing, the trigonal couplings form the C₁₄-setting
pattern C₂₄ = −C₁₄, C₅₆ = C₁₄ (Al₂O₃ −20.8/+20.8/−20.8; SiO₂-q, Bi₂Se₃ likewise). "C₁₄ was read as C₁₅" is correct.
**Measured C_ij [FT], ≥ 3 materials (the C₄₄/C₆₆ ratio decides between the two orders):**
| Material | Source | measured C₄₄ / C₆₆ | v4 (JARVIS idx 4 / idx 3) | R14–R16 reading |
|---|---|---|---|---|
| Al₂O₃ | 2408.04732 Table A.6 p.14: C₁₁ 495, C₁₂ 161.1, C₄₄ 147.7 (printed "−147.7" in a column labelled C₃₄/C₄₄ that holds C₃₃ = 499.9: a header misprint there) | 147.7 / 167.0 = 0.885 | 140.9 / 158.3 = 0.890 | 1.124 |
| TeO₂ | 1912.10270 p.6: "c11 < c66 … c11 = 56.12 GPa and c66 = 66.14 GPa" | C₆₆ > C₁₁ | C₆₆ 72.7 > C₁₁ 56.3 | C₆₆ 28.8 < C₁₁ (contradicts) |
| GaN | 1110.1346 Table I p.2 (recommended values, Vurgaftman–Meyer): 390, 145, C₄₄ 105 | 105 / 122.5 = 0.857 | 90.2 / 107.2 = 0.841 | 1.188 |
| AlN | same table, experimental (Madelung): 411, 149, C₄₄ 125 | 125 / 131 = 0.954 | 114.7 / 126.7 = 0.905 | 1.105 |
| ZnO | cond-mat/0507217 Table III p.7 (BLS, polycrystalline films): C₄₄ 44, C₆₆ = 44 | ≈ 1 (not discriminating) | 36.1 / 39.5 | – |
Four materials favour the v4 order unambiguously. **build_v4.py**: PERM = [0, 1, 2, 4, 5, 3] maps Voigt (yz, zx, xy) ← JARVIS (4, 5, 3) as required.
My own Christoffel code (VASP-order map built independently, 2×10⁵ random directions) reproduces christoffel_v4.json for all 11 entries to ≤ 0.007 km/s:
TeO₂ c̄_LA 4.096, c_NR1 3.759, c_LA,max 4.606, [001] T 2.21/2.22; old order 4.050/3.781/[2.22, 3.51]. The other values match too: α-SiO₂ 6.232/6.011; h-BN 15.48/6.80;
Al₂O₃ 10.780/10.740/11.12. Every §4.1′ number checked stands (h-BN −56%, TeO₂ −8%, α-SiO₂ −4%).
**Correction.** WP8-U-v3 §0 row 10 and the build_v4 note "C₄₄ and C₆₆ were swapped for every non-cubic entry". This holds for the uniaxial entries (C₄₄ = C₅₅).
For orthorhombic PE the old reading was a **cyclic shift** (old C₄₄, C₅₅, C₆₆ = true C₆₆, C₄₄, C₅₅: 4.0/8.8/2.4 vs true 8.8/2.4/4.0). Replace with
"the shear block was cyclically mis-indexed (xy, yz, zx read as yz, zx, xy); for uniaxial crystals this is a C₄₄ ↔ C₆₆ swap". Also, the C33 check
tolerance (`ident < 0.11`) is looser than the printed "0.05 GPa"; the actual maximum is ≤ 0.05.

## B. Screening rows and keys (scope 0b)
All 44 retagged rows (data/v4_changes.json → v4 CSV) checked. Each v4 value equals the recorded new text and is tagged UNVERIFIED. PASS/FAIL on [E] alone →
COND (e.g. InSb S1, NaCl S2, Nb S1–S2, PE S2, NiPS₃ S2 FAIL → COND). Al₂O₃ S2 keeps PASS on [ABS 1704.04320]. No SURVIVOR row lost PASS on [FT]/[ABS]. All 13 dropped
rows were matched to the unique kept row: 11 to the uniform "COND … [UNVERIFIED]" S1 text, and GaAs S1/S2 to the [FT 2507.07119] rows. Integrity: v3 had 154 screening rows,
55 with "[E]" and 13 duplicate keys; v4 has 141 unique keys, 0 with "[E]", and 3311 − 13 + 123 = 3421 rows. **Correction (errata §1.1):** the dropped [E] rows are 11.
The two non-[E] dropped rows are **GaAs S1 ([ABS]) and SiO₂-q S1 ([UNVERIFIED])**, not "the 2 non-[E] GaAs rename rows": GaAs S2's dropped row contained "[E]".

## C. Derivations
**C1 (CW7-154′).** With ΔP = P_X+ − P_X0, A_tot ≥ 0, P ∈ [0, 1]:
- if ΔP ≥ 0, Σ = P_X0A_tot + ΔP·A_X+ ≥ −ΔP[A_X+]_−;
- if ΔP < 0, Σ = P_X+A_tot + |ΔP|A_X0 ≥ −|ΔP|[A_X0]_−.

So [Σ]_− ≤ |ΔP|·max(·). The lemma (∫|f(E) − f(E − h)| ≤ h·TV) and TV ≤ 2 then give (CW7-154′). Correct. The R16 bound fails exactly when A_X0 < 0 in a ΔP < 0 window, as C11 constructs.

**C2 (solver).** The fix precomputes C2, C3 for q < n_th − n_G using f = ρ (G = 1 there). The index bookkeeping is correct: every C2/C3 entry used is final.
moments_fast is indeed unaffected (its convolutions below threshold are identically 0 because m = 0). **Independent MC** (exact cascade: ii split Dirichlet(3/2, 3/2, 3/2),
λ = 3.55, θ_ii = 3/2, x = 8):
- with ω₀ = 0.05 the MC mean is 2.1553 ± 0.0022, and the grid gives 2.1526 (h = 0.01), 2.1531 (0.005), 2.1533 (0.0025): agreement, so the fix STANDS;
- with ω₀ = 0.054 the MC mean is 2.1326 ± 0.0027, but the coded h = 0.02 gives 2.0956 and h = 0.01 gives 2.1526. The reason: n_w = round(ω₀/h) quantises ω₀ to 0.06 and 0.05, so the
  h-sequence is non-monotone and Richardson extrapolation (2.2096) is wrong by 3.6%.

**Owed pitfall (LE-153 spec and L-H2):** "h must divide E_g, θ_iiE_g and ω₀ (ρ and p(x) are also read at x − ω₀). Otherwise the solver solves the problem with
ω₀,eff = h·round(ω₀/h) and h-Richardson is invalid. At the coded h = 0.02, ω₀ = 0.054E_g the mean N is biased by −1.7%." C6's O(h) test is at λ → 0, where ω₀
plays no role, so it does not cover this. C7's agreement with GAP-EF (F = 0.1147) is code-to-code at the same grid.

**C3 (LE-155).**
- Double commutator: ⟨[[p², V], p²]⟩ = 4m⟨V′²⟩ on eigenstates, using p²ψ = 2m(E − V)ψ; with 𝒯 = p²/2m² this gives ⟨(∇V)²⟩/(2m³). 1s: 4Z⁵∫_ε e^{−2Zr}r⁻²dr → 4Z⁵/ε.
- Polar term: D_ij(k, ω) = [k²δ_ij − k_ik_j − ω²ε_ij]⁻¹ → −(ε⁻¹)_ij/ω² for k² ≪ ω²|ε|, for any anisotropy. The k̂-independent tensor form is right; the R16 k̂ε⁻¹k̂ form was the longitudinal part only.

**C4 (r^M).**
- The algebra holds: ⟨n²⟩ = ΔS(1 + 2ΔS) (same-site ⟨aa⟩ = 0), W_⊥ = (S − ΔS)(1 + 2ΔS), LSWT S(1 + 2ΔS), relative defect ΔS/S (0.156 at S = ½).
- Two overclaims:
  - (i) W_⊥ is the full equal-time transverse weight, one-magnon plus three-magnon. The exact one-magnon weight is ≤ W_⊥, so ΔS/S bounds the LSWT overstatement of the one-magnon weight *from below*; it does not give its size.
  - (ii) ⟨n²⟩ is evaluated in the LSWT vacuum, so W_⊥ is itself O(S⁰)-accurate.
- The magnon-velocity renormalisation (energies, hence edges) is a separate nuisance not covered.
- **Replacement (errata §1.7, WP8-F-v3 §2.6, L-H4):** "r^M ≡ ΔS/S is the LSWT defect of the transverse sum rule (Casimir identity, LSWT vacuum) [D]; as the width
  of the one-magnon weight it is a lower estimate [E]".
- Using it as the one M width is acceptable as a declared choice, not as "derived".

## D. WP8-F-v3 FOM changes (scope 0d)
### D1. NR-1ph
- **Light mediator.** (2.3a″) re-derived: ∫dq q²F²η/c_ν with F² ∝ q⁻⁴ gives (1/ω_th − 1/(c_νq_up))η̄. Completeness then removes the branch sum.
  1910.10716 p.9 confirms: "the rate is dominated by the lowest detectable momentum transfer … the dependence on the target properties drops out", Eq. (35).
- **Missing correction.** The η argument at q₋ is c + ω_th/(2m_χc) = c + v_max·m_min^ac/m_χ. This O(m_min^ac/m_χ) term dominates below ≈ 1 MeV for soft lattices:
  CsI/Si = 0.11, 0.42, 0.58, 0.69, 0.82 at m_χ = 0.1, 0.2, 0.3, 0.43, 1 MeV (own run of the C27 model).
  **L-F4 leading-correction column:** add "O(m_min^ac/m_χ) shift of v_min (dominant within ≈ 30× the softer material's edge)".
  §0's "target-independent above the edge" → "… for m_χ ≫ m_min^ac of every compared material".
- **Heavy mediator.** (2.3b) at ω_th = 1 meV gives m_min^ac = 6.5 keV (Si) and 41 keV (CsI). The text "m_χ,edge ≈ 0.1 MeV (1 meV, (2.3b))" in §0, §2.3(a″), §5.1 and
  L-F1 is therefore wrong: 0.1 MeV is 1910.10716's regime boundary ("In the lowest mass regime, mχ ≲ 10⁻¹ MeV …", p.10).
  - Own ratios CsI/Si at 0.1, 0.2, 0.3, 0.43, 0.6, 1 MeV: 3.42, 6.09, 6.48, 5.60, 3.68, 2.03, against 1/c = 6.35. The 1/c_NR1 scaling holds to ±10% only for ≈ 0.2–0.4 MeV in this pair.
  - **Replacement:** "ℛ_NR1 ∝ 1/c_NR1 for a pair of materials when m_χ ≳ 5m_min^ac of the softer one and m_χ ≲ q_BZ/(2v_max) of the heavier cell (Si/CsI:
    ≈ 0.2–0.4 MeV at ω_th = 1 meV)".
  - c_NR1 = ⟨Σ_ν(q̂·ê_ν)²/c_ν⟩⁻¹ is the right scalar: it is the ratio of q-integrals with the 1/c_ν structure factor.
### D2. Polar bound
- **Reproduced.** Lossless o-ray 9.121, e-ray 9.571, axis-average 9.271; LST ε₀ 9.781/12.099; consistent bound 9.522; (8.1) 11.84; mixed R16 route 9.15. All partial-fraction
  residues are ≥ 0, i.e. interlacing holds. Interlacing is a needed hypothesis, implicit in "lossless factorised"; state it.
- **Hostile point.** The ω_L,max form needs ε₀ "of the same factorised model". That is only available from the mode list, which gives 𝓘_pol exactly. With measured
  ε₀ (9.3 ⊥, 11.5 ∥ [FT 1807.10291 via WP8-U]) the same formula gives:
  - 9.30 at ε_∞ = 3.2 (barely above the mode sum);
  - **9.05 at ε_∞ = 3.26 — below the mode sum 9.27**;
  - 9.75 at ε_∞ = 3.1.

  The (8.1) upper end with the same measured pairs stays ≥ 10.88 (10.88–12.01).
- **Replacement (§2.5 last sentence, IF-ERR7-1, IF-F1′):** "for ε-route materials (no mode data) rank by the (8.1) interval
  [(π/2)Δε⁻¹ω_T,min, (π/2)Δε⁻¹ω_T,max√(ε₀/ε_∞)]/ρ_T; the ω_L,max bound is a consistency statement for materials with mode data, not a ranking input".
- "Damping adds O(γ_L/ω_L)" (9.40 vs 9.12 on a truncated window) is [E], not [D].
### D3. 𝓠_Mig
- ∫(π/2)ω_pδ(ω − ω_p)ω⁻⁴dω = (π/2)ω_p⁻³.
- For supp L ⊂ [E_g, ∞): ∫L/ω⁴ = ∫(ωL)ω⁻⁵ ≤ E_g⁻⁵(π/2)ω_p².
- (26.1/16.6)³ = 3.887; 3.38/3.887 = 0.87. Correct. LiF's ω_p^{val} is [E], so the 0.87 is [E].
### D4. ²¹⁰Pb
- Own β integrals (allowed × NR Fermi) give f_<1 keV = 0.0438 (Q 63.5 keV, Z 83) and 9.65×10⁻⁴ (²¹⁰Bi, Q 1162 keV). The sum 86400(0.16·0.0438 + 9.65×10⁻⁴) = 689; 1/689 = 1.45 mBq/kg.
  Per kg Pb: 1.68 (PbS) to 2.34 (PbTe).
- The 84% branch deposits ≥ 46.5 keV minus at most one escaping Pb L X-ray (≲ 15 keV) — still ≫ 1 keV; the argument holds.
- Both β transitions are first-forbidden, and the relativistic Fermi function at Z = 83 enhances the low-energy tail. LU5′ lists both; ESTIMATED is the right status.
- ³H f = 0.0892 reproduced.

## E. Literature ratings and quotes
**E1. Ge EC lines (1607.04560).**
- Confirmed:
  - p.3 "L- and M-shell captures will produce weaker lines at approximately 1 and 0.1 keV";
  - p.10 "between 1.1 and 1.3 keV (the energies of the L-shell lines for 65Zn and 68Ge…)";
  - Table 1 p.25 gives E_L only for ⁷¹Ge, ⁶⁸Ge (1.30), ⁶⁸Ga (1.19), ⁶⁵Zn (1.10).
- **The inference "above the < 1 keV ROI: only M-lines … enter" is false.** The same table lists ⁴⁹V (→Ti) and ⁵⁵Fe (→Mn), produced at 2.8 and 4.6 /(kg·d) per the
  return's §4.4. Their L-shell lines lie at ≈ 0.56 and ≈ 0.77 keV (Ti, Mn L₁ binding energies [UNVERIFIED, standard tables]); ⁵⁴Mn (→Cr ≈ 0.70) and ⁵¹Cr (→V ≈ 0.63) likewise.
- **Replacement (errata §1.11, WP8-U-v3 §4.4, v4 `cosmo_EC_lines_subkeV`):** "the dominant ⁶⁵Zn, ⁶⁸Ga, ⁶⁸Ge, ⁷¹Ge L-lines (1.10–1.30 keV) lie above 1 keV; the L-lines
  of the lighter-daughter EC nuclides (⁴⁹V, ⁵¹Cr, ⁵⁴Mn, ⁵⁵Fe; ≈ 0.56–0.77 keV) and all M-lines are inside the sub-keV ROI".
**E2. 1910.10716 Table I c_LA — CONFIRMED defect for GaN, AlN, ZnO.**
- Table I p.2 prints c_LA^s = 4.17, 5.70, 4.18 ×10⁻⁵ (12.50, 17.09, 12.53 km/s). The method (p.13) averages ω_LA/q on a sphere of radius q ≈ 10 eV, deep in the
  linear regime, so the value must lie within the Christoffel LA range.
- With the measured C_ij of §A (GaN, AlN: 1110.1346 Table I; ZnO: cond-mat/0507217 Table III) and the JARVIS densities, the LA range tops out at 8.18, 11.34, 6.18 km/s
  (means 7.92, 11.05, 6.12). The printed values exceed every direction by ×1.53, 1.51, 2.03.
- Rating: **CONFIRMED** that Table I c_LA is inconsistent with the measured elasticity for these three. The cause is unknown; "suspect" can be upgraded for them.
  α-SiO₂ and NaCl stay UNRESOLVED (no measured C_ij read in full text).
- Caveat: the ZnO values come from films.
**E3. CaWO₄ ³H.** 1908.06755 p.4: "the observed 181W should be accompanied by a 3H component". The phrase "It is hard to be observed experimentally" was not
found verbatim in my extract (line-break damage possible); the "inferred" reading stands.
**E4. Eq. (35)/(37) pages** as in row 2b.

## F. CLOSED-AS-EXACT-GAP / specifications (scope 4)
**G-F6** (two missing steps; spec).
- **Physics.** ⟨S_κ^aS_κ′^b⟩ = δδJ(J + 1)/3 kills the coherent term; w_iso is the standard SD factor; P(¹H, 1 T, 10 mK) = tanh(0.102) ≈ 0.10. Both steps are genuine and
  sufficient for the zero-field class.
- **Spec defects:**
  - (a) the isotope list for "every survivor" omits **⁴³Ca** (CaWO₄, a SURVIVOR). For the COND set it also omits ¹H (PE), ¹³C, ¹⁰,¹¹B, ¹⁴,¹⁵N, ²⁵Mg, ⁶⁷Zn, ⁷⁷Se, ⁸⁷Sr,
    ⁴⁷,⁴⁹Ti, ⁹¹Zr, ²⁰⁷Pb, ²⁰⁹Bi, ³⁵,³⁷Cl, ⁵³Cr, ⁵⁵Mn, ⁵⁷Fe, ⁶¹Ni, ³³S, ¹⁸¹Ta. Generate the list from `isotopes[El]` and do not print a partial one.
  - (b) S^{inc,(1)}_κ = (q²/2M_κ)D_κ(ω)/ω is the cubic-site, angle-averaged form, and needs the normalisation stated (∫D_κ = 1 with the 1/3 absorbed, or ∫D_κ = 3 with
    q²/(6M_κ)). For the uniaxial survivors (Al₂O₃, TeO₂, γ-LiAlO₂) the q̂-resolved projected DOS Σ_ν|q̂·e_κν|²δ(ω − ω_ν) is required (a pitfall to add).
  - (c) e^{−2W_κ} is dropped in the T = 0 formula while the general statement keeps it; keep it.
  - With (a)–(c), the specification is sufficient.

**LE-153** spec: sufficient after the commensurability pitfall (§C2). **LE-154 gate, LE-177 Geant4 criterion** (≥ 100 nuclei ⇔ ≤ 10% statistical error): sufficient.

## G. Proposed LIMITS rows (scope 5)
| Row | Verdict | Correction |
|---|---|---|
| L-H1 | STANDS | – |
| L-H2 | STANDS WITH CORRECTION | validity/pitfall: grid commensurate with E_g, θ_iiE_g, ω₀ (§C2) |
| L-H3 | STANDS | [ABS]-level source declared |
| L-H4 | STANDS WITH CORRECTION | leading correction: "transverse sum-rule defect ΔS/S (lower estimate of the one-magnon defect)" (§C4) |
| L-F1 | STANDS WITH CORRECTION | heavy window as replaced in §D1; "0.1 MeV = (2.3b) edge" withdrawn |
| L-F2 | STANDS WITH CORRECTION | add the interlacing hypothesis; ω_L,max form only with mode data (§D2); 1807.10291 locators not re-read here |
| L-F3 | STANDS | – |
| L-F4 | STANDS WITH CORRECTION | 1910.10716 Eq. (35) p.9 quoted correctly; add O(m_min^ac/m_χ) as the leading correction (§D1) |
| LU5′ | STANDS | source [UNVERIFIED] declared; ESTIMATED is the right status |
| LT1 (Voigt-ordered) | STANDS | §A |

## H. Required changes (for the merger)
- **RC1** §A wording: "cyclic shear mis-indexing (C₄₄ ↔ C₆₆ for uniaxial)"; the C33 tolerance should match the 0.05 GPa printed.
- **RC2** errata §1.1: the 2 non-[E] dropped rows are GaAs S1 and SiO₂-q S1.
- **RC3** LE-153 spec, L-H2, cascade_gf.py docstring: add the commensurate-grid pitfall (h | ω₀, E_g, θ_iiE_g).
- **RC4** WP8-F-v3 §0, §2.3(a″), §5.1, L-F1: the heavy-mediator window as in §D1. L-F4 and §0: the O(m_min^ac/m_χ) correction for the light mediator.
- **RC5** WP8-F-v3 §2.5, IF-ERR7-1: ε-route materials ranked by the (8.1) interval; state the interlacing hypothesis.
- **RC6** r^M status: [D] as a sum-rule defect, [E] as the one-magnon width (errata §1.7, WP8-F-v3 §2.6, §4, L-H4, WP6 §5.2 row).
- **RC7** Ge EC lines: replacement text of §E1 (errata §1.11, WP8-U-v3 §0 row 6/§4.4, v4 row).
- **RC8** G-F6 spec: full isotope list from the table (⁴³Ca at least), the anisotropic projected DOS, normalisation and e^{−2W}.
- **RC9** WP8-U-v3 §5: upgrade 1910.10716 c_LA for GaN, AlN, ZnO from "suspect" to CONFIRMED-inconsistent with measured C_ij [FT 1110.1346 p.2, cond-mat/0507217 p.7].
  α-SiO₂ and NaCl stay pending.
- **RC10** CONVENTIONS row 36 (ERR-CW7 content CLAIMED): the content may move to VERIFIED with RC1–RC9 applied. None of the findings reverses a SURVIVOR verdict or a ranking
  sign; RC4–RC5 change which scalar the WP8-S revision may use.
