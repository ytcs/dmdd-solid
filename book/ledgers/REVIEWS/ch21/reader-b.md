# Chapter 21: mock reader b (personas b and c)
Source read: tex/ch21/*.tex (same content as the current PDF), linearly, after Chapters 1–8 and 10–20. Numerical checks were run in Python/scipy and are listed per section ("✓" means reproduced).

## Persona (b): particle physicist, knows QFT, no solid-state physics

### 21.1 Rate assembly
- **Lost points:** none blocking. "Λ", 𝔇 and S PSD are from Ch. 8 and recalled fine.
- **Reproduced:** integration by parts to eq. (21.1-etaform) ✓; η₂ identity (21.1-eta2) by differentiating in u ✓; η(0)=1041/c ✓; no-escape-cut ratios 1.18/1.90/6.8 ✓; rms 10.4 km/s ✓; floor 0.3332 MeV, June 0.3202 (−3.9 %) ✓; flow window 89.5–590.5, 1/v_flow = 882 ✓, 55 % above 400 km/s ✓; flow-only floor 0.6031 MeV ✓; v_on = 146.9 / 46.4 km/s ✓; WE 21-debris (2.151e5, 1.345, 1.721e5, +7.6 %, 471/day, end points 19.4/35 eV) ✓.
- **Used before defined:** none.
- **Pace:** the paragraph of ratios after lim:21.1a (0.9965, 1.015, 1.026 …) is more detail than I need, but it is harmless.
- **Outcomes:** write any rate as ∫f Γ ✓; convert to the η form ✓; rate in a debris-flow halo ✓; explain why the threshold mass is a floor ✓.

### 21.2 Halo-independent bounds
- **Lost point (minor):** the **lim:21.2a box title says "directional response"**, but the box states the speed-only formula (21.2-hib) "for a response averaged over the directions of q". It took me a second reading to see that the box gives the simple formula and the figure tests it against the directional program. Fix: retitle the box, or say "formula tested against the directional program" in the box text.
- **Lost point (minor):** "δ = −δ_E, the direction against the wind." A stream at δ = −δ_E moves *with* the wind (it comes from upwind, i.e. from Cygnus). Say "arriving from the direction of the Sun's motion".
- **Reproduced:** union bound with ln 30 per bin, 3×1/30 = 0.10 ✓; WE 21-stream prefactor 8.64e22 yr (μ = 486.2 keV, M_cell = 52.3 GeV) ✓; A_i ratios 7.58e-20 / 2.80e-20 / 1.26e-19 ✓; c = 4.67e-23 ✓; event counts 1.26 / 3.40 / 0.76 ✓; galactic speeds 249.5–750.5 ✓; λ₂ = 8.23e-21 ✓; factor 2.94 = 2.42 × 1.22 ✓; declination support cos(δ+δ_E) formula (minimum over right ascension) ✓, range at 790 km/s [−56.5°, −38.5°] → grid −56…−40 ✓; −68° allowed at 600 ✓; grid gain 0.095 % ✓; leakage factors 0.034 / 0.036 ✓. The certificate proof via monotone A_j is clean.
- **Too fast:** 21.2-leak, second paragraph (the Dyson split, the seeding by the zero-phonon partner and stochastic ordering) is compressed and leans entirely on App. D.46. I accept the result but could not rederive the 2ω_max bound from the text alone.
- **Outcomes:** compute a halo-independent bound from step columns ✓ (redid the 500 km/s case); check a dual certificate ✓; say when the closed form fails ✓.

### 21.3 The kinematic edge
- **Lost points:** none blocking. The Ch. 13 vocabulary (Q*, u_ν, second class, glide/mirror plane) is used without a reminder. I remembered it, but **u_ν in "q* = m(v_max ± u_ν)"** deserves a five-word gloss.
- **Reproduced:** beta-function width integral, giving (2m)^{1/2}X^{p+3/2}B(½, p+2) ✓; lens volume πf δ^{k+2}/[a⊥(k+1)(k+2)] and F_esc ✓; A_η = F_esc/2v_max ✓; dm_edge/dv_max = −2m²/q* ✓; halo fractions within 12 km/s of v_max: 5.93e-5, 4.72e-6, 3.65e-8 (numerical integration) ✓ against 6.0e-5 / 4.7e-6 / 3.7e-8; table powers n = p_on + 7/2 (+½ at a corner) ✓; nuclear edge m = 137 MeV for a 10 eV threshold ✓; exposure factor 10^{−2/13} = 0.70, King 0.74 ✓; x*_max 3.5 and 5.3 meV per 0.001 MeV ✓; ∂ln A_η/∂v₀ = +3.2 %/km/s and ∂ln A_η/∂v_esc = −1.76 %/km/s ✓; v_max^14 → 1.76 %/km/s ✓. WE 21-gapshift: 0.00285 MeV, factors 0.0044/0.115/0.371, 231/8.8/2.7, 3.35 km/s, zero-phonon 0.4077 MeV, 0.54/−1.62, 0.00188/0.00277, closing 0.00095/0.00006 ✓.
- **Snag, then resolved:** at first I could not get A_η v_max^{2p+8}. Holding the gap fixed I got 2p+9.4, because μ_χe changes with m_edge. The text means fixed *edge mass* (gap and v_esc shifted together), which gives 2p+8 exactly. The sentence that states the scaling says "at fixed χ-mass minus m_edge"; repeat "at fixed edge mass" there.
- **Outcomes:** derive the edge power for any p_on, k_tail ✓; state which combinations the edge measures ✓; estimate how far an exposure gets from the edge ✓.

### 21.4 Theory nuisances in a limit (my field)
- **Reproduced:** classical limits 1.303, 2.890, 3.322 ✓; Feldman–Cousins Table IV values 2.44/1.61/1.08/3.36 ✓; WE 21-rpaband 9.23e-42, 1.345, 1.048, 1.30e-41, σ_β = 0.393, band 8.78e-42–1.93e-41, 93 %, one-at-a-time factors ✓; e^{1.15σ²} = 1.195 ✓; detector 0.405 / 1.499 ✓; one-sided σ_β = 0.306 ✓; excluded-cell factors 1.25 / 1.59 / 1.49 / 1.08 ✓.
- **Error (small):** "N^up/N₉₀ = 1 + ½σ_β²(N₉₀−1) … 1.103 at σ_β = 0.393". The formula gives **1.101**. The exact constraint-averaged value (I integrated it) is 1.103. Label 1.103 as exact, or quote 1.101 for the formula. The summary table repeats 1.103.
- **Inconsistency:** this section says the final-state split is "a normalization of at most 0.034 of a silicon bin". Eq. (21.2-fsleak) gives ≤ 0.034 ϱ_i. Section 21.6 has it right; this section and the summary drop ϱ_i.
- **Field remarks (no condescension found):** the classical/Feldman–Cousins treatment is correct. A HEP reader will miss **CL_s** and the **direct-detection reporting conventions** (the halo values used here match the community recommendation). One sentence saying why neither is adopted would help. The calibrated threshold 𝗍* = 2N₉₀ = 4.61, against the asymptotic one-sided 2.71, surprises a HEP reader on first sight; a back-reference to why §8.8 calibrates it would help.
- **Outcomes:** classical limit with background ✓; β_k, band and profiled cost for one bin ✓ (redid the 3 MeV case).

### 21.5 Statistics, combination and recasting (my field)
- **Reproduced:** maximum-gap limits from (21.5-C0): g = 0.9 → 2.836, 0.5 → 7.78, ⅓ → 13.8, break-even 0.761 ✓; classical 6.681 ✓. **WE 21-combine reproduced by a full Neyman construction:** 0.928e-42 without the nuisance, 1.029e-42 with the shared one, ϑ̂̂ = −0.46 ✓; A-only closed form e^{k²N₉₀} = 1.12 ✓; recast factors ×1.333 → 1.294/1.222/1.150 ✓, 3.49 × 1.222 = 4.27e-42, consistent with §21.2 ✓; 0.9ⁿ ✓; Dirac recasts 5.4e-43, 8.8e-42 ✓; harmonic mean 50.5² = 2554 ✓; boosted R^{−1/2} limits 1.04 and 4.5 ✓.
- **Field remark:** in the combination the constraint term is "held fixed since a theory nuisance has no auxiliary measurement". That is a hybrid construction. Its coverage is not the usual unconditional one, and one clause saying so would pre-empt referees.
- **Outcomes:** maximum-gap limit ✓; combination with shared nuisances ✓; recast or bracket a limit ✓.

### 21.6 Shared response libraries
- **Reproduced:** 2q²/e² = 3.038e8 eV² ✓; L = 0.1442 / 0.1585 ✓; ΩS = 0.2283 eV⁻¹ (Ω = a³/4 = 40.05 Å³) ✓; interpolated L = 0.1390 ✓; ratios 0.864, 0.242, 0.29 ✓; storage sizes 7.5e6 nodes / 720 MB / 13 TB / 1.2 GB / 1.2e7 ✓.
- **Lost:** none. This is the section most foreign to me (screening, scissor, TB09), but the worked example makes it concrete.
- **Outcomes:** list what a library must hold and why it has no velocity axis ✓; turn a dielectric-table entry into S with its label ✓.

### 21.7 Next targets
- **Reproduced:** β fractions from (21.7-beta): tritium 0.0892, ²¹⁰Pb ground-state branch 0.0438, ²¹⁰Bi 9.67e-4, ⁴⁰K (unique 3rd forbidden) 4.13e-4, ¹¹⁵In 3.7e-3 (allowed) / 4.5e-4 (unique 4th) → 3.9e4 / 4.8e3 ✓; tritium 0.169 / 11.0 and germanium 0.112 / 7.31 ✓; 689 per kg·d·keV and 1.45 mBq/kg; per kg of lead 2.00/2.34/1.68 ✓; KTaO₃ 4.6 kBq, 1.5e5 ✓; ¹²³Te bound 693/kg/d ✓; Klein–Nishina limit 1.20e-28 cm²/keV ✓; cube mean escape path 0.4486 L (Monte Carlo) ✓; 5.4e-4 ✓; CsI 3.73, 3.81, edge 23.1 keV, polar 2.85 keV, floor gap ≈ 6.2 eV ✓; PbSe/Ge floors → 0.170 / 0.744 eV gaps ✓; 42 = 11 + 31 ✓.
- **Lost point:** the composition of the pool. 42 = 23 (Griffin, "all but InSb") + 3 SiC + 16 listed. **KTaO₃ is then either among the 23**, which contradicts "positive evidence removes a crystal" for it, **or it comes from somewhere unstated.** Say where KTaO₃ enters and confirm that it is outside the 42.
- **Field remark:** for CsI's "missing demonstration" (a hygroscopic crystal at mK with a sensor on a carrier), the NaI cryogenic-calorimeter programme is a precedent worth citing if it is documented. I believe COSINUS has done this, but have not checked.
- **Too dense:** the guide (landscape longtable) carries a lot. The prose after it does the reading for me, which helps.
- **Outcomes:** read a row of the guide ✓; background tolerance (R_A/R_B)² ✓ (1.22² = 1.48; 1.56² = 2.44); low-energy β fraction ✓.

### Summary section
- **Error:** in the "Halo of the floor" row, "June **escape speed** lowers the floor by 3.9 %". It is the June **Earth speed** (v_E); v_esc is fixed.
- **Error:** "a final-state assignment that is **not** stochastically ordered leaks at most 0.034 of a bin". In §21.2 the bound *requires* stochastic ordering ("provided the number of pairs grows stochastically…"), and the size is 0.034 ϱ_i.
- **Used before defined:** "semi-infinite linear program" appears only in the summary.

**Verdict (b): MINOR GAPS.** Nothing blocks. I reproduced every derivation and nearly every number I tried, including a full Neyman construction for WE 21-combine. I would keep reading.

## Persona (c): condensed-matter theorist, knows DFT and many-body theory, no dark-matter physics

### 21.1
- **Lost points:** none blocking. I lean on Ch. 1 for v_E(t), v_esc and the sidereal rotation. "Via Lactea II" and "debris flow" are introduced well enough to use.
- **Too fast:** why v_E^ref = 250.5 is not the yearly mean (252.1). The text gives ⟨δv_E⟩ = 1.61 but not the convention behind the reference. One clause pointing to App. A.8 would do.
- **Outcomes:** as for (b) ✓.

### 21.2
- **Lost points:** "upper count of §1.5" and the union bound are fine. "Dual certificate" is ordinary LP duality and clear. The modulation-amplitude case ("bounded only if every stream on which it is positive is seen by some bin") is stated without an argument; it can stay a remark.
- **Field check:** cubic harmonics ℓ = 4, 6, 8; the circle average P_ℓ(v_min/v) Y_ℓ(v̂) (addition theorem) ✓; "model with a 0.82 eV gap, no local fields" is honestly labelled.
- **Outcomes:** ✓.

### 21.3
- **Field check:** the exponents are right. Elliott/Sommerfeld turns √x into a step (continuum p_on drops by ½) ✓; for an isolated quadratic minimum in D variables the density of states goes as x^{D/2−1} ✓; a linearly vanishing vertex adds 1 ✓. The exciton binding of 14.7 meV and the 1s line at 1.1553 eV are right.
- **Possible reader trip:** "the transverse acoustic phonon at Q*, about 15 meV" (E_on − E_g = 14.8 meV). An optics person expects the TA replica at **18.4 meV** in Si absorption. The reason is that the dark matter supplies part of the momentum, so Q* < k_c. WE 21-gapshift hints at this ("larger q* shortens Q*"); say it once where 15 meV first appears.
- **Pace:** the degeneracy paragraph on the height (A_η vs v_max^{2p+8}) needs "at fixed edge mass" restated (see b).
- **Outcomes:** ✓; I can now say which halo parameter mimics a gap error.

### 21.4–21.5 (statistics outside my field)
- **Lost points:** "profiling", the statistic 𝗍 and its slope 𝗍′ rest on App. C.14 and D.47. The key result (21.4-profile) cannot be derived from the chapter text. I took it on trust and checked only its numbers. A two-line heuristic (a quadratic expansion of 𝗍 in ϑ, minimized) would let a CM reader see where σ²𝗍′/4 comes from.
- Feldman–Cousins and Yellin are explained enough to use. The construction in WE 21-combine is followed, but its rationale (why sum outcomes with statistic ≥ observed) needs the C.14 background.
- **Outcomes:** I can compute a band and a profiled factor for one bin ✓, and the maximum-gap limit for a given g ✓. I could not set up the combination construction unaided.

### 21.6 (my field)
- **Field check:** ε_mac = 1/(ε⁻¹)₀₀ against the head ε₀₀; "ε₂/|ε₀₀|² = RPA without local fields" ✓. S per volume in eV² ✓. Detailed balance in the stated form ✓ (with S(q) = S(−q) under time reversal). "Odd ℓ vanish by time reversal, ℓ = 2 by cubic symmetry" ✓. f-sum with ω_p = 16.6 eV ✓. TB09 + scissor attributed correctly. The provenance/versioning rules are sensible.
- **Minor:** "R⁰_GG′ … some 600 TB" implies N_G ≈ 2200 at 16 bytes per complex entry. State N_G so the reader can rescale.
- **No condescension.** The DFT and RPA vocabulary is used at the right level.
- **Outcomes:** ✓.

### 21.7
- **Field check:** pair energies (Ge 2.96 eV at 77 K, GaAs ≈ 4.2 eV, Si 3.749 eV) are standard ✓. The PbSe low-T gap of 0.17 eV is right ✓. Calling CsI "hygroscopic" is an overstatement (it is only slightly so, much less than NaI), but encapsulation as the requirement is reasonable. The Si highest phonon of 64.1 meV is right.
- **Lost point:** the KTaO₃ pool membership (see b).
- **Outcomes:** ✓; I understand why the guide reports two pools and what would move CsI.

### Summary
Same two errors as (b): the June **Earth** speed, not the escape speed; and the stochastic-ordering condition plus the missing ϱ_i.

**Verdict (c): MINOR GAPS.** Nothing blocks. The statistics sections are the weakest for a CM reader because the key profile formula lives in the appendices. Everything in my own field checks out.

## Fix list (priority order)
1. Summary table, "Halo of the floor": "June escape speed" should read "June Earth speed".
2. Summary ¶2 and §21.4-like: leakage ≤ 0.034 ϱ_i, conditional on stochastic ordering; drop "not".
3. §21.7-pools: state where KTaO₃ enters and confirm it is outside the 42.
4. lim:21.2a: box title against content (speed-only formula tested against the directional program).
5. §21.4: 1.101 (second order) against 1.103 (exact), in the text and the summary table.
6. §21.3-degeneracy: say "at fixed edge mass" at the v_max^{2p+8} sentence; gloss u_ν.
7. §21.3 / WE 21-gapshift: explain the ≈15 meV TA energy at Q* (vs 18.4 meV optical).
8. §21.2-dir: "against the wind" wording; summary: define "semi-infinite" or drop it.
