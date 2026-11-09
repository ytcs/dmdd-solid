# App. C.10–C.20 acceptance revision (2026-11-07)

Brief: briefs/reviews/appC2-revise.md. Inputs: derivation-1.md (C.10–C.14), derivation-2.md (C.15–C.20), the App. C items of
../appCE/prose.md, editor rulings C1–C5 (editor-notes.md). Files edited: tex/appC/C-10, C-11, C-12, C-13, C-14, C-16, C-17, C-19,
C-20 (C-15 needed no change; C-18 not touched); NOTATION.md (three rows, one scope, clash entry 97). No commit.

## Derivation items

| Item | Status | How |
|---|---|---|
| D1 C.10 l.101 half-line bound (WRONG; ruling C1) | done | Replaced by: the second entry diverges as ξ → 0 and falls only as ξ⁻³ in the tail, so it is weaker than ϱ_MK near the origin and far out; it is tighter only at intermediate ξ, where a node of the canonical representation through ξ lies below zero; for silicon at q = 100 keV at most 6.8 % below ϱ_MK, near ξ = 0.74 E_R (11.5). Now agrees with 11.5 l.91. |
| D1 C.10 gamma example (ruling C1) | done | "58 standard deviations above the mean" for 4.1 % (and 1.3 % at 173); added that at 58σ below the mean the exact value falls 3.9 % short of the tail form. |
| D1 C.12 c_a, c → ξ_a, ξ₁ (WRONG notation; ruling C2) | done | Extremal halo Ξ* = Σξ_aδ_{w_a}, ξ_a > 0; one-bin stream mass ξ₁ = N₁^up/𝗄₁(w_*). Matches 21.2 and D.46. |
| D1 C.12 Rogosinski n + 1 → n (GAP; ruling C3) | done | Rogosinski's theorem applied to the n + 1 functionals 𝗄₁…𝗄_n, 𝖿 gives a measure with the same counts and objective on at most n + 1 points; the finite argument above removes one more. |
| D1 C.14 σ_N → σ_N̂ (WRONG notation; ruling C2) | done | All 15 occurrences (eq:C.14-gauss, the ratio, the one-sided limit, the profiling example, eq:C.14-quadrature). σ_N in Ch. 1, 2, 11, 12, 18 is the nuclear cross-section and stays. |
| D1 E.27 ξ_i clash | flagged | Outside C.12; left to the E.27 owner (noted in entry 97(d)). |
| D1 ϱ_MK first use (ruling C5) | done | NOTATION row: first use "C.10 (also 11.5)". |
| D1/D2 SPINE "Used by" lists | listed below | Coordinator applies at merge (ruling C5). |
| D2 C.16 α_kj (GAP notation; ruling C2) | done | Renamed 𝔞_kj (`\mathfrak{a}_{\vect{k}j}`, 4 occurrences); new NOTATION row after d_kj. No other file used α_kj. |
| D2 C.17 "k = q = 0" (WRONG wording; ruling C3) | done | "At k = 0 and q = G = (2π/a)(0,2,0), so that the reduced final momentum k + q − G is again 0, eq:C.17-selection requires …". |
| D2 C.17 pointer eq:3.1-fG (GAP) | done | Now eq:A.3-periodic (general definition of f_G, same e^{+iG·r} convention as the next sentence). |
| D2 C.19 Berlin et al. conventions (GAP; ruling C3) | done | States all three differences: per formula unit, σ for σ/2, and χ″_ab = 2(1 − e^{−βω})S_ab with π/V where S_ab carries 2π/V [Eq. (B4)], as 14.4 states. |
| D2 C.20 Fitzgerald series (GAP; ruling C3) | done | One sentence after eq:C.20-EPN: the series of [Eq. (5)] is smaller than eq:C.20-PN by a factor 4 and its barrier [Eq. (6)] smaller than eq:C.20-EPN by a factor 2; a direct lattice sum of E(z₀) confirms the forms given here. |
| D2 C.20 cited formula symbols (ruling C3) | done | Qureshi limit now given in book notation, Δ₀²/(2πα_ohmT), and identified to leading order in α_ohm with Δ̃₀²/γ₀ of [Eq. (10)], with γ₀ = 2πα_ohmT and Δ̃₀² = Γ(1−2α_ohm)cos(πα_ohm)Δ₀²(2πT/ω_cut)^{2α_ohm} defined in place (as eq:16.8-qureshi). Checked: the symmetric rate of C.20 at α_ohm → 0 gives Γ_LR + Γ_RL = Δ₀²/(2πα_ohmT). |
| D2 C.20 locals p, s | done (note) | Listed as locals in entry 97(c). |
| d_kink | not touched | App. B reviser's rename; the file already prints d_kink. |

## Prose items (appCE/prose.md, App. C; ruling C4)

| Item | Status | How |
|---|---|---|
| C.10 l.3 "tell us about" | done | "what five moments fix about". |
| C.10 l.92 aphorism | done | Cut; paragraph ends on "five moments leave it undetermined". |
| C.10 l.103 looped close | done | Cut; its one new clause (path-integral simulations give the moments for any anharmonicity) moved into l.3. |
| C.11 duplicate "turn sums into products" | done | Cut from the generating-function paragraph (kept in the opening). |
| C.11 "The lesson for a cascade" | done | "In a cascade, the fixed-point equation … has more solutions than the physical one, and the physical solution is the minimal one …". |
| C.12 l.3 count-teaser | done | "\Cref{sec:21.2} uses three of its properties: …" in one sentence. |
| C.13 l.98 frame + repeat (looped close) | done | Opens with "A tier does not assert …: B does not beat C"; repeated sentence dropped; closing "What tiers never do … this is why" rewritten as cause → consequence. |
| C.14 "where dark-matter limits live" | done | "the regime of dark-matter limits". |
| C.14 "One draws" | done | "We draw …, evaluate …, and read off …". |
| C.17 long sentences (optional) | left | Both are lint artefacts of a display joined to the next sentence; no change. |
| C.19 run-together cites | done | "\cite[Chap.~7]{squires…}, \cite{lovesey…}". |
| C.19 citation as subject | done | "the combination that Berlin et al.\ extract from neutron data~\cite[Eq.~(26)]{…}". |
| C.19 vague close | done | "A dark-matter response that needs S_xx, such as the contact spin coupling or the absorption of an axion-like particle, therefore cannot be taken from neutron data alone; 14.4 bounds it by positivity and fixes it under spin isotropy." |
| C.20 "decides the physics" | done | "Its power law at low ω fixes the long-time decay of the bath correlation, eq:C.20-Q below." |
| C.20 "Two effects compete." | done | "Cooling shrinks the dressed amplitude and lengthens the dephasing time." |
| C.20 Qureshi notation | done | See D2 above. |

## Checks
- Lint (lint.py --banned BANNED-TERMS.txt), C-10 … C-17, C-19, C-20: 0 blocking; remaining LONG-SENT advisories as before
  (C-16 1, C-17 2, C-20 1), none introduced.
- check_notation.py --files on the revised files: no new gap from 𝔞_kj, σ_N̂, ξ_a, ξ₁, γ₀, Δ̃₀ (pre-existing file-local gaps unchanged).
- Renames grepped in tex/ch*, tex/app* and figscripts: no other file printed c_a (stream mass), σ_N (width of N̂) or α_kj.
  App. B (B-1.tex, generated by figscripts/appB/gen_B1.py) already prints σ_N̂; the new 𝔞_kj row reaches B-1 at its next regeneration
  (App. B reviser).
- Build: latexmk -pdf main.tex, -outdir=/tmp/claude-0/build-appC2: 0 errors, 0 undefined references or citations, 1840 pages
  (the first run hit latexmk's pass limit because parallel App. E edits changed inputs mid-build; the rerun converged).

## SPINE "Used by" additions (for the coordinator)
- C.10: add 11.9 (→ 11.5, 11.9).
- C.11: add 18.3, 20.1, D.43, D.44 (→ 18.1, 18.2, 18.3, 20.1, D.43, D.44).
- C.12: add D.46, E.27 (→ 21.2, D.46, E.27).
- C.13: unchanged (17.6).
- C.14: add 10.10, 11.9, 17.2, D.47 (→ 8.8, 10.10, 11.9, 14.6, 17.2, 17.6, 19.4, 21.4, 21.5, D.47).
- C.15: add 3.5, 7.3, 8.1, D.24, D.34 (→ 3.5, 7.3, 8.1, 10.6, 10.9, 12.5, D.24, D.34).
- C.16: unchanged (12.6).
- C.17: add 3.1, 3.2, 3.4, 10.5, 13.3, C.18 (→ 3.1, 3.2, 3.4, 10.5, 13.3, 13.9, 14.5, C.18).
- C.19: add 7.1, 14.1, 14.3 (→ 7.1, 14.1, 14.3, 14.4).
- C.20: add 16.7, D.42, E.22 (→ 16.7, 16.8, 19.6, D.42, E.22).
