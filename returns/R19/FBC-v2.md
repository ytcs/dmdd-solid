# R19 / FBC-v2: full-band carrier cascade in silicon (stage 1), corrected after REF-FBC-A and REF-FBC-B

Supersedes returns/R19/FBC.md (v1, kept unchanged) wherever the two differ. The referee reports are returns/R19/REF-FBC-A.md
(physics) and REF-FBC-B.md (reproduction). Code is in code/FBC/; checks.py gives **15/15 PASS**. The v2 analysis is in
analyze_v2.py and data/summary_v2.json; caches are in /root/work/FBC/. Run by Claude (LLM); not refereed.

## 0. What changed, by referee item
| item | v1 | v2 |
|---|---|---|
| A1 | "F < 0.119 in every variant supports a structural gap" | **withdrawn**: F = 0.101–0.115 within one model class, which cannot test the missing physics; the 2.5σ deviation stays unexplained |
| A2 | one-at-a-time ε band [3.92, 4.47] | joint corners (screening × phonon set × threshold R_x): **ε = 4.15 [3.95, 4.73] eV within the model class**, plus a model-class systematic of ≥ ±0.4 eV (Nielsen–Fischetti). Our run with NF-like choices (DFPT-ratio phonons for both carriers, no exchange) gives 4.11 eV, so the ≈ 0.6 eV gap to their GW/BSE 3.50 eV is unexplained |
| A3 | "Kotani omits the ½"; R_x = 1.12 below 2.9 eV | **Kotani's Eq. (5) agrees with ours**, including the ½ and the 0.5–1 range; threshold R_x = 0.75 (primary), with 0.5 and 1.0 carried in the band |
| A4 | static Cappellini as primary, unqualified | the static Cappellini primary is an **upper bound on the rate**. Static Resta lies *below* rpaw (×0.68 at 2–3.5 eV) and acts as a proxy for rpaw × z_qp. Dynamic band RPA (rpaw) lowers the rate ×0.37–0.65 and raises ε by +0.22 eV; it enters every corner |
| A5 | uniform D² × 0.6–1.6, values [UNVERIFIED] | asymmetric first-principles ratios (**electrons × 0.52, holes × 3.0**), separately and jointly; JR values cited from arXiv:2104.08998 Table III |
| A6 | P(≥2, 5 eV) [0.056, 0.155]; overcount [6.5, 17.7]; matched TVs at one ε | **P(≥2, 5 eV) = 0.097 [0.030, 0.173]; overcount 10.3 [5.8, 33]**; matched TVs at both ε edges; "94 %" restated as precision |
| A7 | phonons above threshold vs residual, not totalled | **total heat 71.6 % at 100 eV [70.2, 75.0]**; the cascade stops at E < E_g by convention |
| B1 | grid term missing | k-grid term in the budget: ±8 % on P(≥2) at 5 eV, ±17 % at 4.5 eV (twice the 12³ → 14³ shift); ε and F are converged |
| B2 | photon–DM 0.078, "exceeds the book's 0.062" | **at a matched 20³ grid: ≤ 0.15, not resolved** from the photon-seed grid error (0.11–0.14); the claim is withdrawn |
| B3 | C9 tested a toy MC; C11 halves shared seeds | C9 now tests mc.Model.run; C11 uses disjoint random seed subsets; C2 labelled trivial; C12 added |
| B4 | casc18_3 flag: "aliasing above ~60 eV" | the mechanism is (i) Gat extrapolating linearly beyond the grid top X·E_g (53.4 eV for X = 46) and (ii) NZ = 32 aliasing above ~85 eV. Fix: clip E in Gat and set NZ ≥ ⟨N⟩ + 10σ (C12) |

**A bug found and fixed in v2.** The stored labelled seed samples are ordered by q sample (radial bin). Any run using
fewer than all 20 000 per ω therefore took a q-biased subset. This affected nothing in v1, because every v1 P(N) run used
all 20 000, or a full 10⁴ set for the scissor seeds. It did affect the first v2 corner pass. All P(N) runs with 10⁴ events
were redone on random subsets (run_mc.py, key `off`). The one-sided ε/F runs use no seeds and were unaffected.

## Result (v2)
1. **ε_eh = 4.15 eV [3.95, 4.73]** (joint envelope within the EPM / diagonal-W / deformation-potential class, MC ±0.004).
   - F_eh = 0.114 [0.101, 0.115] (MC ±0.002).
   - Measured: 3.749 eV and 0.119 ± 0.002 (5.9 keV X-rays, 123 K).
   - **F**: within this model class F does not move toward 0.119 under any variation. The class cannot test the physics
     missing from both this model and the book's: plasmon creation and decay, excitonic final states, k-dependent DFPT
     couplings, keV-scale primaries. **The 2.5σ deviation is therefore unexplained, and stage 1 cannot decide whether
     it is structural.**
2. **P(N ≥ 2, 5 eV) = 0.097 [0.030, 0.173]** for the DM heavy seed. The step model overcounts the two-pair bin
   **10.3× [5.8, 33]**; the book gives 5.9×. Both band ends come from the two mixed-phonon corners c_lo and c_hi.
   Without them: P(≥2, 5 eV) [0.036, 0.141] and overcount [7.1, 28]. The floor of ≥ 6× is robust; ~30× is reached only
   in the single extreme corner (Resta + holes × 3 + R_x 0.5).
3. **ε is decided below 4.5 eV.** Tripling W_ii below 4.5 eV gives ε = 3.73 eV and P(≥2, 5 eV) = 0.21. Doubling it
   above 5 eV leaves ε = 4.15. The higher ε, despite a lower II/phonon crossing than NF's (4.72 vs 5.24 eV), comes from
   the soft-threshold region, where the full-band A(E) = 4–12.5 eV³ (§2).
4. **The computed electron/hole splits agree to TV ≤ 0.029**, which is 6 % of the α_RK spread (0.50), within the IP-EPM
   seed model. This is precision, not accuracy: the seeds have no screening, local fields or excitons.
5. **Memory ≤ 0.015 TV, a model-internal bound.** Every optical or intervalley phonon redraws k on the shell, so the
   test probes only first-collision k dependence. **mK vs 123 K: TV ≤ 0.016**, which is expected (n(61 meV) = 0.003).
6. **Photon vs DM: not resolved.** At a matched 20³ grid the full-band max is 0.15 (at 7 eV; ≤ 0.04 elsewhere). The
   photon seed changes by 0.11–0.14 between 12³, 20³ and 28³, while the DM seed changes by 0.009. Neither "exceeds 0.062"
   nor "below 0.062" can be claimed.
7. **Energy at 100 eV: pairs 28.4 %, total heat 71.6 %** (27.7 % emitted above E_g + 43.9 % residual kinetic energy
   thermalised after the stop at E < E_g).

## 1. Bands
Unchanged from v1 §1: refit form factors (−0.2343, 0.0558, 0.0676) Ry, residual band errors as tabulated there. v1 and
REF-B checked the band-number convergence: NB = 8/12/20 give the same near-threshold P(N).

## 2. Impact ionization: exchange, screening, threshold
**Exchange (A3).** Kotani–van Schilfgaarde's Eq. (5) is |M|² = ½(|M_D|² + |M_E|² + |M_D − M_E|²) = |M_D|² + |M_E|² −
Re M_D M_E*. This is our bracket, ½ included, and their stated GW-to-Kane factor of 0.5–1 is our R_x range. **v1's
statement that they omit the identical-particle factor was a misreading and is withdrawn.**

R_x above 3 eV is unchanged: electrons 0.84 (3 eV) to 0.66 (10 eV); holes 0.64 to 0.51. Below 3 eV the sampled ratio
is noise. v2 uses the bounded choice R_x = 0.75 for both carriers, the midpoint of the physical range [0.5, 1.0]. The
contact (same-state) limit at threshold is 0.5; final pairs in different valleys give ~1. Effect of the threshold value:

| threshold R_x | 0.5 | 0.75 (primary) | 1.0 | v1 (1.12 e / 0.73 h) |
|---|---|---|---|---|
| P(≥2, 5 eV) | 0.080 | 0.097 | 0.118 | 0.111 |
| ε_eh (eV) | 4.207 | 4.149 | 4.096 | 4.130 |
| F_eh | 0.110 | 0.114 | 0.113 | 0.114 |

R_x was computed with cap and Resta screening (they agree to a few % above 3 eV). It is applied unchanged to rpa0 and
rpaw, which is untested for rpaw.

**Screening (A4).** A static ε(q) ≈ ε₀ underestimates Re ε(ω) at the transferred energies 1–4 eV, which lie below the
E₁/E₂ peaks. The static **Cappellini** primary therefore gives an **upper bound on the ionization rate** and a lower
bound on ε within the class. This does not hold for static Resta: near threshold its rate is ≈ 0.68 × the rpaw rate
(2–3.5 eV), about where rpaw × z_qp (≈ 0.8) would be, so Resta acts as a proxy for rpaw plus z_qp rather than as a bound.
"Static screening bounds the rate" is therefore true for Cappellini only. The dynamic diagonal band RPA (rpaw, the GW-consistent form at first order):
- lowers the shell-averaged rate by ×0.62–0.65 at 2–3 eV and ×0.37–0.45 at 5–8 eV;
- matches Kotani's GW at 5 eV (rpaw × R_x ≈ 5 × 10¹³ s⁻¹, against ≈ 5 × 10¹³ read from his Fig. 2);
- raises ε to 4.37 eV and lowers P(≥2, 5 eV) to 0.068.

The primary is kept static for continuity with v1, and rpaw is in every corner. Local fields, z_qp ≈ 0.8 (another ≈ 20 %
reduction of the rate) and excitonic vertices are stage 2. Each of them lowers the rate, so the bias of the primary
points the same way as rpaw.

**Grid near threshold.** Shell-rate ratios 12³/10³ by window (C7, informational):

| window (eV) | 1.5–2 | 2–2.5 | 2.5–3 | 3–4 |
|---|---|---|---|---|
| electrons | 0.83 | 0.90 | 0.91 | 1.04 |
| holes | 1.76 | 0.98 | 1.03 | 1.07 |

The onset (p_ii = 1 % at 2.4 eV for electrons, 2.6 eV for holes) is quoted ±0.2 eV. REF-B's eo runs give P(≥2, 5 eV) =
0.129/0.117/0.105/0.109 on 8³/10³/12³/14³ and 0.055/0.047/0.041/0.045 at 4.5 eV. I take ±8 % (twice the 12³ → 14³
shift) as the grid term. ε and F are converged (12³ → 14³: +0.003 eV, ΔF = 0.002). A σ ∈ {0.05, 0.15} delta-width test
was not run; the grid term covers it.

**Where ε is decided (A2).** Diagnostic runs (screening cap, JR, R_x 0.75):

| run | ε_eh (eV) | P(≥2, 5 eV) | ⟨N⟩ 10 eV |
|---|---|---|---|
| primary | 4.149 | 0.097 | 2.381 |
| W_ii × 3 for E < 4.5 eV | **3.728** | 0.214 | 2.619 |
| W_ii × 2 for E > 5 eV | 4.150 | 0.103 | 2.384 |

So ε is set where the full-band kernels give A(E) = 4–12.5 eV³ (2.5–4.5 eV), well above the book's 5.674 and NF's ≈ 4.
Above 5 eV our A_e = 1.7–1.9 is about half of NF's. Ionizing more readily there does not lower ε, because almost every
carrier above 5 eV ionizes either way.

**Comparison with Nielsen–Fischetti (arXiv:2610.16949 [FT]):**
- They report ε_Si = **3.10 eV** with a DFT/TDDFT loss function and **3.50 eV** with GW/BSE. Both use DFPT phonons; neither
  includes exchange; both include plasmon emission. Their loss-function magnitude alone moves ε by 0.4 eV, and both values
  lie below experiment, whereas ours lie above.
- NF use DFPT phonons for **both** carriers. The corresponding run here (first-principles ratios e × 0.52 and h × 3.0
  together, no exchange; verifier run) gives **ε = 4.11 eV**. The electron-only scaling (4.022) is not the right mapping:
  the hole scaling raises ε back. The plasmon branch is absent here.
- The remaining **≈ 0.6 eV gap to their GW/BSE 3.50 eV is unexplained.** Candidates are the plasmon branch, the
  soft-threshold rate of our momentum-conserving EPM golden rule against their smooth loss-function rate, and the
  differences in bands and vertices. None was sized. Reaching experiment would need ≈ ×3 the cap rate (≈ ×4.6 the rpaw
  rate) below 4.5 eV.
- **Model-class systematic ≥ ±0.4 eV** (NF's own TDDFT→GW/BSE shift). This should be quoted next to the in-class band.
- The crossing comparison (4.72 vs 5.24 eV) mixes phonon-model and II differences and is not an II validation.

## 3. Phonons (A5)
The JR values used match arXiv:2104.08998 Table III ("previous works", Jacoboni et al.), as REF-A verified: g-LO
11 eV/Å at 62 meV; f-LA and f-TO 2.0 eV/Å at 47 and 59 meV; hole optical 6 eV/Å at 63 meV; acoustic 9.0–9.5 eV (e) and
5.0 eV (h). The small g-TA, g-LA and f-TA entries (< 2 % of the loss) were not verified in a fetched source. The same
table's first-principles couplings give energy-loss weights of **e × 0.52, h × 3.0** relative to JR (REF-A §3). The JR
set was fitted to transport below ~0.5 eV, so its use at 2–5 eV is an extrapolation and should be read as one.

| phonon set | ε_eh | F_eh | P(≥2, 5 eV) | ⟨N⟩ 10 eV |
|---|---|---|---|---|
| JR (primary) | 4.149 | 0.114 | 0.097 | 2.381 |
| e × 0.52 only | 4.022 | 0.115 | 0.125 | 2.450 |
| h × 3.0 only | 4.373 | 0.112 | 0.075 | 2.288 |
| first-principles ratios (e × 0.52, h × 3.0) | 4.234 | 0.112 | 0.109 | 2.344 |

The electron and hole shifts partly cancel in the joint set; separately they move ε by −0.13 and +0.22 eV.

## 4. Seeds
Unchanged (v1 §4). Two statements the referees asked for:
- **Indirect absorption.** The photon seed is direct-only, so it is defined above the direct edge (≈ 3.4 eV) and used at
  ω ≥ 4.5 eV. Phonon-assisted indirect absorption is not modelled.
- **Screened DM seed.** Not run. The in-medium weight 1/|ε(q, ω)|² varies by ≈ ×3 over the dominant 1–9 keV range. That
  is far less than the (q₀/q)⁴ heavy/light reweighting, which moves the P(N) split by ≤ 0.008. I estimate ≤ 0.01 TV [E].

**Matched-grid photon vs DM (B2).** Stage-1 share histograms on a Γ-centred 20³ grid (750 q samples): DM heavy and photon.

| comparison (max over ω ≥ 4.5 eV) | TV |
|---|---|
| energy-only cascade, photon vs DM: 12³ / 20³ | 0.098 (9.25 eV) / 0.103 (7 eV) |
| full-band cascade, photon vs DM, both 20³ (labels random on the shell) | 0.150 (7 eV); 0.035/0.021/0.037/0.009/0.014/0.020 at 5/6/8/10/15/20 eV |
| photon seed 20³ vs 12³, 20³ vs 28³ (energy-only) | 0.142, 0.110 |
| DM seed 20³ vs 12³ | 0.009 |

The DM seed is grid-converged; the photon seed (vertical transitions only) is not. The photon/DM difference is ≲ 0.15
and is not resolved from a photon-grid error of 0.11–0.14. The photon/DM ratio of P(≥2) at 5 eV (0.99 at 28³, 1.35 at
20³) is unresolved as well. A converged photon seed needs a tetrahedron or ≥ 40³ vertical-transition integration (stage 2,
cheap).

## 5. Cascade results (v2 primary: refit bands, cap, JR, R_x 0.75 below 3 eV)
**P(N|ω), DM heavy seed** (2 × 10⁴ events per ω; the light seed differs by ≤ 0.014):

| ω (eV) | P(1) | P(2) | P(3) | P(4) | P(5) | P(6) | ⟨N⟩ | ⟨N⟩ joint band |
|---|---|---|---|---|---|---|---|---|
| 4 | 0.993 | 0.007 | | | | | 1.007 | |
| 4.5 | 0.963 | 0.037 | | | | | 1.037 | P(≥2) [0.007, 0.076] incl. grid |
| 5 | 0.903 | 0.097 | | | | | 1.097 | P(≥2) [0.030, 0.173] incl. grid |
| 6 | 0.644 | 0.356 | | | | | 1.357 | P(≥2) [0.17, 0.46] |
| 7 | 0.321 | 0.669 | 0.010 | | | | 1.690 | |
| 8 | 0.069 | 0.849 | 0.082 | | | | 2.014 | P(≥2) [0.75, 0.97] |
| 10 | | 0.627 | 0.366 | 0.008 | | | 2.381 | [2.16, 2.47] |
| 12 | | 0.244 | 0.640 | 0.116 | 0.001 | | 2.874 | |
| 15 | | 0.008 | 0.423 | 0.499 | 0.071 | 0.001 | 3.634 | |
| 20 | | | 0.018 | 0.337 | 0.490 | 0.148 | 4.793 | [4.24, 5.04] |

**ε_eh, F_eh and energy (A7).** One-sided seeds, slope over 50→100 eV.

| | primary | joint band |
|---|---|---|
| ε_eh (eV) | 4.149 ± 0.004 | [3.95, 4.73] + model class ≥ ±0.4 |
| F_eh | 0.114 ± 0.002 | [0.101, 0.115] |
| b_N | 0.38 | [0.35, 0.46] |
| pairs / total heat at 100 eV | 28.4 % / **71.6 %** | heat [70.2, 75.0] % |
| heat split: above E_g / residual | 27.7 % / 43.9 % | [25.6, 33.8] / [41.2, 44.6] % |
| 𝒱_< + 𝒱_> + 2𝒱_<> (at 100 eV) | 0.107 + 0.352 − 0.348 = 0.111 | |

- **Stop convention.** The prompt cascade stops when every carrier has E < E_g; no ionization is possible below that.
  The residual (≈ 0.90 eV per terminal carrier) is booked, not simulated, and is emitted as phonons within ~ps. The
  split between "above threshold" and "residual" is set by this convention; only the total heat is physical. At mK the
  final step is exciton formation and recombination (binding ~15 meV), which is outside the model.
- **ε/F and the high-energy rule.** ε and F come largely from the region above 19.5 eV, which uses the high-energy rule
  (ionization with probability 1 and a DOS split, no plasmon branch). The hefree variant varies only the DOS shape
  (−0.03 eV). The plasmon branch, which dominates 10–100 eV losses in NF, is a stage-2 item for ε and F.

## 6. Comparisons
**As-is distances** (book cascade A_AB = 5.674 with its DM seed; v2 primary DM heavy). TV at fixed ω:

| ω (eV) | book DM | computed split in book | R–K α=1 | R–K α=∞ | step |
|---|---|---|---|---|---|
| 5 | 0.073 | 0.076 | 0.221 | 0.078 | 0.903 * |
| 6 | 0.080 | 0.109 | 0.287 | 0.214 | 0.644 |
| 8 | 0.098 | 0.104 | 0.123 | 0.364 | 0.151 |
| 10 | 0.214 | 0.197 | 0.268 | 0.582 | 0.634 |
| 15 | 0.204 | 0.194 | 0.216 | 0.158 | 0.501 |
| 20 | 0.243 | 0.227 | 0.251 | 0.241 | 0.852 |
| max (4.4–21) | 0.273 | 0.260 | 0.291 | 0.582 | 0.903 |

\* At 5 eV the step threshold E_g + ε = 4.91 eV lies 0.09 eV below the evaluation point, so the step TV at 5 eV is
largely a threshold artefact. Two-pair probability at 5 eV: full band 0.097; book 0.170; computed split in book 0.173;
α=1 0.318; α=∞ 0.019; step 1.

**Matched distances at both ε edges (A6).** The book cascade is recalibrated to each full-band ε (slope over 20–40 E_g):

| full-band run (ε, A_AB) | book DM | computed split | R–K α=1 | R–K α=∞ | step (same ε) |
|---|---|---|---|---|---|
| low corner (3.95 eV, 8.7 eV³) | 0.146 (6.75) | 0.121 (7.25) | 0.111 | 0.447 | 0.785 |
| primary (4.15 eV, 12.7 eV³) | 0.159 (6.75) | 0.141 (7.5) | 0.108 | 0.448 | 0.793 |
| high corner (4.73 eV, 32.7 eV³) | 0.204 (8.0) | 0.174 (8.0) | 0.124 | 0.496 | 0.829 |

The structural residual of the energy-only model at matched ε is **0.12–0.20 at 6–8 eV**, and ≤ 0.04 at 5 and 10 eV for
the primary (0.004–0.07 across the edges). It grows with ε, because a soft threshold then matters more.

**α_RK.** The computed splits (heavy, light; refit, scissor) agree to TV ≤ 0.029, which is 6 % of the α spread of 0.498
inside the book cascade, within the IP-EPM model. The book's q₀ seed is within 0.035 of them. This measures the
precision of the computed split, not its accuracy.

## 7. Uncertainty budget (v2)
The joint envelope covers the v2 primary, the one-at-a-time v2 variants (rpaw; FP; e × 0.52; h × 3.0; threshold R_x 0.5
and 1.0) and the 14 corners (screening ∈ {cap, Resta, rpaw} × phonons ∈ {JR, FP} × threshold R_x ∈ {0.5, 1.0}, plus
cap/e × 0.52/R_x 1.0 (c_lo) and Resta/h × 3.0/R_x 0.5 (c_hi)). Grid and MC terms are added. **Both ends of every band
come from c_lo and c_hi**, the mixed-phonon corners that pair a first-principles coupling for one carrier with JR for the
other. Without them: ε [4.02, 4.59]; P(≥2, 5 eV) with grid [0.036, 0.141]; overcount [7.1, 28]. Screening variants reuse the cap
final-state and pair-choice tables (REF-B); only the total rate changes.

| headline | primary | joint envelope | + grid | MC | model class (not in band) |
|---|---|---|---|---|---|
| ε_eh (eV) | 4.149 | 3.95–4.73 | ±0.003 | ±0.004 | ≥ ±0.4 (NF 3.10 → 3.50) |
| F_eh | 0.114 | 0.101–0.115 | ±0.002 | ±0.002 | unknown |
| P(≥2, 4.5 eV) | 0.037 | 0.009–0.065 | **0.007–0.076** | ±0.002 | |
| P(≥2, 5 eV) | 0.097 | 0.033–0.160 | **0.030–0.173** | ±0.002 | |
| step overcount, 5 eV | 10.3 | 6.2–30.7 | **5.8–33** | ±0.3 | |
| ⟨N⟩ 10 / 20 eV | 2.38 / 4.79 | 2.16–2.47 / 4.24–5.04 | ±0.02 | ±0.004 | |
| total heat, 100 eV | 71.6 % | 70.2–75.0 % | | ±0.1 % | |
| matched TV, energy-only (max, 6–8 eV) | 0.159 | 0.146–0.204 | | ±0.01 | |
| memory TV | ≤ 0.015 (v1, paired) | model-internal | | 0.013 | |
| photon − DM max TV | ≤ 0.15 at 20³ | — | photon grid 0.11–0.14 | ±0.02 | unresolved |

**Paired variants carried over from v1.** These ran with the v1 R_x and are quoted as paired differences against the v1
primary: memory (eo), 123 K, scissor bands, hefree. Their differences do not depend on the threshold R_x. The gap at
mK is 1.17 eV rather than 1.160; I estimate the shift at ≤ 0.002 in P(≥2, 5 eV) [E] and did not rerun it.

**CPU (v2).** About 2.2 CPU-h, single-threaded BLAS per process. This is 0.2 CPU-h over the 2 CPU-h allowance:
- 0.2 CPU-h was lost to an argument-passing error in the first batch;
- 0.35 CPU-h went to the random-subset rerun after the seed-ordering bug.

## Checks (code/FBC/checks.py, 15/15 PASS)
- C1–C8: as in v1. C2 is relabelled a trivial unitarity check. C7 adds the threshold windows (informational).
- **C9** (new): the production engine mc.Model.run, with the book's kernels swapped in, reproduces casc18_3's generating
  function to TV ≤ 0.007 over four seeds, 3 × 10⁴ events each. **C9ref**: the v1 reference MC, ≤ 0.0023.
- **C11** (new): runs with disjoint random seed subsets and independent RNGs (10⁴ events each) agree to TV ≤ 0.020; the
  largest ratio to the expected noise is 2.7 over 146 ω × seed cases.
- **C12** (new): the casc18_3 failure and its fix.
  - With the default grid X = 46, the variance at 60 eV comes out −0.33, against 1.81 with the grid extended to X = 90
    and NZ = 64.
  - The NZ = 32 slope F over 50→100 eV is 0.38; with NZ = 64 and X = 90 it is 0.1142, ε = 3.7494, matching the 20–40 E_g
    values.

## Symbols introduced/used
As in v1. New in v2:
- R_x^thr: R_x below 3 eV;
- the corner labels c_{scr}_{ph}_{thr};
- FP: the first-principles phonon ratios e × 0.52, h × 3.0;
- wlo, whi: diagnostic rate multipliers below 4.5 eV and above 5 eV.

## Interface flags (revised: what Ch18 should take)
- **IF-FBC-1 (18.1, exchange):** the Kane exchange factor is R_x = 0.66–0.84 (electrons) and 0.51–0.65 (holes) above
  3 eV, inside the 0.5–1 range that Kotani–van Schilfgaarde also state. It is uncomputed below 3 eV (0.5–1.0 carried).
  It lowers the rate by 15–50 %.
- **IF-FBC-2 (18.1-reductions, memory):** with deformation-potential phonons the first-generation memory is ≤ 0.015 TV.
  This is a model-internal bound: every intervalley or optical phonon redraws k, so only first-collision k dependence is
  tested. Physical momentum relaxation needs DFPT couplings.
- **IF-FBC-3 (18.3, α_RK):** full-band computed splits agree among themselves to ≤ 0.029 TV (6 % of the α spread) and
  with the book's q₀ seed to ≤ 0.035, within the IP-EPM seed model. This is precision, not accuracy.
- **IF-FBC-4 (WE 18.3, "5.9×"):** full band gives P(N ≥ 2, 5 eV) = 0.097 [0.030, 0.173] and a step overcount of 10.3
  [5.8, 33]. The band ends come from the corners c_lo and c_hi; without them the values are [0.036, 0.141] and
  [7.1, 28]. Ch18 may state "≈ 10×, at least 6×". The ~30× top comes only from the extreme corner (Resta + holes × 3 +
  R_x 0.5).
- **IF-FBC-5 (18.3, photon vs DM ≤ 0.062):** not resolved by the full band. The DM seed converges in k; the photon seed
  does not at ≤ 28³. The book's number should carry a seed-grid caveat of the same order.
- **IF-FBC-6 (18.4, first principles):** ε_eh = 4.15 eV [3.95, 4.73] within the class (model-class systematic ≥ ±0.4 eV;
  NF give 3.10/3.50); F_eh = 0.114 [0.101, 0.115]. Equivalent A_AB is 12.7 eV³ [8.7, 32.7]. ε is decided below 4.5 eV,
  where A(E) is 4–12.5 eV³. **F agrees with the book's 0.114 and stays below 0.119; that agreement does not show the gap
  is structural.**
- **IF-FBC-7 (18.1, phonon kernel at mK):** the mK and 123 K cascades agree to TV ≤ 0.016 at fixed E_g, as expected
  (n(61 meV) = 0.003); only E_g(T) matters.
- **IF-FBC-8 (casc18_3.py):** Gat clips the index but not the weight, so it extrapolates linearly beyond the grid top
  X·E_g (53.4 eV for X = 46) without warning. Separately, NZ = 32 aliases above ~85 eV. Fix: clip E (or assert E ≤ (K−1)h)
  in Gat, and set NZ ≥ ⟨N⟩ + 10σ_N. The book's uses (≤ 46 eV, X = 46) are safe.
- **IF-FBC-9 (sources):** PRB 108 155203 (arXiv:2308.03893) is GaN. The Si full-band reference is arXiv:2610.16949, with
  ε = 3.10/3.50 eV, a crossing at 5.24 eV and A ≈ 4.
- **IF-FBC-10 (18.2/18.4, energy partition):** at 100 eV the total heat is 71.6 % [70.2, 75.0] and pairs take 28.4 %. The
  above-threshold/residual split is a convention of the stop at E < E_g.

## Proposed LIMITS rows (revised)
| # | Formula (source) | Recovered as | Validity (v2) | Leading correction | Status |
|---|---|---|---|---|---|
| L-FBC1 | Energy-only random-k cascade, one constant A_AB (book 18.1–18.3; R–K 2004.10709 Eq. (8)) | iso-energy reduction of the full-band kernels with A(E) → const | recalibrated to the full-band ε (A_AB 8.7–32.7 eV³): TV 0.12–0.20 at 6–8 eV; ≤ 0.04 (primary) to ≤ 0.07 (edges) at 5 and 10 eV | energy shape of the rate ratio below 4.5 eV (soft onset at 2.4 ± 0.2 eV; A(E) 12.5 → 1.7 eV³) | [CALC], stage 1, within model class |
| L-FBC2 | Step model 1 + ⌊(ω − E_g)/ε_eh⌋ (1509.01598 Eq. (5.1)) | deterministic-price limit | ω < 4.4 eV only; P(≥2, 5 eV) overcount 10.3 [5.8, 33] | full P(N), seed and phonon competition | [CALC] |
| L-FBC3 | R–K Beta split, α_RK = 1, ∞ (2004.10709 Eq. (7)) | seed-replacement limit | α = 1: TV ≤ 0.11–0.12 at matched ε (0.29 as-is); α = ∞: 0.45–0.50 at 5–14 eV | computed split (precision 0.03) | [CALC] |
| L-FBC4 | Kane/Keldysh law W ∝ (E − E_th)^a | fit to the full-band shell average (static W) | a = 4.65 (e), 5.3 (h) over 1.4–6 eV; onset ±0.2 eV (grid); dynamic W lowers the rate ×0.37–0.65 | local fields, z_qp, excitonic vertex | [CALC] |
| L-FBC5 | Energy-only reduction (book eq:18.1-isoenergy) | full-band MC vs shell-randomised MC | TV ≤ 0.015 for 2–20 eV, model-internal (DP phonons redraw k) | DFPT, anisotropic g (stage 2) | [CALC], bound |
| L-FBC6 | Kane exchange factor (Kotani–van Schilfgaarde 0812.2923 Eq. (5)) | sampled R_x = Γ_full/Γ_D | 0.66–0.84 (e), 0.51–0.65 (h) above 3 eV; [0.5, 1] below | dynamic W in M_E; threshold sampling | [CALC] |

## Quotable for the book (verifier list, VER-FBC-v2 §7)
- **ε_eh = 4.15 eV**, in-class envelope [3.95, 4.73] (most of it [4.0, 4.6]), plus a model-class systematic of at least
  ±0.4 eV. Measured: 3.75 eV. NF obtain 3.10/3.50 eV, and our run with NF-like phonon and exchange choices still gives
  4.11 eV. Caveat: stage 1, EPM / diagonal W / deformation-potential phonons, no plasmon branch, static Cappellini
  primary.
- **F_eh = 0.114 [0.101, 0.115]**, the same as the book. It lies below 0.119 ± 0.002, *without* any claim that the gap is
  structural.
- **P(N ≥ 2, 5 eV) = 0.097 [0.030, 0.173]** (DM heavy seed, grid ±8 % included).
- **Step overcount ≈ 10×, at least 6×.** The upper end "~30×" may be quoted only with the note that it comes from one
  extreme corner (Resta + holes × 3 + R_x 0.5).
- **Total heat at 100 eV: 71.6 % [70.2, 75.0]**; pairs 28.4 %. The above-threshold/residual split is a convention.
- **Exchange factor R_x = 0.66–0.84 (electrons), 0.51–0.65 (holes) above 3 eV**, in agreement with Kotani–van
  Schilfgaarde's 0.5–1.
- **Qualitative only:**
  - memory ≤ 0.015 TV (model-internal);
  - mK vs 123 K ≤ 0.016 TV;
  - computed splits agree to 0.029 TV (precision within IP-EPM).
- **Do not quote:**
  - a photon-vs-DM number (unresolved);
  - the "≈ 3.9 eV" NF reconciliation;
  - "static screening bounds the rate" in general.

