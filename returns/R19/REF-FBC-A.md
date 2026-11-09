# R19 / FBC: referee report A (physics and methods)

Referee: Claude (LLM), an isolated hostile referee. I read the return (returns/R19/FBC.md), the brief, code/FBC/*.py, and the data/ and /root/work/FBC
caches. checks.py was rerun: **13/13 PASS**. Nothing in code/ or data/ was edited. The independent probes below were run from a scratch script
(scratchpad/ref/probe.py). It imports mc.Model and reuses the cached tables. The probes use energy-only (eo) mode, which the return shows is
equivalent to full mode to TV ≤ 0.015, with the DM heavy seed and 2 × 10⁴ events. Reference: the base eo run gives P(N≥2, 5 eV) = 0.108; the return's
full-mode value is 0.111.

| probe | P(≥2) 4.5 / 5 / 6 eV | ⟨N⟩ 10 eV | ε_eh, F_eh (one-sided, 50→100 eV) |
|---|---|---|---|
| base (12³, cap, JR, R_x as in the return) | 0.040 / 0.108 / 0.367 | 2.397 | 4.118, 0.111 (2×10⁴) |
| 10³ rate tables (same seeds, eo) | 0.047 / 0.117 / 0.382 | 2.410 | — |
| R_x = 0.5 below 3 eV (e and h) | 0.026 / **0.080** / 0.328 | 2.351 | — |
| phonons rescaled to DFPT/JR ratios: e × 0.52, h × 3.0 (see §3) | 0.053 / 0.129 / 0.383 | 2.363 | 4.18, 0.110–0.111 (2 × 2×10⁴); one 10⁴ run gave 0.119 (a 2.3σ fluctuation) |

## 1. ε_eh = 4.13 eV [3.92, 4.47], "no fitted constant": NEEDS CORRECTION
- The central value is reproducible (my eo run gives 4.118). The method is legitimate as a stage-1 number.
- "No fitted constant" is true, but the calculation still contains discretionary choices that move ε:
  - the primary screening is the static Cappellini model. The dynamic RPA (rpaw), which is physically preferable, gives 4.35, and Resta gives 4.47;
  - R_x below 2.9 eV is extrapolated as 1.12 (§2b). The return should say which variant gives which value. At present the reader cannot tell that
    every screening alternative moves ε away from the measured 3.749.
- **The band is not honest as stated.**
  - It is an envelope of one-at-a-time variants. Correlated variants were not combined (e.g. resta + D² × 1.6, or D² × 0.6 + R_x thr).
  - The phonon band varies D² uniformly for both carriers, but the literature spread is anticorrelated between electrons and holes (§3).
  - It does not reflect the loss-function sensitivity that the return's own source shows. Nielsen–Fischetti (arXiv:2610.16949, which the return read:
    abstract and §IV) obtain ε_Si = **3.10 eV** with a DFT/TDDFT loss function and **3.50 eV** with GW/BSE, both with DFPT phonons. The loss-function
    magnitude alone moves ε by 0.4 eV, and their result lies on the opposite side of experiment. The return cites this paper for the 5.24 eV crossing
    and A ≈ 4, but does not mention its ε values.
- **An unexplained tension.** The return's rate crossing (4.72 eV) is lower than NF's (5.24 eV). Its A_e(E) of 1.7–1.9 eV³ for 5–10 eV is about half
  of NF's ≈ 4. So above 5 eV the return ionizes more readily than NF, yet its ε is 18 % higher than NF's GW/BSE value. The excess must therefore come
  from the soft-threshold region (2.4–4.5 eV, where A_e = 4–12.5) and from the holes. The return should show this decomposition. A per-carrier ε
  contribution, or ε with A(E) frozen above 5 eV, would do.
- **Required.**
  - Quote ε for every variant explicitly.
  - Add a correlated-variant corner run (screening × phonons × R_x).
  - Add a discussion of NF's 3.10/3.50.
  - Restate the band as "one-at-a-time envelope within the EPM/diagonal-W/deformation-potential model class". A model-class systematic of at least
    ±0.4 eV, from NF, should be stated next to it.
## 2. Impact-ionization rate
**2a. Golden rule, Umklapp, factorisation: STANDS.** The factorisation into a carrier vertex and S^pair_GG′ is exact for a static diagonal w, and it
reproduces the brute-force sampled direct rate to 0.99/1.02 (C5). Umklapp over 27 G vectors converges (G 11 vs 8: ≤ 4 %).

**2b. Exchange and spin sums: the physics STANDS, but the literature claim and the threshold R_x NEED CORRECTION.**
- *Spin sum.* I rederived it. With σ₂ = σ₁ the amplitude is |M_D − M_E|². With σ₂ ≠ σ₁ the direct and exchange final states are distinct, giving
  |M_D|² + |M_E|². Summing over σ₂ and halving for the ordered sum over identical particles gives |M_D|² + |M_E|² − Re M_D M_E*.
  - Relabelling symmetry gives Σ|M_E|² = Σ|M_D|². C6 confirms this to 1.02.
  - Hence R_x = 1 − ΣRe(M_D M_E*)/(2Σ|M_D|²). By Cauchy–Schwarz, R_x ∈ [0.5, 1.5].
  - The exch.py formula and its normalisation against Γ_D = (4π/ħ)Σ|M_D|² are correct.
- *Kotani.* The return says that Kotani–van Schilfgaarde "omit the identical-particle factor" and that their extreme value is 0.75 (also in IF-FBC-1).
  **This is a misreading.**
  - Kotani's Eq. (5) is |M|² = ½(|M_D|² + |M_E|² + |M_D − M_E|²), which is exactly the return's bracket, ½ included.
  - The text says that the GW-to-Kane ratio "should be a factor in the range 0.5 to 1". That is the return's own result.
  - The 0.75 sentence concerns a different comparison: omitting the exchange contribution from the Kane formula.
  - Fix: rewrite the R_x paragraph and IF-FBC-1 as an agreement with Kotani, not a correction of Kotani.
- *Threshold R_x.* Below 2.9 eV the raw window ratios are noise (0.38 to 362, Rx_e_raw in rates_*.json). The primary run replaces them with the first
  robust pooled value, **1.12**, clipped to [0.5, 1.5]. That is, exchange is assumed to *enhance* the rate near threshold.
  - Physically this is the wrong direction. At threshold, the minimum-energy final configuration puts the two electrons in the same state, so M_E →
    M_D and R_x → 0.5. For final pairs in different X valleys the limit is ~1.
  - The "rxthr" variant (0.81) does not bracket this. My R_x = 0.5 (< 3 eV) probe gives P(≥2, 5 eV) = 0.080 against 0.108. That is a −26 % shift, and
    the step overcount becomes 12.5.
  - Required: make 0.5–1.0 the threshold range, with the central value at about 0.75 or justified otherwise, and propagate it.
- *Screening dependence of R_x.* The cap and resta raw ratios agree to a few % above 3 eV, so applying cap R_x to resta/rpa0 is acceptable. For rpaw
  it is untested (minor).

**2c. Screening (double counting or omission?): STANDS for double counting; NEEDS CORRECTION on the primary choice.**
- The golden rule with |w(q)|² = |v/ε(q)|² multiplying the bare pair spectrum S equals RPA Im W = v² Im ε/|ε|². Nothing is counted twice, provided S
  is the bare (unscreened) pair spectrum, as it is.
- *Omitted:* local fields (G ≠ G′ in ε⁻¹), the z_qp factor and excitonic vertices. All three are listed for stage 2, which is acceptable.
- *Primary choice.* The transferred energies near threshold (1–4 eV) lie below the Si E₁/E₂ peaks, where Re ε(ω) exceeds ε₀ = 11.7. A static ε₀-based
  W therefore overestimates the rate, by ×2 at 5–8 eV judging from the return's own rpaw/cap ratio.
  - The dynamic form (rpaw) is the physically consistent GW choice.
  - With R_x it also matches Kotani's GW better at 5 eV (rpaw × R_x ≈ 5e13 against GW ≈ 5e13; cap × R_x ≈ 1.1e14).
  - Either adopt rpaw as primary, or state that the primary is the static upper bound of the rate and that ε is therefore biased low within the band.

**2d. Rate fit, Kotani ×2.3, crossing: STANDS, with caveats.**
- The fit P(E − 1.17)^4.65 is correctly described as a fit, not a law.
- The ×2.3 Kotani agreement is read by eye from a log plot, so it cannot discriminate between the screening variants.
- The crossing at 4.72 eV against 5.24 eV compares a deformation-potential phonon rate with NF's DFPT rate. The difference mixes the phonon and II
  errors and should not be read as an II validation.

**2e. Is 12³ adequate near threshold? STANDS for P(N) and ε; NOT for the onset.**
- C7's DOS-weighted mean |ln ratio| hides the threshold window. Directly from the cached rates:
  - electrons at 1.4–1.6 eV: W₁₂/W₁₀ = 0.16–0.26;
  - holes at 1.6–2.1 eV: ×1.6–2.8;
  - electrons at 2.1–2.6 eV: within ±25 %;
  - above 2.9 eV: within ±16 %.
- So the "p_ii = 1 % at 2.38 eV" onset (Result 6 / IF-FBC-6) is only grid-converged to about ±0.2 eV. The σ = 0.1 eV Gaussian also produces non-zero
  rates below E_g (2.5e6 s⁻¹ in the 0.875 eV bin), which the MC zeroes.
- The cascade observable is robust. My 10³ vs 12³ probe gives P(≥2, 5 eV) = 0.117 vs 0.108 and ⟨N⟩(10 eV) = 2.410 vs 2.397, an ~8 % systematic on
  P(≥2) at 5 eV.
- Required:
  - replace C7's metric with windowed ratios over 1.5–4 eV, plus a σ ∈ {0.05, 0.1, 0.15} test;
  - quote the onset with a ±0.2 eV band;
  - add the grid term to the P(≥2) band.
## 3. Phonons (Jacoboni–Reggiani values "from memory")
**Values: STANDS (correct), but the [UNVERIFIED] tag should be replaced by a citation.** The open source arXiv:2104.08998 (Table III, "previous
works", ref. a = Jacoboni et al.) lists:
- g-LO 11 eV/Å (= 11 × 10⁸ eV/cm) at 62.16 meV;
- f-LA 2.0 eV/Å at 47 meV and f-TO 2.0 eV/Å at 59 meV;
- holes: optical 6 eV/Å at 63 meV, acoustic 5.0 eV;
- electron acoustic 9.0–9.5 eV.

These match phonon.py. The small g-TA/g-LA/f-TA entries (0.5, 0.8, 0.3 × 10⁸ at 12, 18.5, 19 meV) match the standard JR table as I know it. I did not
verify them in a fetched source, but they carry < 2 % of the energy loss. ρ and u_l are standard. The full-band form W_j = (Z_j/Z_tot)πD_j²
g_t/(ρω_j), with a per-spin DOS, reduces to the JR valley formula. I checked the units and the 1/6 valley share.

**The D² × 0.6–1.6 band: NEEDS CORRECTION.** The same table gives first-principles couplings: g-LO 3.86, f-LA 1.83 and f-TO 3.55 eV/Å, and hole
optical 10.45 eV/Å.
- In the energy-loss weight Σ Z D², the electrons fall to **0.52 × JR** and the holes rise to **3.0 × JR**. The literature spread is anticorrelated
  between the carriers, and for holes it lies well outside 1.6.
- My probe with this rescaling gives P(≥2, 5 eV) = 0.129, ε = 4.18 and F = 0.110–0.111. It stays inside the stated bands only because the electron and
  hole shifts partly cancel.
- Also, the JR set was fitted to transport below ~0.5 eV. Its use at 2–5 eV follows standard full-band MC practice, but should be stated as an
  extrapolation.
- Required: separate e and h coupling variants covering 0.5–1.6 (e) and 0.6–3 (h), and a citation for the JR values.

**"mK vs 123 K changes nothing beyond noise": STANDS physically, with a labelling fix.**
- The T123 variant adds absorption (× n) and stimulated emission (× (n+1)) to the intervalley and optical modes. What matters for P(N) is ionization
  per unit of energy lost.
- The net loss rate per mode is ħω[(n+1)g(E−ħω) − n g(E+ħω)] ≈ ħω g(E) for E ≫ ħω. The thermal correction is of order n·ħω·d ln g/dE. Here n = 0.003
  for the 61 meV g-LO, which carries 78 % of the loss, and the modes with n ≈ 0.2–0.5 (12–19 meV) carry ~1 %.
- So the null result (TV ≤ 0.016; ε 4.126, F 0.112 at 123 K) is expected, not accidental.
- Defects (minor):
  - acoustic intravalley emission keeps its T = 0 form at 123 K. Its net loss is negligible, but it should be stated;
  - the return itself says that 1.160 eV is the 123 K gap and that the gap at mK is 1.17. So the "mK primary" is run at the 123 K gap. Rerun at 1.17,
    or quote the shift (an estimated ≤ 0.005 in P(≥2, 5 eV));
  - sub-E_g carriers are terminal, so thermal up-scattering is ignored (negligible).
## 4. Seeds and photon/DM ≤ 0.078: NEEDS CORRECTION (minor)
- The machinery is sound: the q → 0 vertex matches the optical vertex to 0.3 % (C10), and the per-event energy identity holds.
- The DM seed uses unscreened |ρ_cv|². The in-medium DM–electron rate is proportional to the loss function Im(−1/ε(q, ω)), i.e. a 1/|ε(q, ω)|²
  q-reweighting at fixed ω. The heavy/light spread (≤ 0.008) suggests the effect is small, but it was not tested. Required: one screened-seed run, or
  a statement.
- The photon seed exists only above the direct edge (≈ 3.4 eV), with indirect absorption omitted. That is acceptable at ω ≥ 4.5 eV and should be
  stated.
- 0.078 ± 0.013 (MC) + ≤ 0.02 (seed grid) is not significantly different from the book's 0.062. No screening or phonon variant was run for the photon.
  Restate as "0.078 ± 0.02, consistent with 0.062". IF-FBC-5's "the 12 % photon excess is not robust" is fair.
## 5. P(N≥2, 5 eV) = 0.111 [0.056, 0.155], step overcount 9.0 [6.5, 17.7], TV distances
- **Central values: STANDS.** The arithmetic checks out:
  - overcount = 1/P(≥2);
  - TV(step) at 5 eV = 1 − P(1) = 0.889;
  - the TV tables agree with summary.json and matched.json.
- **Bands: NEED CORRECTION.** Missing from the band:
  - the threshold R_x (0.080 alone);
  - the 10³/12³ grid term (+8 %);
  - correlated corners. Resta screening (0.056) combined with R_x 0.5 would plausibly reach ≈ 0.04, i.e. an overcount of ≈ 25. An honest band is
    roughly [0.04, 0.16], with an overcount of [6, 25]. The qualitative statement, that the step model overcounts by a large factor of ≥ 6, is robust.
- **Step TV 0.89.** This is a threshold artefact. At 5 eV the step threshold (E_g + ε = 4.91 eV) lies 0.09 eV below the evaluation point. Quote the
  maximum together with this context. A TV-at-fixed-ω table is more informative than "max".
- **Matched distances.** The book cascade recalibrated to A_AB = 12.3 gives 0.16; RK gives 0.28/0.10 (α = 1) and 0.57/0.45 (α = ∞). These carry no
  bands, and the recalibration target ε = 4.13 itself has an 8 % band. Required: recompute the matched TVs at the band edges of ε (e.g. A_AB
  recalibrated to 3.92 and 4.47). Otherwise "structural residual 0.11–0.16 at 6–8 eV" and L-FBC1's validity cannot be quoted as numbers.
## 6. Electron/hole split removes ≥ 94 % of the α_RK spread; memory ≤ 0.015
- **α_RK: NEEDS CORRECTION (wording).** "Removes 94 %" compares the α spread (0.498) with the spread among four computed splits (heavy/light × two EPM
  calibrations). All four share independent-particle, unscreened EPM vertices with no local fields and no excitons. That measures the precision of the
  computed split, not its accuracy. Restate as "the computed splits agree to TV ≤ 0.029 within the IP-EPM model (6 % of the α spread)". IF-FBC-3's
  "closed at the 0.03 level" should carry the same qualifier.
- **Memory ≤ 0.015: STANDS as a model-internal bound** (the return says so).
  - By construction, every optical or intervalley phonon event (≥ 90 % of collisions near threshold) re-draws k uniformly on the shell. Memory can
    therefore survive only until a carrier's first phonon event.
  - So the test probes the k-dependence of W_ii at the first collision and of the II final-state tables, not physical momentum relaxation.
  - Keep the caveat in IF-FBC-2 and L-FBC5 verbatim. "Justified at that level in Si" overstates what was shown.
## 7. Energy partition at 100 eV (28.6 / 27.5 / 43.9 %): STANDS physically; labelling NEEDS CORRECTION
- The pair fraction is E_g/ε (1.16/4.06 per realised pair at 100 eV, including the offset b_N). The residual kinetic energy is 43.9 eV/24.64 = 1.78 eV
  per pair, i.e. a mean of 0.89 eV per terminal carrier (77 % of E_g).
- This is sensible. Carriers drift down through the soft-threshold region by phonon emission and stop just below E_g. Products of near-threshold
  ionizations start low. The value is close to the book's 1.66 and below the parabolic-band Klein value (9/5)E_g ≈ 2.1 eV.
- **The cascade is not run to completion.** It stops when E < E_g, and the residual is booked, not simulated. That is correct for N, because no
  ionization is possible below E_g. However:
  - in a real crystal the 43.9 % is subsequently emitted as phonons within ~ps, so the physical heat fraction is 71.4 %;
  - the split between "phonons above threshold" and "residual" is a convention set by the termination at E_g, not a physical observable. The brief
    asked for "then thermalized by phonon emission". Required: state the total heat (71.4 %) and the convention. At mK, also state that the final step
    is exciton formation and recombination, outside this model (the exciton binding of ~15 meV is negligible energetically).
- The high-energy rule (II with probability 1 above 19.5 eV, DOS split, no plasmon channel) affects the 50–100 eV partition. The "hefree" variant
  probes only the DOS shape, not the missing plasmon branch, which dominates losses at 10–100 eV (NF). Name it as a stage-2 item for ε/F.
## 8. "F < 0.119 in every variant supports a structural gap": FALLS as an inference (the numbers stand)
- The numbers are robust. F = 0.110–0.114 across all variants. My anticorrelated-phonon probe gives 0.110–0.111 at 2×10⁴ events (an earlier 10⁴ run
  gave 0.119, consistent at 2.3σ). F is decoupled from ε: ε moves by 14 % while F moves by ≤ 0.004.
- But that insensitivity is exactly why it cannot support the inference.
  - Every variant shares the model class, because all of them reduce to a random-partition energy cascade. The book's energy-only model gives the same
    0.114. F ≈ 0.11 is a generic property of that class, so agreement among its members says nothing about whether the missing physics would close a
    gap of 0.005 (2.5σ of the measurement).
  - That missing physics includes plasmon creation and decay, excitonic final states, k-dependent phonon couplings, and the keV-scale (5.9 keV X-ray)
    primary cascade behind the measured 0.119.
  - A model that misses ε by 10 % cannot certify a 4 % effect in F as "structural" rather than as a model error.
- Also: the MC error (±0.002) is comparable to the gap, and the 0.119 ± 0.002 measurement is at 123 K and keV energies, whereas F_eh here is a 50→100
  eV slope.
- Required: replace it with "F_eh is insensitive to every input varied (0.110–0.114) and lies below 0.119, as in the book. Stage 1 cannot decide
  whether the gap is structural, because the varied inputs do not include the physics absent from both models." Soften IF-FBC-6 accordingly.
## 9. The Nielsen citation flag: STANDS (confirmed)
- arXiv:2308.03893 (Nielsen, Van de Walle, Pantelides, Schrimpf, Fleetwood, Fischetti) studies thermalization "in wurtzite GaN" (abstract). Its
  reference list (literature/papers-FBC/2610.16949.txt, line 880) cites this work as "…thermalization in semiconductors, Phys. Rev. B 108, 155203
  (2023)". This ties the brief's PRB number to the GaN paper.
- The redirection to arXiv:2610.16949 for Si is correct. However, the return should also quote that paper's ε_Si = 3.10/3.50 eV (§1).
## Required fixes: the "Required" items of §§1–8; priority: §8 withdrawal, §2b Kotani/threshold R_x, §1 and §5 bands.
## Overall verdict: **ACCEPT WITH CORRECTIONS**
The engine is careful. Its pieces are sound: the energy identity, the book-mode reproduction, the factorised rate checked by brute force, the correct
spin sums and the correct phonon values. The headline qualitative results survive my probes: the large step overcount, F ≈ 0.11 with no free
parameter, negligible memory within the model, and a null 123 K effect. The required changes are bands and wording. One inference (the structural F
gap) must be withdrawn, and the exchange literature claim corrected. No headline number moves outside a corrected band.

