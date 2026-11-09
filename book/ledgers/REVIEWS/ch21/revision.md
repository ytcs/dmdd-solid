# Chapter 21 revision (2026-11-06)

Brief: briefs/reviews/ch21-revise.md. Rulings R1–R8 (editor-notes.md, Ch21 block) and the five reports (derivation-1/2, prose, reader-a/b).
Build: `latexmk -pdf -outdir=/tmp/claude-0/build-ch21rev main.tex`: 0 LaTeX errors, 0 undefined citations (undefined references only to unwritten app:B.2, sec:9.x). Lint: no blocking hits; remaining LONG-SENT warnings and the two "landscape" false positives. check_notation on tex/ch21, D-46, D-47: 46 gaps → 7, all sans-serif or stacked-accent tokens that have rows under their printed glyphs (𝖱_FC, 𝖿_u0, 𝗀_λ, 𝗍_ϑ, a_ℓ, b_²¹⁰Pb, the hat of σ̄_e).
Scripts rerun (light Python only, no QE): hib21 (shared), we21_2, fig21_2, limit21_2a, we21_4, nuis21 (shared), fig21_4, we21_5, stats21_5, fig21_5, fig21_3, guide21_7, map21, map13 (as briefed), ch10/nuis10_10 (log now written to nuis10_10.log). Every number changed below is in those logs.

## Substantive rulings

| Item | Status | How |
|---|---|---|
| R1 one construction | done | Book construction = Neyman with ϑ at its conditional best fit, constraint fixed (described once in 21.4-like, with the hybrid/coverage caveat and a CL_s sentence, junk1999confidence). eq:21.4-profile coefficient now σ_β²𝗍′/2, exact for one bin (checked numerically for N_obs = 0,1,2 with backgrounds, we21_4.log Part 3). WE 21.4: profiled factor e^{σ_β²N90} = 1.427 → 1.77e-41; one-sided 1.240 → 1.54e-41; detector 1.457. Fig. 21.4 dashed line = e^{σ²N90}. D.47: μ removed, new subsection: Neyman shift y = σ²Q′/2 (eq:D.47-yhat), exactness for one bin, the fixed-threshold σ²Q′/4 as the comparison (half). Three-coefficient comparison removed from 21.4/21.5; 21.5 WE says its 1.12 is eq:21.4-profile. Summary text and tab:21-nuisances updated. |
| R2 cascade pair bins | done | hib21.pbin: P_casc(N|ω) from ch18/casc18_3.json (DM seed, 3.749 eV, E_g 1.160), round-off <1e-6 zeroed, N≤3 set to 0 above 21.16 eV; step model kept for comparison. Results: 10 MeV σ_lim 3.72e-42 (one-pair bin), bound(500) 3.61e-20, min cost ×2.12 at 379 km/s, ×12.4 at 600, ×77 at 700; 2 MeV ×3.70 at 559; crossover 1→2 at 532.6 km/s (10 MeV); at 2 MeV one-pair binds everywhere, two-pair opens 474.3, three-pair 614.4 km/s. WE 21.2 rewritten (A_i 9.41e19/8.07e19/1.82e19 yr, ξ_1 6.03e-23, counts 3.40/2.92/0.66, λ_1 1.06e-20, ×4.35 = 3.96×1.10). Intro "second pair above 474 km/s". Step model mentioned once as the simplification that would make the two-pair bin bind (×~10 at 5 eV, sec:18.3). Limit Check 21.2a rerun with cascade bins (1.53 % at 600, 0.47 % at 700, ≤2.0 % above 560, 1.15 at 340; 790 km/s now +0.4 %, old "below the formula" sentence removed); grid leakage 0.096 %, defect 9.5e-4, bracket 48 %. Leakage factor uses ε = 3.749 eV and ω_max = 63.7 meV → 0.034 (consistent). 21.5 WE combine uses the cascade one-pair bin (r = 9.14e41; 2.52/1.14/0.809e-42; shared 0.897e-42 ×1.109; split 0.851e-42 ×1.051; θ̂̂ unchanged). Halo recast: factors 1.271/1.204/1.154 (10 MeV, binding one-pair bin, exact 3.72e-42), 1.156/1.432/4.0 at 2 MeV. tab:21-dominant pair-bin row names the two cascade figures (17 % simplified/resolved seed vs tenfold full band), reconciling with 21.7. |
| R4 double-counted cold gap | done | nuis21 and ch10/nuis10_10: tables' gap = measured T=0 gap 1.17 eV (2101.08275 Sect. III B), no 0.06 eV shift. WE 21.4: RPA 9.23e-42, central 1.24e-41 (×1.345), band 8.38e-42–1.84e-41, profiled per R1. Fig. 21.4 rerun: band ×3.42/1.48/1.43; crossings 1.14/3.59/7.04 MeV; RPA/central 1.10 (1 MeV), 1.46 (10 MeV), below the band only at 10 MeV. 10.10 narrow edits: l.3 (tables "counted from 1.17 eV"; "gap of the tables is not the gap of a cold crystal" replaced), the scissor paragraph rewritten (scissor to measured T=0 gap, m_min 0.333; 1.11 eV is the step-model constant), WE 10.band3 central 1.85e4 (51/kg/d, 10 % below 3 eV), LF template +0.066/+0.064, band 1.25e4–2.75e4, ϑ_X = 1 → 2.37e4, light 6.0e3, "at the tables' gap" dropped, l.102 "with their gap of 1.11 eV" dropped, chapter summary 1.85e4. σ = 0.393, 1.48, 93 % unchanged. 21.6 states the tables' gap explicitly. |
| R5 ²¹⁰Pb budget | done | guide21_7: relativistic point-nucleus Fermi function (hayen2018high Eq. (6), eq:21.7-fermi) for Z_d = 83 (²¹⁰Pb) and 84 (²¹⁰Bi): f_β 0.0445 and 1.26e-3, b = 724 per kg d keV per Bq/kg (614.7 + 109.2, Bi 15 %), budget 1.38 mBq/kg; 1.91/2.23/1.60 mBq per kg Pb; +5 % over the nonrelativistic 689 (logged). Z_d attribution fixed. eq:21.7-pb210 carries ×1 Bq kg⁻¹ and ends with a period. Guide table, summary, open problems updated. |

## R3, R6, R7, R8

| Item | Status | How |
|---|---|---|
| R3 June | done | 21.1 floor paragraph, 21.3 end of the time handle, 21.4 halo paragraph (now the ±25/±6 km/s band), summary: exposure average is the basis of a limit; June Earth speed is kinematics; reference floor is the comparison convention. Summary row "Earth speed at the floor", "June Earth speed". |
| ZrTe₅ ~5100 | done | text 5100–6400; fig21_5.py includes the value interpolated at 20 keV (5091); log ratios 1.99–2.52. |
| dominant nuisance only at 3.59 | done | 21.4 fig paragraph reworded; 1.14/7.04 MeV as subdominant swaps. tab:21-dominant "×1.28, ×1.26 at 10 MeV". |
| tabulation spread treatment | done | justified Gaussian with stated prior: a bound on the width of a spread, entered with that width (conservative); stated once in 21.4-like; 21.5 and 21.6 point to it. Alternative (envelope ×1.335, other three ×1.306) logged in we21_4.log, not printed. |
| 600 TB | done | number and "10 GB" dropped (no basis). |
| boosted-flux clause | done | "1.04–4.5" clause removed; remaining wording follows REF §4 items 1–3. |
| 21.3 6.6 %/78 meV; 1 % phonon | done | "−6.0 and +6.6 percent, as −71 or +78 meV" (fig21_3.log, new lines); 1 % error now "in the onset energy E_on". |
| LC 21.1a boundary | done | convention stated: "the yearly average exceeds the closed form by less than 10 (1) percent" (box caption, closing sentence, summary, F row). |
| LC 21.2a | done | title "Speed-only bound against a directional response"; formula credited to Fox–Liu–Weiner (A1)–(A2); one sentence on what the plot shows; "up to 15 percent on the sampled speeds", sampled from 340 km/s (the column below 337.5 km/s is one cell; LP degenerate, stated in limit21_2a.py). |
| keyresult 𝒜_i(u₀) > 0 | done | 21.2 keyresult. |
| 1.101 vs 1.103 | moot | the constraint-averaged construction is no longer quoted (R1). |
| leakage 0.034 ϱ, stochastic ordering | done | 21.2, 21.4, summary (condition stated correctly), D.46: ϱ^leak_i over the bin widened by ω_max, Δ_i = ∫P_i dω, signal = P_i-weighted. |
| KTaO₃ in the pool | done | 21.7-pools: KTaO₃ (11.5 target) and InSb outside the 42. |
| eq:21.5-C0 regular form | done | bracket form, finite at integer N/x; relation to Yellin's printed form stated. |
| v_max^{2p+8} at fixed edge mass | done | "at fixed m_χ − m_edge and fixed edge mass, gap moved with v_esc" (exponent as verified by derivation-1 and reader-b). |
| envelope theorem stated | done | 21.3 degeneracy, one clause with pointer to 21.3-power. |
| "stochastically ordered" defined | done | 21.2 and D.46. |
| ω_max 63.7 | done | 21.2 (sec:11.3), limit21_2a.log 0.0340. |
| scaled-dual exact check (optional) | done | 21.2-leak: evaluation at the cell break speeds certifies on the continuum. |
| u_ν, TA at Q*, CL_s/hybrid | done | u_ν glossed (21.3); 15 meV vs 18.27 meV optical replica explained; CL_s and hybrid in 21.4-like. |
| other derivation-1 items | done | curvature caveat (exponent unaffected), exposure reach depends on the halo tail, Feldstein "Sect. 3, Eq. (3.1)", Lisanti "Sect. II, Eq. (10), Fig. 3", "(one harmonic per ℓ below 12)" in D.46, P_ℓ ≤ 0.375 remark, ⟨δv⟩ "almost all from the second-order term", fig caption "one day at v_E^ref" + year-average clause (×1.06 at 700). |
| other derivation-2 items | done | D.47: β at x with O(σ⁴) note; "template of one sign in every bin" (21.4, D.47). |
| reader items | done | c clash (ξ_a), box title, right-ascension optimization stated, "arrives from the direction toward which the Sun moves", inline certificate proof, Lipschitz/covering radius glossed, M_cell, kernel "scaled to a rate per target mass", v_E^ref convention vs yearly mean 252.1, TB09 glossed, semi-infinite program now introduced in 21.2, CsI "slightly hygroscopic". Not done: COSINUS/NaI precedent (not verified; no citation added). |
| R7 opening | done | second paragraph now motivation (stakes in numbers) plus one orienting sentence. |
| R7 vocabulary | done | "no reading" → "no resolved leader"; "gap" → "hole in coverage", "three missing inputs"; 21.7 Ch20 paragraph reduced to one sentence + pointer. |
| R7 said once | done | union bound (21.2 only; 21.4, 21.5 point), E.27 pointer (removed from 21.1), tabulation spread (21.4-like; 21.5 points). |
| R7 register/house forms | partly | cross-section, nonnegative, km s⁻¹ (\SI{..}{km.s^{-1}}) chapter-wide; count-teasers and prose items 1–74 applied except optional ones (21.4 l.3 rhetorical question kept, accepted by the reviewer). Word-frequency rebalancing ("only", "gives", "however") applied only where sentences were rewritten. |
| R7 eq punctuation, D.47 typo, capability statuses | done | eq:21.7-pb210; D.47 "𝗍′ = 2N^up = 2.61"; capability column uses "shown" (documented, cited) / "not reported" (no record), h-BN "<0.1 g" removed. |
| R8 notation | done | c → ξ_a; δ → δ_dec, δ_cert (edge distance keeps eq:1.3-edge's δ); 𝒦_j → K^rc_j; β_k/σ_β flagged row; D.47 μ removed; six undefined symbols defined (M_cell, u_ν, Δ_χ, 𝒬, ε_D, λ_AB); kernel relation stated (NOTATION Ch21 row; E.27 narrow edit). E.27 negative-pieces statement corrected (weak duality holds; mass bound fails). NOTATION: Ch21 block (12 rows) and clash entry 93. |
| Coordinator: junk1999confidence | done | bib entry added after confirming hep-ex/9902006 on the arXiv API (Junk, NIM A 434 (1999) 435). |
| Titles | done | 21.1 "Rates as halo functionals", 21.5 "Combining and recasting limits", 21.5-corrected "Dirac and boosted-flux recasts", 21.7 subsections "Candidate pools and detector readiness", "Absorption and unranked channels". |

## Owed outside the brief's files (for the editor / light passes)
- 10.2 (l.43 caption, l.86 WE threshold "1.11 eV of a charge…"), 10.9 (l.73 caption "tables' gap of 1.11 eV"), 17.1 l.44 ("0.316 MeV with the gap of the table"): same R4 premise; the tables' gap is 1.17 eV. Numbers there change by <0.1 % (threshold 1.11 vs 1.17 on node-resolved tables), only the wording is wrong (17.1's 0.316 MeV floor should be 0.333 MeV).
- Ch16 we:16-factor "near 9 keV" vs 21.5 "near 9.5 keV" (digitized minimum): align at Ch16's light pass.
- 22.3 displays F_Fermi again (eq. in s22-3); it may now point to eq:21.7-fermi.
- SPINE: 21.1 "floor" wording (exposure-average position); 21.7 open problem on elastic constants (TeO₂ + computed tensors + CsI cold density); Ch22 index entries for the same. 21.2/21.5 now use the cascade bins.
- App. E: the release tolerances of 21.6 are now phrased as examples ("for instance"); no App. E change needed.

## Changes the campaign ledgers need (not edited here)
- state/CORRECTIONS.md: (1) R4: the Knapen–Kozaczuk–Lin silicon tables carry a scissor to the measured T=0 gap (1.17 eV); any campaign or book number that shifted them by +0.06 eV double-counts (10.10 central 1.77e4 → 1.85e4; Ch21 WE 1.30e-41 → 1.24e-41; band 8.8e-42–1.93e-41 → 8.4e-42–1.84e-41). (2) R1: the book's profiled limit is the Neyman construction at the conditional best fit, ln ratio = σ²𝗍′/2 (exact for one bin); eq:8.8-cost's fixed calibrated threshold is an illustration with half the exponent. (3) R5: ²¹⁰Pb+²¹⁰Bi sub-keV budget 724 (not 689) per kg d keV per Bq/kg, ≤1.38 mBq/kg; Bi share 15 % with the relativistic Fermi function (12 % nonrelativistic); ²¹⁰Bi daughter Z = 84. (4) R2: halo-independent silicon numbers with Ch18 cascade bins (σ_lim 3.72e-42 at 10 MeV, one-pair bin binding; ×2.12/×3.70); CW7-errata "3.3 % ρ_−" consistent with 0.034.
- SOTA.md: halo-independent cost "×2–4 in the bulk" stands (2.12–3.70); the step-model statements "two-pair bin tightest", crossovers 379.5/792.9/758.5 km/s are superseded. Ge tritium 7.31 (measured 82/kg/d) vs research 6.7 (calculated 75) — production-rate choice, not an error.
- LOOSE-ENDS: open — first-forbidden ²¹⁰Bi shape for the sub-keV budget; ²¹⁰Pb activity of growable lead; COSINUS/NaI precedent for CsI capability (unverified); h-BN capability rests on an [UNVERIFIED] row (now "not reported"); directional LP not sampled between 332.7 and 340 km/s (single-cell column).
- NOVELTY: the profiled-limit exactness for one bin (Neyman construction, any counts) and the stochastic-ordering leakage bound 2ω_max/Δ_i are book derivations (D.46, D.47).
- DEFERRED-COMPUTE: none added (no unsized F-row; the ²¹⁰Bi forbidden shape is a light computation if wanted, not QE).

## Post-revision check fixes (postrev-check.md, 2026-11-07)
- Summary: "five to forty percent" → "five to forty-five percent" (profiled factor 1.427).
- Leakage factor: the cascade bins have Δ_i = ∫P_i dω = 3.604 (two-pair) and 3.687 eV (three-pair), 4.976 eV (one-pair), so 2ω_max/Δ_i is at most 0.035 (0.026 for the one-pair bin). Updated in s21-2 (leak paragraph, with the widths), s21-4 (detector paragraph), s21-6 (checks paragraph; ϱ_i → ϱ^leak_i), summary text and tab:21-nuisances row. limit21_2a.py now computes Δ_i from hib21.pbin and logs the three factors (limit21_2a.log).
- guide21_7.py fermi_rel uses the prefactor 4 of Hayen et al. Eq. (6); rerun: guide21_7.log identical (the prefactor cancels in f_β).
- E.27: "non-negative" → "nonnegative" (two places).
- s21-2: "rises and falls once" → "is the difference of two nondecreasing functions with values between 0 and 1, its total variation is at most 2".
- Rebuild (-outdir=/tmp/claude-0/build-ch21rev): 0 LaTeX errors, 0 undefined citations. tex/ch22, E-14 and s10-6 not touched.
