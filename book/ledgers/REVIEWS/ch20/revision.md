# Chapter 20 revision (2026-11-06; brief briefs/reviews/ch20-revise.md)

Files changed: tex/ch20/ch20.tex, s20-1 … s20-5, s20-summary; tex/appF/F-rows.tex (Ch20 rows only); narrow edits in tex/appE/E-12.tex
(Luke rate) and E-25.tex (critical angle, τ_h → Δ_h, ℭ_s wording, ϖ_O range, 3–13 % reference, t_l factor 1.31, Leman locator);
NOTATION.md (Ch20 block, rows x_L → f_LA and t₀, ε₀ row extended to 20.1, clash entry 92).
Scripts: amm20_3.py (0 K Al primary; room-T sensitivity; Hill average; anisotropy ratios; lumped-form upper 10 % crossing),
fig20_3.py, limit20_3a.py (rerun on the new medium), qp20_4.py (Voigt 0 K c_LA; 60 nm film r = 0.72/0.94; arrival band 13.6–43.8Δ;
loss percentages; Ge decay-time spread), new film20_5.py (cascade yield to 120Δ, first-break probability, vector recursion for the
spectrum of phonons a film returns, energy closure 5.5e-5 against the fine cascade), kern20_5.py (rewritten: cascade yield, film
escape at the t_l/t₀ of 20.3, "lost" and "returned" variants, one and two films, f_LA = 0.093, operating point 0.84 meV,
band summary, new figure), disc20_5.py (low-bias spread model stated and recomputed at each recoil's own E_ph; bias grid to 1e-3 V;
binomial 1σ corner; S_sep meaning; t_rel), phon20_2.py (rms distance along the scaling trajectory at 0.95 ns), map20.py (rerun;
the brief's "map13.py" is the Ch13 script, so the Ch20 map was rerun instead). Logs: figscripts/ch20/*.log.
Figures regenerated: fig20_3, limit20_3a, fig20_4, limit20_4a, fig20_rcoll, fig20_5, map20. No QE.
Build: /tmp/claude-0/build-ch20rev, 0 LaTeX errors, 0 undefined citations; undefined references only to unwritten Ch21/22, B.2,
D.47, 9.x (pre-existing). No overfull box in Ch20. Lint: 0 blocking (warn tier: long sentences in captions/table rows; one EQ-PUNCT
false positive in 20.2). check_notation on tex/ch20: 0 gaps.

## Substantive rulings (done first, R3 before R1)

| Item | Status | How |
|---|---|---|
| R3 Al constants | done | amm20_3.py: AL = Voigt 0 K (114.3, 61.9, 31.6 GPa; ρ 2.70) → 6.63/3.30 km/s; room T (C.18) kept as AL_RT sensitivity. Rerun: t̄_Si→Al 0.938, t̄_esc 0.368 (DMM 0.282), 𝔫 ratio 0.392, v_s 3.50, t_l 0.187/0.244 ns, t_l/t₀ 0.72/0.94, factor 1.31, critical angles 54.6° (Si side), 21.5/29.9/37.7/47.5° (Al side), trapped flux 0.557, conversion max 0.17 at 76°, L-into-film 0.979/0.899/0.962, lumped factor 2.72 thin limit and 1.82 at 60 nm (ℓ_f = v_st₀), WE ℓ_f 0.909 µm, y_f 0.132, P_abs 0.422 vs 0.418; fit P_abs 0.320–0.586, ℓ_f/d_f 23.1–8.3 (AMM), 1.39–0.50 µm, specular 1.29–0.46, DMM 1.19–0.31 µm → "≈5–23"; naive reading 0.118–0.216; anisotropy 0.327/0.405, t_l 0.210/0.169 ns, t̄_Si→Al 0.927–0.943; interlayer t_min 0.844 (bare 0.994), 1 nm 0.901; Limit Check 20.3a window 1.146–1.242, correction ≤ 6.9 %, overstatement 2.70, reciprocity estimate 0.390. Room T in WE as sensitivity (0.327/0.259, 0.223/0.281 ns, 0.86/1.08; t_l +20 %). Propagated to 20.4 (c_LA 6.63 → v_F/c_LA 305, Δ/v_Fq 1.6e-3; 60 nm film r = 0.72–0.94: Y(10Δ) 0.383–0.409), 20.5 (t̄ 0.938; escape ratios), summary, nuisance table, F rows, E.25 (37.7°, 56 %). Ch15's 6.47/3.40 are [100] speeds: flagged (NOTATION 92(b); Ch15 light pass). Hill average moves t_l by 0.6 % (reader c). |
| R1 𝔯_coll | done | kern20_5.py + film20_5.py: 20.4's cascade (0.01Δ grid, 0.590/0.600 at 5.46Δ, escape-dependent) in units of each film's gap; film escape enters as p_pb on the absorption rate and the cascade yield of the first-broken phonon; DC-83 operating point 0.84 meV (text: "transport Monte Carlo"); f_LA = 0.093. Reproduces derivation-2 (two thick films 0.934/0.910 at 0.75 meV, 1.040 at 2.2, 1.088 at 3.05; one Al film r = 4: 1.109/1.056). New: identity eq:20.5-sign generalized with Ȳ_prim (exact to 1e-4 thick, within 0.011 with escape); the "returned" variant (escaped phonons re-enter the crystal with the cascade's spectrum) gives the thick-film values within 0.001 at every t_l/t₀ for one film type. Text: near-gap model lowers 𝔯_coll at 0.75 meV to 0.91–0.93 (stated); "outside every value of this estimate" removed; the band contains 1.128, so "transport alone does not exclude collection; the two-bias measurement of 19.5 separates collection from stored energy". Figure rebuilt with the 19.5 band 1.099–1.152, the 0.84 meV marker, the flat-yield reference and two one-film escape curves. |

### Final 𝔯_coll band (for the Ch19 amendment)
Mean-field silicon slab, 4 mm; Luke ⟨E_L⟩ 0.75–4.7 meV, operating point 0.84 meV (Si electrons, 1 V/cm):
- Thick films (no escape): two films 0.91–1.09 (0.92–0.94 at 0.84 meV); one Al film 0.96–1.00 (sub-gap lost), 1.00–1.02 (absorbed). Over both geometries and both sub-gap fates at 0.84 meV: **0.92–1.01**.
- Film escape with escaped phonons lost (lumped film): one Al film at 0.84 meV 1.01–1.05 (t_l/t₀ = 8, ≈600 nm), **1.05–1.10 (t_l/t₀ = 4, ≈300 nm)**, 1.14–1.21 (2), **1.30–1.53 (60 nm, t_l/t₀ = 0.94–0.72)**; two films 0.93–0.96 (8), 0.94–0.98 (4), 1.02–1.16 (60 nm).
- Escaped phonons absorbed again (one film type): thick-film values within 0.001 at any thickness.
- 1.128 (1.099–1.152) lies inside the full range; it needs thin films whose escaped phonons are lost to a sink without signal.
Ch19 pointer text should read along these lines: "0.91–1.09 for thick films; with film escape and escaped phonons lost, 1.05–1.10 at ≈300 nm and up to 1.5 at 60 nm; collection alone is not excluded by transport, and the two-bias measurement separates it from stored energy."

## Other rulings

| Item | Status | How |
|---|---|---|
| R2 memory times | done | 20.5 primary route, summary, nuisance row use 6.8/47 ns (band top), 0.15/1.0 µs (upper factor two), ~1 µs (22 meV TA), 13.5 % near-face at 1 µs; eq:20.5-primary written "≃" and called an estimate (bound 0.15 vs actual 0.012); "a few percent" removed; "toy cascade" removed. 20.2's "usually quoted" sentence cut. |
| R4 Luke rate | done | E.12 eq:E.12-luke replaced by the golden-rule form (k/k_s)², "grows as k²", Eq. (8) noted as low by k_s/k, Eq. (9) integrates to it. 20.1: one neutral sentence (angular law integrates to eq:20.1-luke; printed totals lower by k_s/k); open-problems "normalizations differ" removed; summary/table "published total rates low by k_s/k". |
| R5 numbers | done | 1.72 ↔ binomial 1.36 (WE, hv paragraph, summary, table; disc20_5.log); low-bias ceiling 10.8 (grid to 1e-3 V); film loss over the arrival band: the band itself was re-sourced (R6) to 13.6–43.8Δ, so the loss is 47–58 % at t_l/t₀ = 0.5 (41 % at 10Δ), 35–50 % for 60 nm (qp20_4.log); 15 % → about 13 %; 62 meV = band top (20.5), Ge 35.7 meV = band top (20.4); 45 meV spread 1.0 µm (phon20_2.log); hole Luke mean 1.1 meV (log 1.15); "4.4 meV"/"a quarter" → 5.0 meV energy-weighted (4.0 number-weighted), 18 % below 3 meV; face-sheet bound restated (vanishing slab; midplane 1.26e5 cm⁻² over the whole crystal; 10 h whole crystal, 5 h near-face limit); WE 20.2 δ^M sign (+0.39, −3.17, −6.72 %); fig 20.2 caption LA:TA energy shares 42:22; summary electrode sentence (85–92 % at or below 2Δ, ballistic); t₁ = 3.87 t_rel stated as root of e^{−x}(1+x) = Y_q at Y_q = 0.102. |
| R6 citations | done | Leman Sect. III G (20.5, E.25); eq:20.4-tpb attributed to Kaplan et al. (Leman only for α²F and the kernels); 0.7–2.7 THz dropped and replaced by the logged mean-field arrival band (2.45–7.88 meV, 0.59–1.91 THz, middle 80 % of absorbed primary energy; kern20_5.log), fig 20.4 tan band moved; ω_opt 64.1/37.6 meV → sec:5.2, tab:5-phonons, ε_eh 3.75 eV → sec:18.2 (Leman kept for Ge 2.96 eV); Ge anharmonic constant: both "Tamura" values (6.43e-55 Leman, 1.65e-54 Hernandez) given, factor 2.6 disagreement stated, slowest value used. "As quoted by" removed for Shockley–Ramo/Hecht (cite both), Kaplan, Tamura measured B, t₀; F row Hecht likewise. |
| R7 structure/prose | done | 20.5-verdicts subsection cut (its 21.7 pointer moved to the Summary); 20.5 points to f_s of 20.2 (eq:20.2-fs) instead of re-deriving; "not validated" kept in the opening, 20.1-open and Summary, reduced to a pointer in 20.5; E.25 pointers cut in 20.1 l90, 20.3 l7/l157 duplicate, 20.4 l75, 20.5 l57; count teasers named (20.1-open, 20.3 hypotheses, 20.4 three rates, 20.5 three effects/routes/two items, 20.2 proof); numerical assurances cut (20.3 3e-11, 6e-16; 20.4 1e-12, 2e-14; 20.5 1e-6); "percent" → \SI in 20.4; "Ref.~\cite" style fixed; 20.4 title "…Chang–Scalapino equations", "correction" coinage removed; looped open-problem sentences cut; 20.2 isotope re-derivation condensed to 11.6's result (one-line cubic-site reason); Limit Check 20.2b in book notation; 20.2-f/g; 20.3-a/c (impedance-law paragraph merged into the box); 20.1-a…j; 20.5-a…n; S-1…S-5; opening O-a…c. Register: "however" now in every section (20.2 sapphire, 20.3 ×3, 20.4 cascade, 20.5 HV ceiling), "we find"/"we will see" (20.1, 20.3), "as a result" (20.1); "so" at 1–3 per 1,000 words. US spelling kept. |
| R8 notation | done | t₀ stays the pair-breaking time; 20.5 track time → t_rel (19.5 rename owed by the coordinator); b(t) → f_ret; f_soft/ω_op → f_s/ω_opt; ε_0 SI sentence reworded with ε₀^SI (entry 2 convention); one x_L: renamed f_LA (addendum), value 0.093 everywhere (kern20_5 switched from 0.0975; 0.0975 named as the isotropic-speed value in 20.2); F_eh convention stated in 20.1 WE and 20.5 (0.114 cascade, 0.119 measured); one Al sound-speed set (6.63/3.30); Γ_em → Γ_qp,em; b → b_α; 20.5's p(u), u, γ removed; \operatorname{Var}; ~85 new symbols in 15 rows; clash entry 92. |

## Report items not covered by a ruling

| Item | Status |
|---|---|
| deriv-1 f_s cap "6 to 9 meV" | done |
| deriv-1 20.3 thin-limit reciprocity reason for the fit | done (one sentence in 20.3-fit) |
| deriv-1 Martinez wafer thickness | done ("300 to 380 µm") |
| deriv-1 ε₀ = 11.4 at mK in 20.1 | done (NOTATION ε₀ row extended to 20.1; book-wide 11.4/11.7 note stays with the editor) |
| deriv-2 A1 unconditional yield | already stated (yield per first-broken phonon; absorption probability separate) |
| deriv-2 MC "1.2 standard errors" | done |
| deriv-2 Ge decay "0.1–1 s" | done (qp20_4.log 0.12/0.31/1.25 s) |
| deriv-2 v_F/c with ρ 2.73 | superseded by R3 (Voigt 0 K at 2.70 → 305) |
| deriv-2 Y′_q vs Y_q in low-bias route | done (numbers use Y′_q; stated) |
| deriv-2 224 eV edge interpolation | done |
| reader-a P_d energy-weighted | done (P_d = 2y p(y)) |
| reader-a Luke azimuth bookkeeping, l₀ meaning, "deposit ω", conductivity mass | done |
| reader-a lumped form re-enters 10 % band above 0.55 | done (amm20_3.log 0.551; 20.3 and F row) |
| reader-a ±Q_z convention | done |
| reader-a/b low-bias thresholds 0.13/0.24/0.45 not reproducible | done: model stated (equal E_R, own E_ph per recoil, Y′_q, binomial F_eff); recomputed 0.11/0.22/0.43 at 10–12 V, matching both readers |
| reader-b S_sep = 2 meaning; correlated bands | done (84 %/84 %, 1e-3 needs 6.2; corners treat bands as uncorrelated) |
| reader-b ρ_g reminder | done |
| reader-c v_F in m/s, Hill average, Debye usage | done |
| reader-c why 3.8 eV | done (one clause) |
| prose 20.2-e (repeat of the 69 eV example) | kept (acceptable per the report) |
| reader-a TV numbers 0.13/0.026/0.015/0.012 "could be cut to two" | kept (each is logged and the 1 µs value is used by 20.5) |
| PDF "guide to next targets (??)" | forward reference to sec:21.7 (unwritten), moved to the Summary |

## Changes owed in campaign ledgers (not edited here)

- **state/CORRECTIONS.md**
  - Row 656/657 (𝔯_coll): replace "transport ≤ ~1.09 / collection alone disfavored" by the band above: thick films 0.91–1.09 (0.92–1.01 at 0.84 meV); with film escape and escaped phonons lost 1.05–1.10 (≈300 nm) and 1.30–1.53 (60 nm) at 0.84 meV; escaped phonons absorbed again → thick-film value; 1.128 not excluded by transport. The ramp-yield numbers (−0.048, +0.06, 0.892/0.900, 1.094/1.040) are superseded by the cascade (+0.002/+0.018; +0.13/+0.11 at r = 4; 0.934/0.910; 1.088/1.040). The toy 0.87–0.98 stays superseded.
  - §19.13(g) Al constants: 20.3 now uses the 0 K Voigt set (6.63/3.30 km/s at 2.70); log that Ch15's "6.47/3.40" are [100] speeds at ρ 2.73, not isotropic averages (Ch15 light pass); C.18 room-T constants are a sensitivity in 20.3.
  - CW6 row l.345 (AMM 0.32/DMM 0.26/×1.26): becomes 0.368/0.282/×1.31 with 0 K Al; ℓ_f/d_f 5–23; do not quote a_opt.
  - Memory-loss times (l.441 δ_coll^prim ≤ 0.012 and IF-E7 δ_prim ≤ 0.007): the transfer-kernel bound is 0.15 at 1 µs for the model births (actual 0.012); f_s = 0.017 only when E_mem lies below every hard birth; the primary-route number is an estimate.
  - Luke rate: G4CMP Eq. (8)/Leman Eq. (21) low by k_s/k (E.12 fixed); DC-83 ⟨E_L⟩ 0.84 meV at 1 V/cm used as the operating point; 20.1 balance 1.09–1.15 meV is an overestimate.
  - HV ceiling: 1σ corner 1.72 is the mean-charge limit; binomial 1.36. Low-bias route: 0.11/0.22/0.43 (was 0.13/0.24/0.45); ceiling 10.8 (was 10.3).
  - Film loss over the detector band: 47–58 % at t_l/t₀ = 0.5 over the mean-field arrival band 13.6–43.8Δ (not "up to 40 %", which is 10Δ).
- **state/SOTA.md**
  - l.540, l.581 ("≈10 ns / 30–100 ns, ≲ 0.1 mm"): superseded by 6.8/47 ns (band top), 0.15/1.0 µs (upper factor two), ~1 µs for 22 meV TA; r_rms 0.54 mm at 1 µs; 13.5 % near-face shell.
  - l.695 ("transport ≤ ~1.09"): replace by the R1 band; collection alone not excluded by transport.
  - WP8-R HV verdict: add "(mean-charge limit; binomial 1.36)" to the 1.72.
- **LOOSE-ENDS**
  - New: fate of phonons that escape a sensor film in a real detector (lost to uninstrumented metal/holders vs reabsorbed) — decides whether film escape raises 𝔯_coll (1.05–1.53) or not; needs the DC-78 kernels with the film-return spectrum.
  - New: Ge anharmonic constant — two values both attributed to Tamura (6.43e-55 Leman, 1.65e-54 Hernandez), factor 2.6, unresolved without the primary.
  - ε₀ 11.4 (mK) vs 11.7 (room T) book-wide: unchanged, NOTATION allows 11.4 at mK (18.5, 20.1).
  - The cascade α²F ∝ E² is used up to 120Δ_Al in kern20_5 (2.4 % of primary energy above 60Δ, 0.08 % above 120Δ).
- **NOVELTY**
  - Add: one-film-type identity 𝔯_coll − 1 = s_ng − (1 − κ_sub)s_sub with Ȳ_prim; the result that film escape changes 𝔯_coll only if escaped phonons are lost (returned variant = thick film within 0.001); 0 K-Al reciprocity reading of the fitted Si→Al coefficient (ℓ_f/d_f 5–23).
- **DEFERRED-COMPUTE**
  - DC-78 (kernels): add the film-return spectrum (film20_5 vector recursion) and the lost/returned switch to the spec; report 𝔯_coll at 0.84 meV for 60 nm and ~300 nm Al.
  - Unsized: Luke-rate transverse-phonon correction (20.1) stays unsized.
  - Ch15 light pass: label 6.47/3.40 km/s as [100] speeds.

## Changes owed in Ch19 (coordinator; not edited here)
- 19.5 l.151, l.193 and the 20.5 pointer: the band above; remove "largest transport value 1.09 … collection alone is disfavored".
- eq:19.5-bimol: rename the track time t₀ → t_rel (t₀ is the pair-breaking time of 20.3/20.4; NOTATION entry 92).
- F-rows Ch19 row (F-rows.tex l.800, Limit Check 19.5b): "0.935–0.998 … up to 1.04–1.09" → the new band.

## Post-check rework (2026-11-06; ledgers/REVIEWS/ch20/postrev-check.md, REWORK on R1)

**This section supersedes the "Final 𝔯_coll band" and "Changes owed in Ch19 / CORRECTIONS / SOTA" items about 𝔯_coll above.**

| Item | Status | How |
|---|---|---|
| R1(a) selective sink | done | kern20_5.py rewritten: the default ("conserved") returns every phonon a film emits after its first pair break (relaxation and escaped phonons, film20_5 spectrum) for **both** films; energy closes to 1e-5 (signal + bare loss + dropped sub-Al-gap returns). The old "lost" variant is kept and labelled a selective sink / upper envelope. New "uniform sink" variant: bare-face loss 1e-3, 0.01, 0.1, 0.3. |
| R1(b) two-film relaxation phonons | done | Nb-like relaxation phonons now return and are collected by Al: ε_prim 0.684 (was 0.610), a_prim 0.610, ϖ_O 0.39 (0.12/0.045/0.019 at 2/2.9/4.7 meV). Two thick films 0.81–1.01 over 0.75–4.7 meV, 0.82–0.84 at 0.84 meV; two 60 nm films 0.85–1.01. |
| "within 0.001" | done | now "within 0.002 (max 0.0016 at 60 nm), numerical, at ℓ_bare = 1e-3; a returned phonon continues the same cascade; return-path loss and decay break it". |
| text | done | 20.5 mean-field and sign subsections, Fig. 20.6 (new curves: two thick films conserved; two 60 nm films conserved; lumped-film two-film reference; one 60 nm film selective-sink envelope), Summary, nuisance row, F row, 20.4 open problems, E.25 ϖ_O range (0.02–0.39). |
| 20.5 operating point | done | "0.84 to 4.6 meV for silicon electrons over 1–100 V/cm" (DC-83 0.840/1.90/4.62); scan 0.75–4.7 meV labelled as also covering germanium; kern20_5 docstring updated. |
| ρ 2.70 vs 2.73 | done | one clause in 20.3 (2.70 is the book's density for impedances and rates; 2.73 gives 6.59/3.28 km/s and t_l +1.6 %, amm20_3.log). |
| HV 1.36 | done | "1.36 at f_det = 0.873; 1.52 at full collection" in WE, hv paragraph, Summary, table (disc20_5.log). |
| nits | done | "beside them" (20.1); phon20_2 prints f_LA. |

Build /tmp/claude-0/build-ch20rev: 0 errors, 0 undefined citations. check_notation ch20: 0 gaps. Lint: 0 blocking.

### FINAL 𝔯_coll band (kern20_5.log, "band summary")
- **Energy conserved** (all film phonons returned; one Al film or Nb-like + Al; t_l/t₀ = 0.72 (60 nm) to ∞; sub-gap lost or absorbed; one-speed or spread Luke spectra): **0.81–1.02 over ⟨E_L⟩ = 0.75–4.7 meV; 0.82–1.01 at the operating point 0.84 meV** (Si electrons, 1 V/cm). One Al film 0.96–1.02; two films 0.81–1.01.
- **Uniform signal-free sink** (bare loss up to 0.3/hit, ε_prim down to 0.08): max **1.023**.
- **Selective sink** (lumped film: phonons emitted after the first pair break deleted), upper envelope, no physical realization identified: one Al film at 0.84 meV 1.05–1.10 (≈300 nm), 1.30–1.53 (60 nm); two films 0.91–1.09 thick, up to 1.19 at 60 nm.
- 1.128 (1.099–1.152) is **not reached** by any energy-conserving case.

### Exact Ch19 pointer text (for 19.5 l.151/l.193 and the Ch19 F row)
"The mean-field transport estimate of \cref{sec:20.5-sign} puts the collection ratio between 0.81 and 1.02, and between 0.82 and 1.01 at the mean Luke energy of silicon electrons at \SI{1}{V/cm}, for one or two films of any thickness down to \SI{60}{nm} with energy conserved; values up to 1.5 arise only for a selective sink that the estimate does not identify in a detector. Collection alone, $\mathfrak{r}_{\mathrm{coll}} = 1.128$, is therefore not reached by the transport estimate, but it is not excluded until computed kernels test real detectors (\cref{app:E.25}); the two-bias measurement decides."

### Ledger rows replacing the 𝔯_coll items above
- CORRECTIONS 656/657 and SOTA l.695: replace "transport ≤ ~1.09 / collection disfavored" (and the first-pass "1.128 inside the range, not excluded") by the FINAL band and the pointer wording; record that the first-pass two-film 0.91–1.09 and ε_prim 0.610 deleted the Nb-like film's relaxation phonons (non-conserving), and that the 1.05–1.53 escape values require a selective sink.
- LOOSE-ENDS: the "fate of escaped phonons" item becomes "a selective sink of film-emitted phonons in real detectors (unidentified); the computed kernels (DC-78) should report 𝔯_coll with film phonons returned".
- DC-78 spec: film-return spectrum for every film (film20_5) is mandatory; report the conserved value.
