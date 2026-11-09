# R17 referee report VER-ERR-WP8 (hostile, isolated): returns/R17/WP8-errata.md

Referee VER-ERR-WP8, brief briefs/R17/VER-ERR-WP8.md. Read: the return, code/REV-WP8-S/, code/CW7/ (cascade_gf.py, checks.py, data/v4_changes.json), referees/R17/VER-ERR-CW7.md,
referees/R16/VER-WP8-S-v2.md (not used beyond the brief's pointers), returns/R16/WP8-S-v2.md, WP8-F-v3.md (§2.7 only), WP8-U-table-v4.csv (screens), CONVENTIONS §8, §13 rows 29, 38.
Literature (lit.py → literature/papers-r17-VER-ERR-WP8/, PDFs deleted, .txt kept): 2508.08858, cond-mat/9408044, 1910.10716, 1607.04560, 2310.05815.
Own checks (scratchpad, not in the repo; all < 1 min): independent cascade MC; independent lab-frame η (angular quadrature) → κ_η, onset, pair ratios; Christoffel solves (CaWO₄, Al, CsI);
sympy (cubic Rayleigh floor, Cauchy ν, first-order light expansion); ³H β fraction below 1 keV.

## Verdict table (scope 0–3)
| # | Item (errata §) | Verdict | Reason (one line; detail below) |
|---|---|---|---|
| 1 | §1 RC1 PE cyclic shift; C33 0.050 GPa | STANDS | PERM [0,1,2,4,5,3] gives old (C₄₄,C₅₅,C₆₆) = true (C₆₆,C₄₄,C₅₅); S3-C11 passes. Note: tolerance `round(ident,3) <= 0.05` equals the observed maximum (not a margin) |
| 2 | §2 RC2 dropped rows | STANDS | v4_changes.json: 13 dropped, 11 contain "[E]", the 2 others GaAs S1 [ABS], SiO₂-q S1 [UNVERIFIED] (re-read) |
| 3 | §3 CaWO₄ measured tensor | STANDS WITH CORRECTION | Numbers reproduced (c_NR1 4.578, c̄_LA 4.647, LA [4.36, 5.17], min eig 25.86, ρ 6.115, C₁₆ sign irrelevant). Source chain mis-cited: C1 |
| 4 | §4 CsI floor + B-floor model; lead | STANDS | Floor [D] re-derived (sympy); 1.726 km/s, model 2.316 (ν = 1/4), floor/ν→0 limits reproduced; independent check (C2) keeps the lead. Minor: C3 |
| 5 | §5 RC3 commensurate grid; C5c/C7 | STANDS WITH CORRECTION | Own MC agrees with the commensurate grid (C4); docstring −1.7% vs text −1.61%; 41/41 PASS reproduced but in 574 s, not 19 s (C4) |
| 6 | §6 RC4 heavy window (4.2 m_min onset, pairwise) | STANDS WITH CORRECTION | Code windows reproduced in kind, but the printed W_AB formula is not what is computed; "4.2" is not a per-material onset; the η(c+u) shift is omitted (C6) |
| 7 | §7 light factor 1 − (1+κ_η)m_min/m_χ | STANDS | Algebra re-derived (sympy, remainder o(u₋) relative); κ_η = 3.139 from an independently built η; spot values (TeO₂/Si 0.3 MeV: first order 0.870 vs full 0.88) |
| 8 | §8 RC5 ε-route; sapphire σ 3% | STANDS | Residues of 1/ε = (1/ε_∞)Π(ω² − ω_T²)/(ω² − ω_L²) scale as 1/ε_∞ at fixed modes; interlacing = positive residues; reading "consistency statement" is right |
| 9 | §9 RC6 r^M [D] defect / [E] width | STANDS | S^± creates odd magnon numbers in the LSWT vacuum, so W₁^LSWT − W₁ = ΔS + W₃ ≥ ΔS: "lower estimate" is correct |
| 10 | §10 RC7 Ge EC L-lines | STANDS WITH CORRECTION | 1607.04560 Table 1 (p.25) checked: K energies, the three E_L, and every nuclide named; E_L of light daughters is an extrapolation [E] (no E_L in the table). Omits ⁴⁴Ti/⁴⁴Sc (C7) |
| 11 | §11 RC8 G-F6 specification | STANDS WITH CORRECTION | "e_κν normalised on the κ sublattice" is wrong; ∫D_κ = 3 needs full-cell normalisation (C8) |
| 12 | §12 RC9 1910.10716 c_LA ratings | STANDS WITH CORRECTION | CsI CONFIRMED (q ≈ 10 eV ≪ π/a, so 1.379 is a sound speed); **CaWO₄ is CONFIRMED inconsistent, not "marginal"** (C9) |
| 13 | §13.1 row 38: only diamond promoted | STANDS | v4 screens rescanned: C is the only material whose sole non-PASS screen is S2 (S1, S3, S4 PASS). 2310.05815 p.1–2: two 0.175 g CVD crystals, W-TES, thresholds 19.7 and 16.8 eV, above ground |
| 14 | §13.2 DATA-ADDENDA (Al, YIG) | STANDS | Al c_NR1 6.628, c_LA,max 6.71 reproduced; ρ 2.698 from a 4.05 Å. Note: 0 K C_ij with room-T a (ρ at 0 K ≈ 2.73 [UNVERIFIED]; −0.6% in c), negligible |
| 15 | §14 VER-WP8-S rows 2–5, 9, 11, 12 | STANDS | Statement (ii) re-derived from ranking_v3.json (Ge only, excluding Migdal); 117 tiers; NiO ×0.832/×1.441; 262/124 = 2.11; ³H f_<1 keV = 0.0892 (own Fermi-function integral) |
| 16 | §15 L(k, ω) specification | STANDS WITH CORRECTION | Sufficient except the 𝓠_Mig k-cut (C10) |
| 17 | §16.1–16.3 ranking, r_mat variants, readings | STANDS | rank.py + checks.py rerun: 31/31 PASS (13.3 s checks, 52 s with rank.py); tiers and leaders verified from JSON. rank.py rewrites ranking_v3.json (runtime field), md5 changes (C11) |
| 18 | §16.4 next-target guide | STANDS WITH CORRECTION | Several "missing demonstration" cells omit COND screens; several "measurements" are literature reads (C12) |
| 19 | §17 owed texts (L-F1, L-F2, L-F4, L-H2, L-H4, NOTATION, CORRECTIONS) | STANDS WITH CORRECTION | L-F1, NOTATION m_on and §6 replacement texts inherit C6; L-EW1 needs the isothermal-B note (C3); the rest are exact and correctly targeted |
| 20 | Scope 2: 1910.10716 wrong (GaN, AlN, ZnO, CsI, CaWO₄) | see #12 | Table I (p.2) values re-read: GaN 4.17, AlN 5.70, ZnO 4.18, CsI 0.46, CaWO₄ 1.42 ×10⁻⁵c; App. A3 (p.13): ω_LA/q averaged on a sphere q ≈ 10 eV |
| 21 | Scope 3: new [D] results (cubic floor L-EW1, Cauchy ν, EW-7.1, 𝓘 ∝ 1/ε_∞, L-S3 factor) | STANDS | each re-derived; hypotheses stated correctly (Born stability; isotropy for Cauchy ν; flat lab-frame η at 0; fixed modes) |

**No SURVIVOR verdict, leader or tier changes under any correction below.** The corrections are wording, citation and one rating (CaWO₄).

## C1. CaWO₄ source chain (§3, §12, §17.3(e), IF-EW-3)
2508.08858 p.16 reads: "The distribution function … was obtained in [63] using the elastic constants C11=145.9, C33=127.4, C12=62.6, C13=39.2, C16=-19.2, C44=33.5, and C66=38.7
(GPa), taken from [73]". [73] is Farley & Saunders, J. Phys. C 5, 3021 (1972), "Ultrasonic study of the elastic behaviour of calcium tungstate **between 1.5 K and 300 K**"; [63] is
Malkin et al., PRB 96, 014116 (2017). The errata's "via its ref. [63]" is wrong. **Replace** in §0 header, §3 and §17.3(e): "quoting J. M. Farley & G. A. Saunders … via its ref. [63]" →
"quoting its ref. [73] (Farley & Saunders 1972, ultrasonic, 1.5–300 K; the temperature of the quoted set is not stated; also used by its ref. [63], Malkin et al. 2017)". The values
are quoted correctly. σ_ln 0.02 [E] is acceptable for a 1.5–300 K ultrasonic set (LA stiffening over that range is of order 1–2%).

## C2. CsI: independent check of the lead (§4)
(a) The floor: the cubic quartic form C₁₁ − 2(C₁₁ − C₁₂ − 2C₄₄)Σq̂ᵢ²q̂ⱼ² (sympy identity, residual 0), the endpoint differences 2(C₁₁ − C₁₂)/3 and 4C₄₄/3, hence
ρc_qL² ≥ B: **DERIVED, stands.** √(13.5 GPa/4.529 g cm⁻³) = 1.7265 km/s. Isotropic M = 3B(1 − ν)/(1 + ν) = λ + 2μ (sympy); M(ν = 1/2) = B. CsI c_LA: ν 0, 0.20, 0.25, 0.35 →
2.99, 2.44, 2.32, 2.07 km/s, as stated.
(b) Independent of the ν prior: with room-T ultrasonic CsI constants C₁₁ 24.5, C₁₂ 6.6, C₄₄ 6.3 GPa [UNVERIFIED, from memory; to be read, IF-EW-3] the Christoffel solve gives c_NR1 = 2.217 km/s,
**FOM 3.92** vs Si (8.694); ×1.08 stiffer (a 0 K guess) gives 2.300 km/s, FOM 3.78. The Voigt-average ν of that tensor is 0.255, inside U[0.20, 0.35]. Bi₂Se₃ (3.04) would need
c_NR1(CsI) ≥ 2.86 km/s, i.e. C₁₁ ≳ 37 GPa, ~50% above any plausible value. **The CsI 42-pool heavy lead survives the independent check**; it stays [E]-tagged until measured C_ij are read.
(c) 1910.10716's 1.379 km/s is a genuine long-wavelength value (App. A3 p.13: ω_LA/q averaged on a sphere of radius q ≈ 10 eV; π/a(CsI) ≈ 1.36 keV, so q/q_BZ ≈ 0.7%): the
rejection is not a dispersion artefact of the comparison. Its lattice constants (Table III: 4.671, 4.669 vs exp 4.567) indicate the DFT softening.

## C3. CsI inputs: B₀ and ρ (§4, L-EW1, §17.3(e))
cond-mat/9408044 Table I (PDF p.18) is correctly quoted (expt. a₀ 4.56 Å, B₀ 13.5 GPa, footnote a = ref. [11], Mao et al. 1989/1990, high-pressure XRD). Two corrections:
(i) this B₀ is an **isothermal room-T equation-of-state fit**, not the adiabatic B_S that bounds a sound speed; B_S from ultrasonic C_ij is ≈ 12.6 GPa [UNVERIFIED, C2(b)], floor 1.67 km/s
(1910.10716 still 17% below). L-EW1 leading-correction column → append "B_T (EOS fit) vs B_S (adiabatic) and T-dependence: ±7% in B, ±4% in the floor". The σ_ln(B) 0.07 covers this; say so.
(ii) ρ_T = 4.529 g/cm³ corresponds to a = 4.567 Å (room T), not the a₀ = 4.56 Å quoted (→ 4.550). Cite the a actually used. Effect on the floor 0.2%.

## C4. Cascade grid fix: independent Monte Carlo (§5)
Own vectorised MC of the exact model (carrier x ≥ θ_ii: ii with p = 1/(1 + λ√(x − ω₀)/Φ(x − 1)), Φ(y) = Γ(3/2)³y^{7/2}/Γ(9/2), Dirichlet(3/2,3/2,3/2) split of x − 1, else x → x − ω₀;
x = 8, λ 3.55, θ_ii 3/2; 4×10⁵ histories, seed 7, 3 s): **ω₀ 0.054: N̄ = 2.1294 ± 0.0009** (grid 2.12998, 0.7σ); **ω₀ 0.050: 2.1527 ± 0.0009** (grid 2.15336, 0.7σ);
ω₀ 0.060: 2.0975 ± 0.0009, i.e. −1.53% vs ω₀ = 0.054 in the continuum (the errata's −1.61% also contains the O(h) discretisation of the h = 0.02 run). The guard, commensurate_h
(0.002 for ω₀ = 0.054, θ 3/2) and the ω₀,eff = h·round(ω₀/h) reading are correct. **Corrections:** cascade_gf.py docstring "biased by −1.7% at h = 0.02" → "−1.61% (CW7-C5c)";
§0 header "41/41 PASS, 19 s" — on this box (4 cores) checks.py gives 41/41 PASS in 574 s; the runtime claim and the checks.py header "Runtime < 1 min" must be restated
as measured (the brief's "no heavy numerics" is met per call, not in total).

## C6. Heavy-mediator window (§6, L-F1, §17.1, §17.2 m_on)
Own η (lab-frame SHM of CONVENTIONS §8, angular quadrature, normalised; κ_η = 3.1393 matches 3.1401) and own rate integral (2.3a″):
(a) **The printed W_AB = [max(m_on,A, m_on,B), min(…)] is not what rank.py computes** (it computes the ratio (R_A/R_B)/(c_B/c_A) directly and takes the contiguous |g − 1| < 0.1 range)
and it contradicts the return's own adjacent windows: TeO₂/CaWO₄ starts at 0.052 MeV < 4.2·m_min(TeO₂) = 0.063 MeV. **Replace** the definition by "W_AB = the contiguous m_χ range,
capped at min(m_hi,A, m_hi,B), where |(R_A/R_B)(c_A/c_B) − 1| < 0.1; for c_A ≈ c_B it extends below either material's onset vs Si".
(b) **"4.2" is the onset against Si, not a per-material property.** With the per-material normalisation of the derivation (I₀ = ∫₀^{v_max}u²η du) the lower cut alone reaches 10% at
u₋ = 0.212 v_max (not 0.24), i.e. m_on = 4.73 m_min; including the η(c + u) shift the per-material 10% onset is 4.9–5.7 m_min for c = 1.5–6 km/s. The return's 4.16–4.25 (TeO₂,
CaWO₄, Ge, GaAs, CsI, NaI, Bi₂Se₃ vs Si, ranking_v3.json) arises because Si's own integral is ≈ 6% low (c-shift), which cancels part of the soft material's loss. The "4.0–4.5 over
the survivors" also fails for materials stiffer than Si, whose lower end is Si's (C 8.1, LiF 3.3, γ-LiAlO₂ 2.7 in units of their own m_min). **Replace** "m_on ≈ 4.2 m_min^{ac}(c_NR1)
(η-weighted 10% onset; 4.0–4.5 over the survivors)" → "against Si, the 10% onset is ≈ 4.2 m_min^{ac} of the softer material (4.16–4.25 for every material softer than Si; per material,
normalised to the c-independent integral, it is 4.7–5.7)" and "reaches 10% at u₋ ≈ 0.24 v_max" → "0.21 v_max".
(c) **Omitted systematic:** ∫u²η(c + u)du differs from I₀ at first order in c (dη/dv ≠ 0 at v ~ v_max/2), not O(c²/v₀²): the large-m_χ ratio to 1/c is 0.989, 0.956, 0.937, 0.914 for
c = 1.5, 6, 8.7, 12 km/s. Hence C/Si = 0.932 at every m_χ (outside any window), and **a common window "vs Si" does not give 10% pairwise agreement among the survivors**:
C/TeO₂ = 0.90 at 0.2–0.4 MeV (at the 10% edge). Add to §6 and L-F1 leading correction: "η(c + u) shift: (R_A/R_B)(c_A/c_B) → 1 − O(6(c_A − c_B)/v_max) at large m_χ (diamond/Si
−7%)". No heavy-row leader moves (C is last; TeO₂, CsI lead soft-vs-soft).

## C7. Ge EC L-lines (§10)
1607.04560 Table 1 (PDF p.25, "EC decays with half-lives above 10 days for 21 ≤ Z ≤ 33") gives E_L only for Cu, Zn, Ga daughters; the light-daughter E_L are an extrapolation [E], as tagged.
The ratio trend and the ≤ 0.61–0.87 keV bounds are arithmetically right. The list omits **⁴⁴Ti (→Sc, 60 y) and ⁴⁴Sc (→Ca)**, also in Table 1 with E_K 4.49/4.04 keV and L-lines
< 1 keV: add "⁴⁴Ti/⁴⁴Sc" to the replacement text (production in Ge not given in the paper; flag as unquantified).

## C8. G-F6 normalisation wording (§11)
"Σ_ν over the 3N modes and e_κν normalised on the κ sublattice" → "e_ν normalised over the cell (Σ_κ|e_κν|² = 1); completeness then gives Σ_ν|e_κν|² = 3 per k, i.e. ∫D_κdω = 3".
With sublattice normalisation the stated ∫D_κ = 3 and the q²/(6M_κ) prefactor would be wrong. Also state the k-average (1/N_k)Σ_k and the per-cell count of κ atoms. The rest
(q̂-resolved projected DOS for non-cubic sites, e^{−2W} kept, regenerated isotope list incl. ⁴³Ca) stands; the two missing steps are correctly identified.

## C9. 1910.10716 ratings (§12): CaWO₄ CONFIRMED inconsistent
1910.10716's c_LA is a sphere average (App. A3, p.13). The like-for-like measured quantity is the sphere-averaged LA speed, 4.647 km/s (C1 tensor); 4.257 km/s is **−8.4%** below
it and 2.3% below the slowest LA direction, i.e. below every direction. Against the errata's own σ_ln 0.02 that is > 4σ; the C_ij temperature range (1.5–300 K) moves LA by ~1–2%.
**Rating: CONFIRMED inconsistent (−8.4% vs the sphere average; below the LA minimum).** Replace in §12 row CaWO₄ and in the §12 replacement text "CaWO₄ 2.3% below its measured LA range
(marginal)" → "CaWO₄ 8.4% below the measured sphere-averaged LA speed and below the slowest LA direction: CONFIRMED inconsistent". GaN, AlN, ZnO: Table I values re-read
(4.17, 5.70 ×10⁻⁵c → 12.50, 17.09 km/s); the measured-C_ij comparison was VER-ERR-CW7's and was not re-fetched here (no change). CsI: CONFIRMED (C2c).

## C10. L(k, ω) specification (§15, scope 4)
It states what is computed, the level (RPA + local fields; TDDFT-ALDA rung), the method, five convergence criteria and six pitfalls; it is sufficient **except**: (i) 2011.09496 Eq. (6) is
valid only for k ∈ 1BZ (WP8-F-v3 §2.7), and 𝓠_Mig's d³k = 4πk²dk weight makes the result dominated by the cut; the specification must fix the k-domain of 𝓠 (1BZ Wigner–Seitz cell,
not a sphere of 5 keV) and require the cut-sensitivity (WS cell vs inscribed sphere) as a convergence item; the 0–5 keV k range is for ER only. (ii) Pitfall (e): "the BSE rung bounds
it" → "the BSE rung computes it" (BSE is not a bound). With these two edits the gap qualifies as CLOSED-AS-EXACT-GAP; the single missing step (the L(k, ω) computation itself) is correct.

## C11. Ranking code reproducibility (§16, §18)
rank.py (seed fixed) regenerated ranking_v3.json with identical readings (S2-C14 PASS) but a different md5 (72e022… → ae166e…) because it stores `runtime_s`. The "byte-unchanged"
claim concerns ranking_v2.json and CW7 ranking.json, which are unchanged (98a678…). Recommend dropping runtime from the JSON so S2-C15 can also pin v3. Note: running the checks as
instructed overwrote ranking_v3.json (content-equivalent); no other file of the return was written by this referee.

## C12. Next-target guide (§16.4): corrections
- **PbSe** (C/C/C/P) and **PbS** (C/C/C/P): missing demonstration lists only S2 and ²¹⁰Pb; add "mK operation (S1 COND) and phonon readout (S3 COND)". **PbTe** (P/C/C/C): add S3 readout.
- **h-BN**: S2 FAIL rests on an [UNVERIFIED] v4 row ("mm-scale (HPHT/flux)"); say so.
- "Single most rank-changing **measurement**": diamond C_ij (C row), LiF ε₀, GaSb low-T gap (Ge row), TeO₂ C_ij and CsI C_ij exist in the standard literature [UNVERIFIED: McSkimin &
  Andreatch 1972 (diamond), Ohmachi & Uchida 1970 (TeO₂), Vurgaftman et al. 2001 (GaSb gap)]: relabel these cells "literature read (IF-EW-3)", not measurements. The Pb-salt ε_eh,
  ²¹⁰Pb activity, α-quartz mode data, CsI ω_LO at low T and L(k, ω) entries are correctly measurements/computations.
- The rest (screens copied from v4 + row 38; P₁ and rank intervals; TeO₂ 6–8 in 42) checks against v4 and ranking_v3.json.

## Owed texts (§17): status
L-F2, L-F4, L-H2, L-H4, NOTATION (κ_η, Z_prim, ω₀,eff, ν_CsI, r^M), CORRECTIONS §19.13(a)–(d),(f),(g), §19.14, §19.15, IF-EW-1: exact and correctly targeted. Amend before merging:
L-F1 and §6/§17.2 m_on, W_AB (C6a–c); §17.3(e) and §3 citation (C1); §12/§17.3(d) CaWO₄ rating (C9); L-EW1 leading correction (C3); §10 list (C7); §11 wording (C8); §15 (C10).
Proposed LIMITS rows (scope 5): L-EW1 source quoted correctly (cond-mat/9408044 Table I p.18, expt. B₀ from ref. [11]); validity "cubic, Born-stable" right; leading correction as C3.
L-S1–L-S3: consistent with CONVENTIONS row 29 and the S3-C9 factor; "X_pole ≥ 1 is a prior" correct.

## Rerun
code/REV-WP8-S: `python3 rank.py && python3 checks.py` → **31/31 PASS** (checks 13.3 s; with rank.py 52 s).
code/CW7: `python3 checks.py` → **41/41 PASS, 574 s** (not 19 s); C5, C5b, C5c, C6, C7 (F 0.1139, ε/E_g 3.2185; quantised 0.1147, 3.2610) and C8 printed values identical to the return.
