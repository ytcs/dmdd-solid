# Chapter 15 editor notes

## 15.3 drafted (2026-11-06; ~3,800 words detex; no box per SPINE; 1 F row)
- Overlap with 15.2's "Mean free path at the edge" (tab:15-edge): 15.3 points to it and adds only the local dirty-limit Mattis–Bardeen ratio (0.235/1.302/1.259 at y = 2.2/3/5, matching the validated compute record). Decide at review whether to merge the two passages.
- PRIORITY derivation check: sheet screening factor [(ε_a+ε_b)/(q_∥d)]² for films thinner than 1/q (eq:15.3-sheet); 540 for the 50 nm example. Not found stated in the DM literature.
- E.20: WSi k_F𝔩_e ≈ 1 → "a few" (1.8–5.5 from transport). Fix at the App. E pass.
- Al v_F = 6.67e-3 with k_F = 1.75 Å⁻¹ implies m* = 1.012 m_e; 6.4's E_F = 11.7 eV gives 6.77e-3. Align book-wide.
- Attributions: Anderson 1959 (unread, credit only); QROCODILE plasmon width Γ = 0.1 E_F, implementation inferred; the WSi interaction-disorder statement has no citation. Review must check.
- Results: 50 nm Al film normal-state loss = 24× clean at keV-mass momenta, = ε₀ωρ_el (residual resistivity fixes it); the Lindhard function at ω + iγ_rel gives twice the Drude tail for q𝔩_e ≪ 1 (check: Mermin correction).

## 15.2 drafted (2026-11-06; ~2,410 words + table + box; D.39 ~560 words; Limit Check 15.2a; 1 F row)
- SUBSTANTIVE: the SPINE edge values (0.33–0.40 at y = 2.2 … 0.94–0.96 at y = 10) are the bare bubble, which violates charge conservation. They are replaced by the validated conserving response (DC-41, quoted per REF-DC-41 §7): 0.87/1.00/1.07/1.07/1.02 × 𝔤_I L^nor at y = 2.2/2.5/3/5/10, with the mean-free-path range stated. The one-sided nuisance is upward (+0.8 to +9.1 % for y ≥ 3). Keep the y < 3.8 mask. Update SPINE, LIMITS and SOTA at the merge.
- 15.1 says bare is within 10 % of conserving only at y ≥ 9.4; the root-finder gives 9.2 → fix 15.1.
- 15.1's ω_AB (Anderson–Bogoliubov) clashes with NOTATION's Alig–Bloom entry (E.13): rename.
- v_F subscript: upright book-wide (15.1 uses italic).
- 𝔣_L(ν) with ν = ω/qv_F clashes with the phonon branch ν: rename (ruling at review). L^BCS NOTATION row unused → L^bare/L^cons.
- Gan et al. 2609.06423 evaluate the bare BCS loss only numerically; the closed form is the book's D.39.
- The disorder columns come from data at v_max/v_F = 0.39, not 0.397 (caption says so; ≤ 0.004).
- Strong-coupling (frequency-dependent gap) correction unsized: DEFERRED/nuisance row.
- The final 15.2 text (sentence splits) has not been rebuilt.
- 15.1/15.2 overlap handled: 15.2 cut to what 15.1 lacks.

## 15.4 drafted (2026-11-06; ~3,470 words + summary file ~1,370 + D.40 ~1,420; Limit Check 15.4a; 3 F rows)
- TOP PRIORITY (new claim, large effect): the uniform spin current of a singlet superconductor breaks pairs by itself at q → 0 (in Nambu form σ_z p → τ_z-type, which does not commute with Δτ_x), so a clean superconductor absorbs ALPs directly. Clean Al at 0.72 meV: g_aee = 5.1e-13 for 3 ev/kg-yr, vs 5.6e-9 from the phonon-assisted σ₁ that published projections use (Hochberg–Lin–Zurek Eq. (22); Mitridate et al. Sect. V). Support: the f-sum gives exactly (π/2)ω_p² (the normal spin Drude weight), and the dirty limit conserves it to 0.05 %. The review must:
  (a) re-derive it independently;
  (b) check the ALP NR operator (σ·p/m with ȧ, vs ∇a·σ) and its normalisation;
  (c) check the role of spin–orbit coupling in real Al (it breaks σ·p conservation in the normal state; does it change the weight or the conclusion?);
  (d) search the literature (INSPIRE/arXiv) for prior treatment of ALP absorption via the spin current in superconductors, including Mitridate et al. 2106.12586 Sect. V and its citations, and state whether published projections omit it or exclude it for a reason;
  (e) check that the weight sits in the 2Δ edge region with the right coherence factor.
  Until verified, no downstream use; NOVELTY check after the review.
- Open items stated in the text but not in SPINE: the coherence factor of phonon-assisted spin-current absorption near the edge; scalar absorption near the edge (couples to the amplitude channel). Add them to the SPINE open problems at the merge.
- Free-electron ω_p: 15.78 eV (15.4) vs 15.7 eV (15.3). Unify.
- E.20 N_s, P_s (Eliashberg) clash with 7.1's N_s; 15.4 uses N^El, P^El. Fix E.20 at the App. E pass.
- The free-electron α²F_tr is wrong by 1.25e4 at low frequency (umklapp). The phonon-assisted rate within a few meV of the edge needs a first-principles α²F_tr: DEFERRED.
- Strong coupling: if each current eigenvalue carries 1/(1+λ_tr), the rate changes by 0.52; which factors survive is open.

## 15.1 drafted (2026-11-06; ~3,610 words detex; chapter opening + map; Limit Check 15.1a; 2 F rows)
- Conserving response in closed form (eq:15.1-Rcons) via one pair function F_μ. Implemented independently of the DC-41 code, it reproduces the DC-41 clean edge values. The first-order correction −2(Δ/qv_F)𝔰_BCS describes the BARE bubble only (SPINE LO(iii) conflict). Fix SPINE at the merge.
- 15.2's resummed form (CW4 (8.1)) is the resummed bare bubble. Check that 15.2 says so (it does, per its report) and that no "physical" claim rests on it.
- 16 % (SPINE, v_F = 6.8e-3) vs 17 % (book v_F = 6.67e-3). One Al v_F book-wide (see the 15.3 note: 6.67e-3 vs 6.77e-3).
- Allen 1971 (case-I elliptic form) credited unread: citation audit.
- NOTATION row 1068 "𝔤_IL^nor" is a misparse: delete at the merge.
- Possible duplicate pair-function reduction in D.39 vs 15.1. Make one point to the other.
- WE 15.1: bulk gap 0.18 meV vs film convention; the 0.3 meV of 2109.04473 is Δ (half the gap). Factor 1.23 between the two.
- 15.1 says bare is within 10 % of conserving only at y ≥ 9.4; 15.2 finds 9.2 (see 15.2 note).

## Spin-current check (independent verifier): CORRECT WITH CAVEATS (spincurrent-check.md)
- Derivation holds. ȧ σ·v/2m → v τ₃ in Nambu form, which does not commute with H_MF; it creates zero-momentum triplet pairs. σ^J = 2πω_p²Δ²/[ω²√(ω²−4Δ²)], weight (π/2)ω_p² exactly. Robust beyond mean field: exact spin f-sum and zero spin stiffness of the singlet at T = 0 (the Knight-shift physics). SOC negligible in Al. Numbers reproduced: 5.12e-13 vs 5.64e-9 (the latter is the book's own recomputation with the published method).
- Literature: Hochberg–Lin–Zurek (1604.06800) and Mitridate et al. (2106.12586) leave this channel out by assumption (Π_ΣΣ = Π_11 extended to the superconductor, which drops the sign flip of the anomalous term). No prior paper found.
- RULING R0 (binding on the Ch15 reviser): the text must state that
  (i) the clean limit needs ℓ ≫ ξ₀ ≈ 1.6 µm (bulk high-purity Al);
  (ii) the 10⁴ gain is over phonon-only clean-Al projections only, since for a 50 nm film the published σ₁ mapping applied to its Mattis–Bardeen σ₁ already gives g ≈ 2.0e-12 against 1.5e-12 for the spin channel;
  (iii) the line shape at fixed m_a depends on F₁ᵃ backflow, the triplet p-wave vertex and strong coupling (g ×~1.2), while the integrated weight is fixed by the sum rule.
  No novelty wording in the book; recorded in NOVELTY.

## Ch15 review rulings (2026-11-06; five reports + spincurrent-check: all MINOR GAPS / REVISE, no REWRITE). R0 above binds.
- R1. One aluminum free-electron set book-wide: m* = m_e with k_F = 1.75 Å⁻¹, so v_F ≈ 6.76e-3, ω_p = 15.78 eV and the matching k_TF. Compute each value once in a shared script (figscripts/ch15/bcs15.py or a new al_constants.py) and log it. Apply it in Ch15, and by narrow edits in 6.4, 7.2 and E.20 wherever they print v_F, ω_p or k_TF. Rerun the Ch15 scripts (loss ratios move ≤ 0.4 %; the vertex fraction 𝔳 moves 10–40 %, so update it). Replace the superseded room-temperature Al elastic constants per state/CORRECTIONS §19.13(g).
- R2. The y < 3.8 cut: re-justify it from the conserving response and its mean-free-path dependence (15.2's second reason), not from the bare first-order term. If a different cut follows, adopt it consistently (15.2, summary, F rows) and log the criterion.
- R3. The edge remainder is two-sided above the edge momentum: −2 % to +9 % (the clean ratio falls to 0.980 at about 4× the edge momentum at y = 3). Fix 15.2, the summary table and the F row. The clean edge values carry the mean-free-path clause that DC-RESULTS requires.
- R4. Fine-grid thresholds everywhere:
  - 9.2 (not 9.4), 7.9, 0.050, 6.3, 2.25;
  - Fig. 15.2b q𝔩_e = 0.64 and 9.8;
  - the Lindhard limit 8e-7 (3e-5 was a quadrature floor);
  - "within 8 %" → 9 %.
- R5. Sheet screening: present the formula as the kd ≪ 1 limit of Lasenby–Prabhu 2110.01587 Eq. (19). WE 15.3: 540 at leading order, 588 exact slab. Fix the QROCODILE paraphrase (anisotropy very large at 1 nm⁻¹, significant already at 1 keV).
- R6. 15.2 opener kinematics: a threshold-mass particle scatters at q = 2ω/v_max; only particles a few times heavier reach the edge q = ω/v_max.
- R7. One home for each overlap:
  - the conserving edge values → eq:15.2-cons + tab:15-edge;
  - the algebra and a single quadrature recipe → D.39 (15.1 points there);
  - mean free path → 15.3.3, with one normalization for its numbers; 15.2.3 points forward without using undefined terms;
  - the AB pole → 15.1, with its proof in D.39. Its explanatory scope is limited to y ≲ 2.3 (17 % of the shift at y = 3, none at y = 5).
  - f_L lives in 15.2.
  - Define "kinematic edge" at first use and distinguish it from the "pair-breaking edge".
- R8. Numbers and typos:
  - WE 15-film: ×10⁶, and 0.241×10⁵;
  - WSi DOS maximum 3.4e47, Zhang x = 0.85 rows recomputed via the Einstein relation;
  - Gan: gap 0.26 meV, locators Sect. V and Eq. (8); Hochberg 2021 Lindhard Eq. (S.13);
  - WE 15.1 share 20 %; ladder correction 4e-4 (weighted);
  - summary: "bare down to 0.53" only for y ≥ 3 (0.37 at y = 2.2); source "×1.13 heavy" or remove it;
  - 𝔰_BCS → π²/(2y) asymptotically;
  - Re ε^cons < 0 at y ≈ 2.2: mention it;
  - 1/q is not a "wavelength";
  - explain the M_{s2} phase and the |M_η|² step.
- R9. Language and provenance:
  - remove "masked cells" (campaign term) and the data-generation sentence in the tab:15-edge caption;
  - strong coupling: qualify "open" (the normal-metal extended-Drude result is known; open is the superconducting case);
  - Allen 1971: cite directly only if read; otherwise "as quoted by";
  - pair-list prose → tables or one sentence each;
  - register as in the prose review;
  - fix the 16.2 "??" (plain prose until Ch16 exists).
- R10. Spin current (with R0): in the dirty limit the weight conservation is exact (∫(𝔤_I − 1)dy = 2); attribute the 0.05 % to the Drude shape and cutoff. Electron–electron absorption: add it to the nuisance table as a named, unsized channel only; print no size estimate, since the coefficient is unverified.
- R11. Notation:
  - ω_AB → a non-clashing symbol (Alig–Bloom owns ω_AB);
  - upright v_F;
  - D.39 h, g, G, T clashes; mislabelled δ_𝔰;
  - 𝔣_L(ν) → a variable other than ν;
  - delete NOTATION row 1068; replace L^BCS with L^bare/L^cons;
  - add the missing 15.x rows.
