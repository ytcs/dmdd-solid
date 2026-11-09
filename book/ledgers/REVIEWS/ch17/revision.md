# Chapter 17 revision (2026-11-06): item → done/how

Files changed: tex/ch17/ch17.tex, s17-1 … s17-6, s17-summary; tex/appF/F-rows.tex (17.5 row); NOTATION.md (Ch17 block, clash entry 88);
figscripts/ch17: abs17_2.py (Ch16 measured-structure ZrTe5 row), exo17_3.py (NiO c_M 1.36e-4, parabolic plasmon cutoff, NiO weight
decomposition), sectors17.py (one-phonon cap at the band top), map17.py (tag), new check17.py (every number the revised text quotes that no
other log printed). Reran: abs17_2, exo17_3, sectors17 + fig17_sectors, map17, map13, check17. Not rerun (inputs unchanged): fom17_5,
fig17_window, pol17_5, limit17_5a, rank17_6, interf17_4. No QE. tex/ch12 and D-33/D-34 untouched.
Build: latexmk -outdir=/tmp/claude-0/build-ch17rev (result at the end). Lint: 0 blocking; the remaining LONG-SENT hits are captions and table rows;
EQ-PUNCT at the cases display of eq:17.3-endolin and the split of eq:17.4-Sek are false positives (punctuation inside the environment).

## R0 — Migdal at q < q_BZ: pending Ch12 erratum (numbers NOT changed in this pass)
Marked "pending Ch12 erratum" (a follow-up pass applies it):
- 17.1: the Migdal crossovers ω_th^× (tab:17-crossover, now a table), the Migdal rates, the zero-phonon shares, the 13.2 MeV equality, the
  Migdal floor band and the 0.006 eV local-field shift (all from the diagonal soft limit at every q, eq:12.3-soft/12.4-harm).
- 17.4: the lock eq:17.4-lock itself is the identity the erratum rests on and stays; no Migdal number of 17.4 depends on 12.4 below q_BZ.
- 17.5: the Migdal pole factor (0.87 LiF, 0.47 Ge; 5.7e5; 1.1e5/3.2e4) and tab:17-fom Migdal row.
- 17.6: the Migdal row of tab:17-rank (0.315, NaF 1.000 at r = 1, medians), the X_pole prior, the nuisance row.
- No "q ≳ q_BZ" qualifier and no coherent-Migdal nuisance row were added (derivation-2 §A, §E suggestion), per R0.

## R1 — number errors
- WE 17.4 GaAs: now "without the cross cell 403× (Ga)/521× (As); bare nuclear charges alone 216/245, before the ε∞ screening both share"
  (check17.log). Also answers reader-a (does 216 include ε∞?).
- 17.3 elastic rate: reconciled from exo17_3.log. The elastic pair rate is 16.73 (= the "17" of the opening/17.1/summary) and the elastic
  phonon rate 975.9; the sentence now states the elastic values first and the 1.12/1.39 factors after (the old wording made 976/16.7 read as
  the exothermic rates, which is what led reader-b [D3] to 12.0 and 871). Phonon factor: the log gives 31.05 at |Δ| = 10 eV and 32.4 at
  10.3 eV; text says "raised by a factor of 31 at 10 eV" (summary: 31 at 10 eV). **Deviation from R1:** R1's "37×" follows from [D3]'s
  misread elastic 871; the log value 31 is kept. Gain 3e6 at 80 eV checked against 16.73.
- WE 17.2: the 40 meV is right for the full edge of eq:13.8-edge (abs17_2.log: 40.4 meV, further replicas open); the square-root onset alone
  gives 122.7 meV (check17.log). Text now says both. 4.6 cm⁻¹ → 4.3 cm⁻¹ (ε₂ = 2.54e-4 converted with n_r = 3.48, the index used in the
  WE; the script's 4.58 uses √ε∞ = 3.30; check17.log). Lorentz 0.008 unchanged (0.0081).
- NiO ratio 3.1: decomposed with the new log lines (exo17_3.log): 3.77 (v_ν/⟨v⟩) × 0.676 (F²: 0.599/0.885) × 1.137 (weight: 1.149/1.010)
  = 2.90; the remaining 8 % is stated as the elastic halo weighting. "it" ambiguity removed.
- tab:17-endo NiO row with c_M = 1.36e-4: 7.31/8.20/316 keV (exo17_3.log); caption "fastest magnon speed of the J₁–J₂ model".
- CsI 25 % above (check17.log 1.252). η-shift nuisance 7 % (0.9328). GaAs polar edge 10.35 keV everywhere (17.1 text, tab:17-boundaries,
  summary).
- "about 500 MeV" → 410 MeV (413.6, check17.log); "escape speed" → v_max; Ge Θ_D 373 K; zone average 1.156 with 1 + 2ΔS = 1.157 (ΔS
  defined); "against 32" → "32 for the GaAs phonon and 46 for the NiO magnon" (check17.log 32.2/45.6).
- "about 8×10⁵" → 7×10⁵ (4.41e4 × 16.73 = 7.38e5, check17.log; reader-a) in the opening, 17.1 and the summary.

## R2 — ZrTe₅ rerun
abs17_2.py now uses the measured-structure row of 1910.10716 (v = 1.1/0.45/1.0e-3, Λ = 0.23/0.215/0.1 Å⁻¹, Λ̃ = 0.191 eV) with Δ_D = 11.8 meV,
and the relaxed-cell ISIF7 row (Λ̃ = 0.180 eV) with 15.6 meV. Log: ζ(100 meV) = 1.25e-15, factor 6.29–6.39 ("6.3 to 6.4"), cone end 0.382 eV.
Text: 6.3–6.4; tab:17-abs-decades 1.25e-15, "ZrTe₅ to 0.38 eV; none from 0.38–1.17 eV"; coverage paragraph and summary 0.38 eV; fig17_2.pdf
redrawn; caption names both rows; nuisance row now states the two rows (onset 23.6 vs 31.2 meV, reach at 100 meV differs by 2.5 %).

## R3 — counting vs coherent
"A coherent detector overtakes … below ~T" removed; the gray band is now "where the advantage of counting has vanished". Bandwidth assumption
added to the key result (counter band = line width Δω_eq; band B multiplies the ratio by (B/Δω_eq)^(−1/2); Lamoreaux's cavity counter carries
(Q_c/2πQ_a)^(1/2), his Eq. (18)). Squeezing/dark counts now "reduce the advantage" (no crossover). Summary: "advantage vanishes well below T".
Nuisance row updated.

## R4 — YIG dark-photon point
Kept, with the derivation line in 17.2.2: substitution of 14.3, random polarization, ratio e²⟨|(v×ê)⊥|²⟩/⟨v⊥²⟩ = 0.0451 (abs17_2.log),
ζ = g_aee/0.212 = 7.6e-17 at 10 µeV.

## R5 — 17.5
- WE 17.5: "ranks correctly at every mass above the edges" → "ranks the pair correctly above 14 keV, 2.2 Si edges, where the rates cross;
  below that the softer crystal's cut reverses the order" (crossing 14.0 keV from fom17_5_rates.npz, check17.log).
- eq:17.5-pole: dispersion stated and sized (new paragraph): Bohm–Gross ω_p^(−2) → LiF/Si 1.37, free-particle-dispersion ω_p^(−3/2) → 1.72;
  Ge 0.42–0.44 (check17.log); "even the order of LiF and silicon depends on the dispersion". 0.87 kept as the dispersionless value (R0).
- Ge pole factor: 3d core-screening/hybridization caveat (unsized). LiF: F 2s / Li 1s caveat on condition (ii) (persona c).
- Polar log formula: v ≃ v₀ stated; asymptotic 0.79/0.87 and 54 MeV against the full 0.77/0.87/52 MeV (check17.log); with v_max it would
  give 0.87 at 1 MeV (reader-b) — not printed.
- 17.5.7 removed; its one new fact (absorption figures of merit exact at each mass) moved to the tab:17-fom caption; the table is introduced
  at the end of 17.5.1. The polar subsection now points to we:11-ipol/lim:11.2d instead of restating Ch11 (0.1415/0.153/9.12/19.0, 103 = 134 ×
  0.77, sapphire 7 %/2.1, GaAs 8 %, 3.5 removed).
- Also from derivation-2/readers: f-sum "applies unchanged" → stated for the model function ε_m, with the intermediate-asymptote remark (and
  the F row updated); "1.1e5" → "1.1e5 for the energy integral, 3.2e4 with the nuclear factor"; κ_η, Z_val, A_cell, N_κ, L_Mig,κ defined;
  "We name its inverse" → "Its inverse is"; Brillouin scattering and Laue class replaced (light scattered by thermal sound waves; "point group
  4/m, which allows C16 = −C26"); straight quotes fixed; km.s⁻¹ → km/s; the five-crystal audit is now tab:17-speeds with the constants stated
  (prose items 79–81; reader-a pace); Vallin cited "[abstract]"; process sentences (bulk-modulus floor used only for CsI; "a tabulated speed
  is therefore an input to be checked") removed; disclaimer of l.3 removed.

## R6 — 17.6
- X_pole: kept as a device, stated so; X_Si ≈ 25 from the 4 % plasmon share of 12.3 (check17.log); medians and P(first) of the Migdal row
  called prior artifacts; tab:17-rank caption says the Migdal medians include √3 = 1.73; row label "Migdal pole factor times X_pole";
  "pole-free value" → "value at X_pole = 1"; widths-table caption calls the prior a device. "No reading" kept. (Prior not rebuilt: the
  book's own numbers give one crystal only, and a wider prior only widens the intervals; rank17_6 not rerun.)
- tab:17-widths: GaAs 𝓘_pol 0.04 added ("half the spread of its dielectric and splitting routes", as rank17_6.py); caption now matches the
  text (speed and gap widths tested in 17.6.1).
- 17.6.1 rewritten: opener cut after the question + one "we will" sentence; hedge stack cut; process sentences of l.31 removed (book values
  replace…, Christoffel reproduces…, Griffin CaWO₄ not used); CaWO₄ tensor not repeated (pointer to tab:17-speeds); pool gaps and LiF/NaF
  Z*, ε∞, ω stated (check17.log); JARVIS functional named (OptB88vdW); "in the pool" (D14).
- 17.6.5 rewritten: leader list cut; the two opposite-running pairs kept with numbers; "GaAs 134 below LiF and 64 below sapphire" (D10);
  reduced "readings differ" paragraph to diamond 1.66 and LiF's factor of two; disclaimer removed; CsI "at most 4.5 % denser"; title
  "Rankings of the scattering channels".
- Also: Φ defined; "we show this by changing the width" and "a reader who trusts…" removed; tier stated positively and the 60-word sentence
  split; the looped paragraph after WE 17.6 removed (its fact merged into the WE); TeO₂ vs CaWO₄ with the database offset 0.987 → 0.956 added
  (derivation-2 suggestion; check17.log); Fig. 17.8 shift convention explained (the lead salts' listed gaps are low-temperature values,
  unshifted; reader-a).

## R7 — figures and tables
- fig:17-sectors(a): one-phonon deposits capped at the band top 63.7 meV (sectors17.py); rerun: class 1 now ends at the 60.3 meV grid row
  (was 67.6); no other label or printed number changed (sectors17.log identical otherwise; fig17_sectors.log). Caption says so.
- tab:17-boundaries: GaAs zero-phonon edge "L channel 0.517–0.560 (Γ pair closed)"; floor row renamed "Kinematic floor"; "(model)" now
  "property of the model"; caption standalone.
- Plasmon window: parabolic dispersion meets qv_F + q²/2m_e at 2.30 keV, window 7.3 eV (exo17_3.log 2304 eV, 7.33 eV).
- map17.py: "Limit Check 17.1"; rerun. map13.py rerun (unchanged content).

## R8 — prose (117 items) — all applied unless noted
Opening: items 1–3 (atlas clause added for persona b; disclaimer once, positive). 17.1: 5–26 (opener; title "Kinematic ceilings of the
sectors"; cross-section hyphen; σ_p; deleted "two maps below…"; "The nucleon-coupling map uses four responses"; labeled; caption no longer
repeats the label criteria; CAL l.15 applied; 52-word sentence split; "the value at 100 MeV is the one of 12.3" deleted; x_R and ⟨u_x²⟩
defined; l.42 recap removed and its new fact merged into the Migdal paragraph; count-teaser fixed; screening clause of l.11 cut, l.50 kept;
Ge crossover sentence moved to the open problems only; GaAs recap sentence deleted; 10.35; split; caption; run-in "Open problems" heading
dropped). The crossover numbers are now tab:17-crossover (reader-a pace). D13: "the sum of higher orders overtakes it at 2W = 1.26"
(check17.log). Coherence clause for the one-phonon contours below 3.4 MeV (derivation-1 PRIORITY suggestion). D5: the 2.59e-5 is defined
(mean nucleon number per mass, 1.001072 and 1.001046 per u, we:8-nucleon).
17.2: 27–38 (γ_L, c̃ defined; caveats compressed to one clause; l.55 recap cut; "two targets"; Lamoreaux Poisson remark moved into the
key-result note; gray-band sentence rewritten; seam "Unlike scattering"). D7: 11.7 at room temperature / cold 11.4 for donors. Reader-a: the
per-bin rms sentence. Si ALP row "to 1 keV" (derivation-1 GAP). n_B always with its argument.
17.3: 39–56 (title "Inelastic scattering into collective modes"; outline tail; symbols A_κ, c_4, F^mag, w^M pointed; 70-word sentence split;
restatement after the box cut; ΔS defined; NiO sentence split; Larmor sentence positive; \bar L pointer; q_Δ defined via q_ν; l.88 rewritten;
l.90 end cut to one sentence; CAL l.92 applied ("Of course … the upshot"); en dash; endolin punctuated; "kilogram and year" throughout).
Reader-a/b: (v_max/v_ν)² ≤ 0.34 now quoted for 10.3–80 eV; WE heavy 0.012 stated as the full integral (shell 0.010, light shell 2620).
Seam C6: "Back in scattering".
17.4: 57–69 (n_B → "first Born–Oppenheimer order"; θ_ep defined; "First,"; "That limit is the content…" deleted; mass-proportional teaser
paragraph deleted and its content folded into the key-result discussion; CAL l.85 applied; l.94 recap cut; l.110 reduced). GaAs numbers
moved from 17.4.1 to the WE (item 59). R8 "17.4.2: add the steps": the boost amplitude eq:12.1-amp is restated and the three steps (one-phonon
term, cell sum, p-sum) are written out. Reader-b: δ_w and edge shell pointed to 8.6; Higgs-portal/B−L clause. Derivation-2: S^PA as the joint
two-label response in the bound; lock "exact amplitude, in the notation of eq:17.4-Mmig"; O(qa) → O(q/q_BZ); the phase clause (i vs −i of
eq:A.6-g). F_κ → F^fol_κ.
17.5: 70–86 (see R5). 17.6: 87–107 (see R6). Summary: 108–117 (17.4/17.5 split; Dirac process sentence deleted; 15.4 condition clause
dropped; endothermic sentence replaced; 1810; 7 %; L(p, ω); disclaimer kept here; nuisance ZrTe₅ process note removed). Summary citation
11.1 → 17.5 for 1.73/0.46 (derivation-2). D15 fixed.
Cross-chapter C1 (disclaimer in the opening and summary only), C2 (CaWO₄ tensor once), C3 (stiff-lattice / polar reversal once in 17.5 +
17.6 numbers + summary), C6 seams, C7 titles. US spelling ("labeled"); "cross-section" hyphenated. 21.7 references are plain prose ("the guide
to next targets at the end of the book"); the undefined \cref{chap:19,chap:20} in 17.1 is plain prose too.

## R9 — notation (NOTATION.md Ch17 block + clash entry 88)
σ_n → σ_p (per nucleon); n_B: BO order in words in 17.4, Bose function n_B(m_φ) with argument in 17.2; ω_top → ω_max; ω_× → ω_th^×;
F_κ → F^fol_κ; σ_j → σ^prov_j; new rows for 17.2–17.6 symbols (list in entry 88). check_notation.py: 0 gaps.

## Items considered and not changed
- R1 "37×": see above (log gives 31 at 10 eV).
- Persona-b: LiF/NaF medians 18.9/9.93 vs inputs 18.99/9.95: lognormal medians equal the inputs up to Monte Carlo noise (0.2–0.5 %); no change.
- Persona-c: RPA plasmon-dispersion caveat for real Si: no sourced number; not added.
- Derivation-1: Si ε₁ 11.7 vs 11.4 kept as 11.7 (book ruling App E: 11.7 throughout), with the cold 11.4 named for the donor factor.
- Ge crossover and GaAs acoustic edge stay "not evaluated" (inputs absent; DEFERRED candidates below).

## Owed campaign-ledger changes (not edited here)
- state/CORRECTIONS.md: (1) NiO magnon edge with c_M = 1.36e-4: 7.31/8.20/316 keV (supersedes 7.16/8.05/317 of the Ch17 draft, which used
  the J₂-only 1.39e-4 of row 628). (2) ZrTe₅ absorption in Ch17 now on the measured-structure row: ζ(100 meV) 1.25e-15, factor 6.3–6.4,
  cone end 0.38 eV, dark-photon gap 0.38–1.17 eV (supersedes 6.2–6.3, 1.2e-15, 0.36 eV). (3) Griffin et al. Table I CsI: floor 25 % above the
  tabulated speed (not 20 %). (4) Chapter-17 symbol renames of NOTATION entry 88; 12.3/12.6 still print σ_n (clash with 15.4 σ_n) — owed at
  their next pass. (5) GaAs WE 17.4 factor: 403/521 without the cross cell, 216/245 bare nuclear charges.
- state/SOTA.md: Book-phase corrections, Ch17: (a) counting vs linear readout — ratio e^{m/2T} holds for a counter whose band is the line;
  no coherent crossover below T (the advantage tends to one); (b) Migdal pole factor depends on the plasmon dispersion (LiF/Si 0.87
  dispersionless, 1.37–1.72 dispersing): ranking of Migdal targets open, now more so; (c) X_pole prior [1, 3] is a device; Si's own X ≈ 25;
  (d) heavy-mediator diamond/Si order reverses below 14 keV.
- state/LOOSE-ENDS.md: (a) Ch12 erratum application to Ch17 (R0 list above) — follow-up pass; (b) book-wide GaAs density 5.361 vs Ch11 R6
  lattice constant (17.2 WE uses 5.361); (c) Ge a = 5.652 vs 5.658 Å (c_NR1 +0.16 %, no printed probability changes); (d) Vallin 1964 CsI
  constants read in abstract only; (e) Skauli 2003 / Franta 2017 refractive indices not checked against source (closed access).
- state/NOVELTY.md: no verdict changes. Note for the Ch17 entry: the NiO exothermic ratio now decomposed (speed × form factor × weight, 92 %),
  and the YIG dark-photon point carries its derivation line.
- state/DEFERRED-COMPUTE.md: (a) measured or DFPT elastic tensor of GaAs (P(GaAs ≻ Ge) 0.884 → 0.741 with the database offset) and of TeO₂
  (P(first) 0.968 → 0.781 at doubled width); (b) germanium phonon DOS (multiphonon–Migdal crossover in Ge) and GaAs elastic tensor for the
  acoustic edge; (c) L(p, ω) near the gap at p of several keV for LiF, NaF, Ge (Migdal figure of merit; dispersion now a factor-2 nuisance);
  (d) Ge core screening ε_core(0) (3d shell) for the pole factor — unsized; (e) silicon one-phonon contours below 3.4 MeV carry the coherent
  correction of 11.3 (>10 % below 18 keV) — unsized in Fig. 17.2a.

## Build
latexmk -pdf -outdir=/tmp/claude-0/build-ch17rev main.tex: 0 LaTeX errors, 0 undefined citations; every \cref in tex/ch17 resolves (the
248 undefined references of the book are to unwritten chapters such as chap:19/20, none from Ch17). Overfull boxes remain in display math
(eq:17.4-Mmig, ~73 pt, unchanged from the draft) and in the narrow table columns; left for the figure/layout check.

## Ch12 erratum applied (2026-11-06; follow-up to R0)
Source: ledgers/REVIEWS/ch12/erratum-migdal.md (verdict PARTLY). No Ch17 number changes; every R0 item resolved as follows.
- 17.1: numbers kept (crossovers, Migdal rates, zero-phonon shares, 13.2 MeV, 0.006 eV). Domain qualifier added after the Migdal opening
  (s17-1.tex): up to 1 MeV the Migdal rate comes from 0.75 keV ≲ q ≲ 2 q_BZ, where the coherent response is not computed; the 0.32–1 MeV band
  and the 1 MeV column of tab:17-crossover (29 % from q < q_BZ) carry that unsized factor; ≤ 7 % of the rate from 3 MeV on. fig:17-sectors
  caption: Migdal region below 1 MeV carries the unsized factor. New tab:17-nuisances row "Coherent Migdal response at q < 2 q_BZ"
  (14.9× as q → 0; quantitative only below ≈ 0.75 keV; band shares). Logs: figscripts/ch12/migdal_rates12.log (f(0.75 ≤ q < 2q_BZ) = 1.000 at
  0.7–1 MeV, 0.327 at 2, 0.074 at 3, 0.003 at 6.3 MeV; f(q < q_BZ) = 0.287 at 1 MeV), migdal_ratio12.log (14.88), migdal_coh12.log.
- 17.4: unchanged. eq:17.4-lock is eq:8.3-boostward on the one-phonon sector, consistent with the erratum; "order of magnitude only" kept
  in the window row (the Si window at 0.9–1.3 keV lies outside the ≲ 0.75 keV domain).
- 17.5: unchanged. The pole factor and tab:17-fom Migdal row are impulse-regime (q ≫ 2 q_BZ) objects; the ×1.2–1.4 applies there.
- 17.6: unchanged (built on the 17.5 pole factor); nuisance row unchanged.
- tab:12-nuisances quotes the model domain as "within 15 % for q ≤ 0.75 keV" (migdal_coh12.log 1.152).
- Note: the band 0.75 keV–2 q_BZ holds essentially all of the rate at 0.42–1 MeV, not only the 29 % below q_BZ quoted in the erratum.
Build: latexmk -outdir=/tmp/claude-0/build-erratum: 0 LaTeX errors, undefined references unchanged (32 keys, same set as build-ch17rev).

## Post-check fixes (postrev-check.md, ACCEPT WITH FIXES; 31× confirmed)
- F1 s17-1: the sum rule eq:12.4-harm "holds at every momentum transfer in its incoherent form", with a pointer to the Migdal-band qualifier and tab:17-nuisances.
- F2 s17-1: "is not known to equal the coherent response"; added that near threshold the factor is likely a large suppression (the exact small-q
  spectrum sits at the plasmon, beyond the energies open there); the whole 1 MeV rate is now said to lie in the band (29 % of it below q_BZ);
  a third at 2 MeV, ≤ 7 % from 3 MeV (migdal_rates12.log: 0.327 at 2 MeV, 0.074 at 3 MeV).
- F3: fig:17-sectors caption "below about 2 MeV (7 % of it at 3 MeV)"; nuisance row adds "33 % at 2 MeV".
- F4: tab:17-speeds ZnO 2.05 (12.53/6.10).
- F5 s17-6: the "wider or crystal-dependent prior only widens" claim replaced: a wider prior widens; a gap-dependent prior, and the pole
  dispersion for LiF (0.87 vs 1.37–1.72), would favor small-gap crystals, so the Migdal order is open, not merely unresolved.
- F6 s17-2: for m_φ < T the counting advantage "has fallen below e^{1/2} and tends to one".
- F7: missing spaces after the periods in the fig:17-sectors caption and the Migdal-band paragraph fixed.
- Rebuild (-outdir=/tmp/claude-0/build-ch17rev): 0 LaTeX errors, 0 undefined citations, every Ch17 \cref resolved. tex/ch12 untouched.
- Owed ledger changes, in addition to the list above: CORRECTIONS — withdraw the R1 ruling "37×" (the log value 31× at 10 eV stands);
  Griffin et al. Table I ZnO tabulated/measured-max ratio 2.05. SOTA — the Ch17 Migdal pole-factor ranking: a gap-dependent X_pole favors
  small-gap crystals, so the order is open, not merely unresolved; silicon Migdal rates below about 2 MeV carry the unsized coherent factor of the
  Ch12 erratum (33 % of the rate at 2 MeV, 7 % at 3 MeV). LOOSE-ENDS — sign and size of the coherent factor at 0.75 keV–2q_BZ (likely a
  suppression near threshold); DEFERRED-COMPUTE — the coherent Migdal response between 0.75 keV and 2q_BZ for Si (sizes the 17.1 Migdal band).
