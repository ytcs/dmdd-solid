# Ch20 post-revision check (isolated verifier, 2026-11-06)

Scope: tex/ch20/*.tex, E-12/E-25 edits, Ch20 F rows, figscripts/ch20 logs, rulings R1–R8 (+ addendum). Light Python; nothing edited. Scratch tests sink.py/two.py exec kern20_5.py's solver without writing anything.

## 1. R3 — aluminum constants
- 6.63/3.30 km/s: **CONFIRMED** (my Voigt average: G_V 29.44 GPa, K 79.4 GPa → 6.628/3.302 km/s at 2.70).
  **CONCERN (minor):** 2.70 g/cm³ is the room-temperature density. Ch15 (al_constants.py) pairs the 0 K constants
  with 2.73, which gives 6.59/3.28 km/s. amm20_3.log shows the effect: t̄_esc 0.364, t_l 0.190 ns (+1.6 %).
  This is far inside the AMM/DMM spread. Fix: add one clause in 20.3 ("ρ = 2.70; the 0 K density 2.73 moves t_l by
  +1.6 %") or switch to 2.73. Either way, Ch15's light pass should use the same pairing.
- t̄_esc 0.368 (DMM 0.282), t̄_Si→Al 0.938, t_l 0.187/0.244 ns, t_l/t₀ 0.718/0.937, critical angle 37.67°,
  trapped flux 0.557, lumped factor 2.72 (thin) / 1.82 (60 nm, 𝔩_f = v_s t₀), 𝔩_f/d_f 23.1–8.3 (AMM) to 19.9–5.1
  (DMM) → "5–23": **CONFIRMED**. I recomputed the SH average independently (0.3591 against the log's 0.3592) and
  the trapped share as cos²θ_c × T weight = 0.6266 × 0.8896. Reciprocity and flux closure hold to 1e-11.
- Propagation to 20.3, 20.4 (c_LA 6.63; r = 0.72–0.94), 20.5 (0.938; the r grid), E.25 (37.7°, 56 %, factor
  1.31), the F rows (0.368/0.282, 2.72/1.82, 0.187–0.244 ns, room T as a sensitivity), the summary and the nuisance
  table: **CONFIRMED**, no stale 0.327/3.06/35.2°/0.86–1.08 values outside the room-T sensitivity clauses.

## 2. R1 — 𝔯_coll (central item)
**Numbers against kern20_5.log: CONFIRMED.**
- Thick films over 0.75–4.7 meV: two films 0.911–1.089. At 0.84 meV, over both geometries and both sub-gap fates:
  0.918 (two films) to 1.014 (one film, κ = 1) → 0.92–1.01.
- One Al film with escaped phonons lost, at 0.84 meV: r = 4 gives 1.054–1.103; r = 0.94 gives 1.299–1.417;
  r = 0.72 gives 1.383–1.525. These match the quoted 1.05–1.10 and 1.30–1.53.
- Two films at 60 nm: 1.023–1.162. 20.5 quotes 1.05–1.16, at r = 0.72 only. Both readings are consistent.
- Identity eq:20.5-sign: within 1e-4 for thick films and within 0.010 with escape ("0.011" in the text).
- Near-gap lowering at 0.75 meV to 0.91–0.93 is stated. "Outside every value" is removed.
- The cascade yield replaces the ramp. Escape enters through p_first and Y(W; r) at the 20.3 values of r.

**"Returned = thick film within 0.001": CONFIRMED numerically, but it is not exact.** The reason: once a phonon has
escaped and re-entered, it is statistically identical to a phonon the film had kept, because the cascade is Markov.
Escape plus return is therefore a delayed continuation of the thick-film cascade. Two effects break this, both
small at ℓ_bare = 1e-3: bare-face loss on the return path, and anharmonic decay in the crystal. Raising the loss
breaks the agreement. My sink test (one 60 nm film, shape A, 0.84 meV, returned variant) gives:

returned 0.998 / 1.004 / 1.023 at ℓ_bare 0.01 / 0.03 / 0.3, against a thick-film value of 0.994.

Fix: in 20.5, write "within 0.001 at the bare-face loss of 10⁻³ (exact without loss on the return path)".

**Physical conclusion: CONCERN (substantive). The 1.30–1.53 values are an artifact of an asymmetric assumption.**
- The "lost" variant reflects a phonon that leaves the film unbroken back into the crystal. It deletes the
  phonons that leave after a first pair break. Both kinds cross the same interface into the same crystal, so no
  geometry treats them differently in the mean-field limit.
- The text says the rise "needs a sink … that takes them without signal". That is not sufficient. A sink without
  signal that acts on every crystal phonon (modelled as raised bare loss, which is exactly such a sink) does not
  reproduce the lost-variant rise. With the returned variant, one 60 nm film at 0.84 meV gives:

  ℓ_bare 1e-3 / 0.01 / 0.1 / 0.3 → shape A 0.995 / 0.998 / 1.015 / 1.023, shape B 0.969 / 0.971 / 0.982 / 0.988
  (ε_prim 0.577 / 0.484 / 0.185 / 0.078).

  The lost variant gives 1.53/1.38 at the same point. Even a sink strong enough to destroy the detector
  (ε_prim 0.08) moves 𝔯_coll by ≤ 0.03. The rise needs a *selective* sink: one that removes escaped cascade phonons
  before they reach a film again, but not phonons that have yet to enter one. The mean-field model contains no such
  sink, and the chapter names no physical one.
- Hence 1.05–1.10 / 1.30–1.53 are an upper envelope of the lumped-film assumption, not detector values.
- The hedge "1.128 lies inside this range; transport alone does not exclude collection" is too strong as worded.
  Corrected wording for 20.5 l.80, the summary paragraph, the nuisance row and the F row (and the Ch19 amendment):
  > "In the mean-field estimate 𝔯_coll lies at 0.91–1.09 for thick films (0.92–1.01 at 0.84 meV), and escape
  > leaves this unchanged when escaped phonons return to the crystal, even with a strong sink acting on all
  > phonons. Values up to 1.10 (≈300 nm) and 1.5 (60 nm) arise only if phonons leaving a film after a pair break
  > are removed selectively, as the lumped film assumes. That configuration is an upper envelope, and the estimate
  > does not identify a physical case for it. Collection alone therefore is not reached by this estimate, but it
  > is not excluded until computed kernels (E.25) test real geometries. The two-bias measurement of 19.5 separates
  > collection from stored energy."
- **Two-film model: WRONG (substantive).** kern20_5 deletes the niobium-like film's own relaxation phonons, even
  for thick films (r = ∞; lost variant). These lie below 2Δ_Nb = 3 meV but mostly above 2Δ_Al. In a crystal they
  return and the Al film absorbs them. The returned variant was run for one Al film only. My two-film test
  (two.py; same solver; returned = film20_5 spectrum re-injected for both films):

  | Case | ε_prim | 0.75–4.7 meV | at 0.84 meV | Note |
  |---|---|---|---|---|
  | thick, lost | 0.610 | 0.911–1.088 | | reproduces the log |
  | thick, returned | 0.684 | 0.81–1.005 | 0.82–0.84 | 3.05 meV peak: 1.088 → 1.005 |
  | 60 nm, lost | 0.410 | 0.86–1.21 | 1.06–1.16 | |
  | 60 nm, returned | 0.642 | 0.85–1.00 | 0.85–0.88 | |

  So the two-film 0.91–1.09 rests on a non-physical energy sink. Conserving relaxation phonons gives ≤ 1 everywhere,
  and the full thick band becomes about 0.81–1.02. Fix: rerun kern20_5 with the returned
  variant for both films. Either make it the default, or report both variants and say which is physical. Then
  restate the band in 20.5 (sign subsection, Fig. 20.6 caption/curves), the summary, the nuisance row, the F row,
  and the Ch19 pointer.
- Consequence for R1 as a whole: with every escaped and relaxation phonon conserved and only uniform sinks, no
  mean-field configuration examined reaches 1.099–1.152 (maximum ≈ 1.03). 1.128 needs a selective sink (lumped-film
  assumption). The physics message reverses from "inside the range, not excluded" to "not reached by the estimate;
  not excluded until computed kernels test real geometries; the two-bias measurement decides."

**Operating-point source: WRONG (minor).** 20.5 l.48 says "0.84 meV at 1 V/cm, and 0.75 to 4.7 meV for electrons
over 1 to 100 V/cm" for silicon. In DC-83 (code/DC-83/out/test_luke_ntl.txt), Si electrons give 0.840/1.90/4.62 meV
at 1/10/100 V/cm. The 0.75 is germanium (0.755). Fix: "0.84 to 4.6 meV for silicon electrons over 1–100 V/cm".
Keep 0.75–4.7 as a parametric scan, labelled "including germanium" (same in the kern20_5 docstring). The thick band
"over 0.75–4.7" stays valid as a superset. DC-83 also confirms R4 independently: CMPMC's "ratio to Leman (21)" = M.

## 3. R2 — memory-loss times: CONFIRMED
6.8/47 ns, 0.15/1.0 µs, ~1 µs (22 meV TA) and 13.5 % at 1 µs appear in 20.5, the summary and the nuisance row.
eq:20.5-primary is "≃", "an estimate, not a bound" (0.15 against 0.012), and the summary says "rests on". No "few
percent" remains.

## 4. R4 — Luke rate: CONFIRMED
I re-derived the golden-rule rate: Γ = 2D²m²(k−k_s)³/(3πρ k_s k) = (c/3l₀)(k/k_s)²(1−k_s/k)³. It grows as k², and the
angular law (cosθ−k_s/k)² integrates to it. E.12 eq:E.12-luke now prints this form, with Eq. (8) "lower by k_s/k"
and Eq. (9) integrating to it. The 20.1 clause (Leman Eqs. 21/22, G4CMP Eqs. 8/9) is neutral. charge20_1.log and
the DC-83 CMPMC test both show a ratio of exactly M = k/k_s to the printed Eq. (21). Nit: "the total rates printed
beside it" should read "beside them" (two sources).

## 5. R5/R6 — numbers and citations
- HV 1.72 (mean charge) and 1.36 (binomial): **CONFIRMED** at the logged corner (Y 0.098, F_NR 0.4, f_det 0.873).
  **CONCERN (minor):** the 1σ envelope also varies f_det to 1, and there the binomial value is 1.52, equal to the
  mean-charge value (nothing is trapped). Write "1.36 when the 12.7 % trapped carriers induce nothing (1.52 at full
  collection)" in 20.5 l.143/153, the summary and the table, or say that f_det is held at 0.873 in the binomial
  number.
- Low-bias ceiling 10.8: **CONFIRMED** (10.801 at 1e-3 V, the zero-bias limit 10.802; the maximum sits at the grid
  edge, which is the V→0 limit).
- Film loss: **the reviser is right.** qp20_4.log at t_l/t₀ = 0.5 gives losses of 46.8 % at 13.6Δ and 58.3 % at
  43.8Δ, so 47–58 % over the logged arrival band (13.6–43.8Δ, the middle 80 % of absorbed primary energy,
  kern20_5.log). The ruling's 49–60 % over 16–60Δ came from the 0.7–2.7 THz band, which R6 dropped as unsourced
  (Y(60Δ) = 0.238 gives 59.7 %). 20.4 also states 35–50 % for 60 nm (log 35.1–50.0) and 41 % at 10Δ. Correct.
- About 13 % (1.128): CONFIRMED. 55.6 meV Debye against the 62 meV band top: CONFIRMED (20.2 captions, kern
  docstring). 1.0 µm at 0.95 ns: CONFIRMED in 20.2. Hole Luke mean: the log gives 1.15 meV, the text 1.1. That is
  acceptable, but the ruling's 1.14 does not match the log (no action).
- Contrasts 0.11/0.22/0.43 (log 0.108/0.223/0.430): CONFIRMED. 5.0/4.0 meV and 18 % below 3 meV (log 0.177):
  CONFIRMED.
- Face-sheet bound: CONFIRMED. 20.1 l.140–142 limits 6.3e4 cm⁻² to a vanishing slab. The summary and table give
  ~10⁵ (6.3–12.6e4) over a finite part of the crystal.
- Citations: Leman Sect. III G (20.5, E.25) CONFIRMED. The pair-breaking rate is attributed to Kaplan (20.4 l.28)
  CONFIRMED. ω_opt 64.1/37.6 meV → sec:5.2 and ε_eh → sec:18.2 CONFIRMED. 0.7–2.7 THz is gone, CONFIRMED. The Ge
  constant gives both "Tamura" values (factor 2.6) CONFIRMED.

## 6. R7/R8 — structure and notation
- The verdicts subsection is cut (20.5 has five subsections, ending at 20.5-hv). The 21.7 pointer is in the Summary.
  The soft share points to eq:20.2-fs: **CONFIRMED**.
- t₀ stays the pair-breaking time. 20.5 uses t_rel: **CONFIRMED**. eq:19.5-bimol still uses t₀ (Ch19 rename owed
  by the coordinator, as logged).
- f_LA = 0.093 in Si everywhere (0.098 in Ge; 0.0975 named as the isotropic value): **CONFIRMED**. Nit: phon20_2.log
  still prints "x_L = 0.093" (log label only).
- F_eh convention is stated in 20.1 (l.115) and 20.5 (l.110): CONFIRMED. There is one Al speed set (6.63/3.30):
  CONFIRMED, subject to the ρ remark in §1.

## 7. Summary and nuisance table: CONFIRMED against the sections
All numbers agree with the sections. Two exceptions, inherited from §2 and §5: the 𝔯_coll sentence and the 1.36
qualifier.

## Verdict: REWORK (targeted at R1 only; everything else ACCEPT WITH the minor fixes)
1. R1: rerun kern20_5 with phonons conserved (returned variant for both films; Nb-like relaxation phonons not
   deleted). Restate the band (thick ≈ 0.81–1.02; escape does not raise it without a selective sink; uniform sink
   ≤ 1.03). Reword 20.5 l.76/80, Fig. 20.6, the summary, the nuisance row and the F row as in §2. Give the
   coordinator the corrected Ch19 pointer, not revision.md's "up to 1.5 … not excluded".
2. "Within 0.001": add "at ℓ_bare = 10⁻³; not exact".
3. 20.5 l.48: Si electrons 0.84–4.6 meV over 1–100 V/cm (0.75 is Ge, DC-83).
4. 1.36 binomial: add f_det = 0.873 (1.52 at full collection).
5. Minor: ρ 2.70 against 2.73 (one clause); "beside them"; the x_L label in phon20_2.log.
