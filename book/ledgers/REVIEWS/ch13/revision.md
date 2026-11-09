# Ch13 revision (2026-11-06): item → done / how

Files touched: tex/ch13/ch13.tex, s13-1 … s13-9; tex/appD/D-35, D-36, D-37; tex/appF/F-rows.tex (Ch13 rows); tex/appE/E-14 (l.13, l.62),
E-15 (l.35), E-16 (l.19); tex/ch06/s6-5.tex and tex/ch10/s10-7.tex (cold excitonic edge only, R5); NOTATION.md (Ch13 rows, entry 84).
Scripts (figscripts/ch13): NEW interim13.py (+ .log); edited onset13_1.py, fig13_3.py, fig13_4.py, fig13_6.py, fig13_7.py, we13_2.py,
we13_4.py, we13_6.py, map13.py; all light scripts rerun, logs regenerated (fig13_1/3 and onset13_1 logs written from stdout). No QE.
Build: see the end of this file.

## R2 first: the screening correction (formerly the "interim factor [0.4, 1.8]")
Redefined as the correction relative to the rate normalized to the measured optical edge, whose ε₂ contains the pair channel and the
local-field wings at q → 0; the external factor is not in ε₂ and is calibrated at q → 0 only by pinning ε₁^model (F2). interim13.py states every input (I1–I8) and assumption (A1–A4).
- K_ext = (ε_model/ε₁⁰)²: the estimate's Cappellini ε₁ against the true macroscopic ε₁⁰, taken between the RPA ε_mac (Knapen/DarkELF)
  and that value × 1.294 (RPA deficit at q → 0, 1.20 eV). Window momenta 0.94–1.27 keV, ω 1.184–1.47 eV: **0.60–1.45**
  (0.73–1.43 at 1 keV). The macroscopic local fields (+25–31 %) are inside it.
- K_wing (A2: wings ≤ head→mac change of 1/ε₁², either sign, independent at q and 0): **0.55–1.77**.
- K_pair: **1 to 4×10⁻⁴ (applied-potential limit; pinned pair momentum) and to 4×10⁻³ (rigid limit)**; between the limits not derived
  (if only bracketed by the limits: 0.068–14.8 with max ε₁ = 3.84 — 14.7 in the post-revision check, rounding; printed, not adopted; F4).
- **Result: sized correction K_ext·K_wing = 0.33–2.56, quoted 0.3–2.6 (estimate); the pair-channel q-dependence beyond the optical
  calibration is an unsized nuisance.** Adopted in 13.4 (closing paragraph), 13.9 (text, Table 13.1 new row, nuisance row), E.14 l.13,
  E.16 l.19. Error budget rebuilt: form factor ×3, screening ×2.8, cold-data spread ×2.8 (0.38 MeV) → ×1.4 (0.43 MeV), threshold ×1.5
  → combined ×6.5 at 0.38–0.43 MeV, rounded to ×10 (old budget ×4). The old [0.4,1.8] arithmetic is reproduced in the log.

## Rulings
| R | done / how |
|---|---|
| R1 | Summary: 1/30–1/38 (macroscopic). |
| R2 | above. |
| R3 | GaAs 1.71 eV sentence deleted (13.9); vurgaftman cite no longer used in Ch13. |
| R4 | WE 13.2 states twist 0.3 rad (0.05 rad per k; gap 1.442 → 1.448 eV) and the vertex phase convention (cell origin); other convention (orbital, Q = −q): |M| = 0.107, factor 1.6 (we13_2.log). 13.2 text, 13.8 quote and nuisance row name it. |
| R5 | 13.9 primary input = Stanford et al. 0.5 K fit (21.5 cm⁻¹, ε₂ 1.2e-3 at 1.25 eV); Macfarlane 20 K as spread (10.4 cm⁻¹, ε₂ 5.9e-4; ×20 at 1.20 eV; within 5 % above 1.37 eV). Rate model of the estimate rerun with both (reproduces published values with M): σ̄_e heavy 3e-30 (0.36), 4e-32 (0.40); light 1.4e-32, 2e-34; ZP/PA ratios change ≤5 % (lead masses unchanged). New nuisance row; 13.8 WE quotes the 20 K value (0.21 cm⁻¹, ×20). Cold excitonic edge aligned book-wide to 1.1728 eV with E_g(0) = 1.1692 eV: 13.8 opener (reconciliation cut), 6.5 WE (last sentence; the four-number excitonic list replaced by "down by E_x^b"), 10.7 caption. |
| R6 | Removed "interim", "computed once", "has not been run/done", "derived here", "to our knowledge", "tested once", "made once" (13.1–13.9, F rows). Table 13.1 labels: two independent calculations / symmetry, confirmed numerically / derivation / one calculation / measured data / estimate / open; headers Established / Estimated or open. 13.7: rebuttal of the 0.12 eV estimate deleted; 8 meV stated positively. |
| R7 | 6.1 meV VBM (40.9 → 34.8), 1.9 meV CBM (23.3 → 21.4), Γ_c range −21.4 to −7.4 meV; fig13_7.py fixed and rerun; F row updated. |
| R8 | Table: second heavy hole "0.415: two independent calculations; 0.420: estimate". GaAs row unchanged (0.43 → 0.52–0.56). |
| R9 | 1.33 keV (parabolic) / 1.27 keV (computed bands) labelled in 13.3, 13.6 (twice), F row, Summary; δ_w defined at first use in 13.3 with \cref to 13.6; two-branch vs TA-only labels in 13.5 box and 13.8; "halves |M|²" → emission Q > 0, ×2.9 for the other sign. |
| R10 | E.14 l.62 (Ge heavy hole less warped; nothing transfers); E.15 l.35 (one pair per intermediate state; two-pair states via the interaction beyond Tamm–Dancoff). |

## derivation-1.md
| item | done / how |
|---|---|
| D.35 diagonal-term denominator | now E₀ − E_m ∓ ω_Q with E_m = E_f ∓ ω_Q, = −ω. |
| 0.62 → 0.61 keV | printed 0.615 keV (log 615 eV), 1.94 − 0.615 = 1.33. |
| 44.3 → 44.1 meV | Nelder–Mead refinement added to fig13_3.py (44.14). |
| "4 to 5 %" | 4.2/4.8 % (head), 3.7/4.4 % (macroscopic); nuisance row 3.7–4.8 %. |
| GaAs 10.5 meV computed | labelled computed (upper value). |
| Giustino/Noffsinger citation | reworded: combined two-term form. |
| SOC < 1e-4 | stated as an estimate from the ZP spin–orbit lift on the same axis (3.6e-6 vs 0.150). |
| (2̄00) glide | confirmed by derivation-2; no change. |
| 1.33 label | R9. |
| rigid-limit 2e-3 wording | 13.4: strict limit ω_f = ω; 1e-3/2e-3 at the window TA energy; WE wording. |
| DarkELF data citation | knapen2022darkelf added (13.4 WE). |
| l.150 vs 13.9 | aligned (13.4 closing paragraph rewritten; 13.9 states ε₁ model and that the macroscopic LF are inside K_ext). |
| S5 | R2. Double counting: the old "factor two from screening" was the same item; now one budget entry. |
| NOTATION (M^±, ς, W^scr,R, ω_TA(Q*), L^PA screened, δ_LF/δ_pair) | see NOTATION below. |

## derivation-2.md
| item | done / how |
|---|---|
| 8 meV split, Γ_c range | R7. |
| 77 K ZP shift −0.0007; 300 K ZP 0.3966–0.3995 (best 0.3985) | fixed (WE 13-windowT). |
| 13.8 l.69 spurious N⁻¹ | chain corrected. |
| glide parities | confirmed; nothing to change in text. |
| medge halo assumption | keyresult and text state the standard halo of tab:1-shm (quadratic η at v_max). |
| Table second hole status; GaAs vs SOTA | R8; ledger list below. |
| 1.71 eV | R3. |
| 13.5: Eq.(1) is α; 2.45 eV at 300 K; 0.61/0.88 gap law; "two-branch" 300 K | all fixed. |
| D-37 Galilean "antisymmetric" | rewritten: v^g⊗p = p⊗p/m_e symmetric for local potential; nonsymmetric only via V_NL. |
| D-37 Qmin "for emission" | emission gives δ_w/(v−c); printed bound is absorption's and holds for either sign. |
| 13.6 velocity/deformation 1e-5 | "a few times 1e-3 per band (1e-5 after e–h cancellation)"; we13_6.py prints 5.6e-3, 3.1e-3. |
| halves |M|² | R9; we13_6.py prints 0.500 / 2.912. |
| 1.77 eV "along the valley axis" | 13.6 l.3, 13.3 l.3; 13.7 "narrower off the axis". |
| Γ̂ definition | 13.6 keyresult (edge to δ_w above), numbers 3–21 meV at edge, 15 meV 0.3 eV above at 1 keV; NOTATION row. |
| δ_w = 0.1/0.5 eV ratios | 0.64, 0.56–0.73; 0.13, 0.11–0.15 (fig13_6.log). |
| 13.7 f-sum one-phonon zero-pair sector | stated, Z_v m_e/M_cell = 8e-5 (fig13_7.log). |
| z_qp | 13.7 renamed. |
| 13.8 vs 13.9 cold data | R5. |
| 13.9: fifteen times; 18 of 21; E-17 label; 10.4 cm⁻¹; "two orders" | fixed (new numbers: two orders with the 0.5 K fit, 2.6 with the 20 K data). |
| C: E_g(0), Γ̂, η, ς, ŝ_Q, F(q), unregistered symbols | NOTATION; R5 alignment. |
| D: ledgers behind the book | listed below. |

## prose.md
All items applied: O-1…O-5; 1-1…1-8 (1-4: subsection paragraph cut to two sentences; 1-5 \cites in 13.1, 13.2, 13.7 ×3; 1-6 Ge paragraph split in three);
2-1…2-9 (preview paragraph → one "we will" sentence; computational passage cut; paragraph breaks); 3-1…3-9; 4-1…4-10 (4-5 "applied-potential
limit", also in we13_4.py/log; 4-6 display already punctuated); 5-1…5-9 (5-1: L^PA_IP in 13.5; 5-2 band in the box); 6-1…6-10 (title
"The off-shell window"); 7-1…7-9; 8-1…8-8 (title "Exciton replicas and bosonic absorption"); 9-1…9-13; S-1…S-5; D35-1/2, D36-1, D37-1…4
(D.37 "check in one dimension" subsection replaced by one sentence; WE 13-soft now reports the Q = −0.25 absorption check too). Redundancies
(a)–(e) cut where flagged; seams 13.3→13.4 and 13.5→13.6 bridged; connectives ("however", "we will", "note that", "since") added in each section.
Not done: Macfarlane table locators (closed access; locator not checkable).

## reader-a.md / reader-b.md
All flagged items fixed: Summary factor; "binding"→"tighter bound"; halves |M|²; D.37-Qmin label; 300 K factors two-branch; ε₂ = 5.9e-4
with 10.4 cm⁻¹; α_abs named in WE 13-darkphoton-edge; LA Δ₁ sentence; nonsymmorphic phases cancel (pointer to WE 13-glide); twist and
vertex convention (b2); δ_w defined before the boxed result; D∓cp vs D+vp reconciled in 13.6; θ_ep paragraph made explicit (0.7×0.3/1);
"16, 7.3" two-branch; halo-edge assumption; 1.33/1.27; SOC/PT reality ((PT)² = +1 on even-N many-electron states); ZG "same coupling"
softened; "about 60 meV" → 56 / 71–73 meV; bound-pair q* convention (both passes 2E/v_max; direct minimization 0.885/0.896 keV); RPA
deficit attributed to the missing electron–hole attraction; x and ς clashes resolved. Not done: a C_4v character table (reader-b
should-fix 12) — the cited Yu–Cardona chapter carries it; App. C has no compatibility table to point to.

## NOTATION (brief list: M^±, ς, x, s_Q, η, F(q), Γ̂, z_qp, W^{scr,R}, ω_TA(Q*))
M^± row widened (two- and three-argument forms); ς → 𝔰^(2) (13.4, D.36); x, y → 𝗑, 𝗒 (13.4, 13.8, D.35, D.36); ŝ_Q, s_mn → 𝔱̂_𝐐, 𝔱_mn
(13.6, D.37); η → η(v_min), A → A_η, glide-η row widened to 13.9; F(q), F₀ → x_max(q), x*_max; Γ̂ row widened; z_nk → z_qp(n, k);
W^scr → W^scr,R in 13.4 keyresult, D.36, Fig. 13.4 (fig13_4.py); ω_TA(Q*) in 13.1/13.3/13.4 WEs. ~45 rows added after the δ_w row;
clash entry 84. check_notation.py on ch13 + D.35–D.37: 0 gaps.

## Changes the campaign ledgers need (not edited here)
- state/CORRECTIONS.md: (i) l.82 "interim factor [0.5, 1.2] stands" → superseded; the campaign value [0.4, 1.8] (WP3-v3 C28) is itself
  superseded in the book by the screening correction relative to the optical calibration, 0.3–2.6 for the external factor and the
  local-field wings (estimate, interim13.log) with the pair channel's q-dependence unsized. (ii) Rate-estimate normalization: the book's
  primary cold edge is now the Stanford et al. 0.5 K fit; σ̄_e (3 events, 1 kg yr) 3e-30 (0.36 MeV) and 4e-32 cm² (0.40) heavy, 1.4e-32 and
  2e-34 light (COMP-PAER values with Macfarlane 20 K: 3.1e-29, 7e-32, 1.3e-31, 3.9e-34 — the spread, ×9 at 0.36 MeV); combined budget ×6.5
  quoted as ×10. (iii) Nonadiabatic ZPR split 6.1 meV VBM / 1.9 meV CBM (not 6.0/2.1); CW1 "≲ 2 meV" superseded by 8 meV (l.617 already).
  (iv) GaAs window 0.43 → 0.52–0.56 MeV (E_L(0) = 1.815 eV) supersedes 0.43–0.51 [E, parabolic] of §580. (v) l.314/l.335 "allowed ZPL from
  0.547 MeV" superseded (by l.575). (vi) Cold excitonic edge 1.1728 eV with E_g(0) = 1.1692 eV book-wide (1.1736 retired).
- state/SOTA.md: l.65 interim factor entry → screening correction 0.3–2.6 + unsized pair-channel q-dependence; GaAs R17 row 0.43 → 0.52–0.56;
  rate-estimate reach values as in CORRECTIONS (ii).
- state/LOOSE-ENDS.md: LE-178 "≲ 2 meV" → 8 meV (Poncé Table VI; 6.1 VBM + 1.9 CBM). New loose end: pair-channel ratio at finite q vs
  q → 0 (between the solvable limits) unsized — supercell route E.16. New: cold Si absorption within 25 meV of threshold at mK (0.5 K fit
  vs 20 K data differ ×20 at 1.20 eV, ×2 at 1.25 eV).
- state/NOVELTY.md N7: prior art credited (Mitridate et al. 2106.12586 Sect. V Eq. (72), intraband phonon-assisted kinetic absorption in a
  superconductor); claim narrowed to the interband edge of an insulator; the book no longer prints any novelty claim (all "derived here"/
  "to our knowledge" sentences removed per R6) — record that the claim lives only in the ledger.
- CONTROLS.md C8: GaAs control band 0.43 → 0.52–0.56 MeV (E_L(0) = 1.815 eV; L floor 0.517, edge ≤ 0.560); no calculation of the control yet.
- Also for the coordinator (outside this brief's file scope): SPINE 13.7 LO(iii) and limits row CW1-L9 → 8 meV; SPINE "GaAs Fano map in
  E.26" → E.14; 8.5 light pass (θ_ep = 1 at 0.25 eV is a bound, matching 13.6); 8.8 pair-channel pointer → E.16 and the 13.9 screening
  correction; E.17 l.13 deformation tensors → 13.6/D.37; s10-8 caption and figscripts/ch10/abs10_7.py, pair10_8.py still print 1.1736 eV
  (align to 1.1728 with E_g(0) = 1.1692); D.37 strain tensor S_αβ → u_αβ at the next notation pass (editor ruling).

## Build and checks
`latexmk -pdf -outdir=/tmp/claude-0/build-ch13rev main.tex` (full book): 0 LaTeX errors, 0 undefined citations. Undefined references
only to unwritten parts (Chaps. 14–22, sec:9.x, app:B.2, app:D.47). Display overfulls in eq:13.6-soft and eq:D.37-limit removed (split);
no overfull box left in the Ch13, D.35–D.37, 6.5, 10.7 or F-row displays (the two remaining log hits near D.37 and E.14 are
bibliography lines). lint.py: 0 blocking hits in ch13/*.tex and D-35–37 (TITLE hits of 13.6 and D.37 gone; D.36 periphrasis fixed).
check_notation.py on ch13 + D.35–D.37: 0 gaps. map13.py rerun (node "Exciton replicas", W^scr,R).

## Post-revision fixes (postrev-check.md, ACCEPT WITH FIXES)
| F | done / how |
|---|---|
| F1 | 13.9: the 0.36 MeV reach is quoted as the dataset band 3e-30–3e-29 cm² (heavy), 1.4e-32–1.3e-31 (light); 0.40 MeV keeps 4e-32 / 2e-34 with ×10. Budget sentence: ×15 at 0.36 MeV (data spread ×9.2), ×6.5 → 10 at 0.38–0.43. New sentence: 55 % of the 0.5 K-fit rate at 0.36 MeV is below 1.206 eV (Stanford's lowest diode), where the fit is an extrapolation with E_g1 floated to 1.134 eV, TA threshold 21 meV below the cold edge; the 20 K curve below 1.212 eV is the estimate's ramp, not data. Table 13.1 row and the nuisance row carry it ("factor 10 at 0.40; 15 at 0.36"). interim13.py logs the shares (55/20/10 % at 0.36/0.38/0.40), the variants (7.0e-30 fit-above-diode + ramp; 3.5e-30 clamped at 1.1728 eV), the band and ×15.1. |
| F2 | 13.4 (optical-limit paragraph), 13.5 (l.48), 13.9 (screening paragraph), interim13.py docstring, this file: ε₂ contains the wings and pair channel; the external factor is calibrated only through ε₁^model at q → 0. 13.9 also states "independently at q and at q → 0" for the wings. |
| F3 | 13.4 closing paragraph, 13.9 screening paragraph, nuisance row: pair ratio = 1 to 4e-3 only at exact pinning; the ~0.2 keV spread of pair momenta above the onset (ε₁ 4.5 → 3.3 between 1.61 and 1.97 keV, logged) leaves an unsized residual. |
| F4 | interim13.py uses max ε₁: bracket 0.068–14.8 (log); this file corrected. |

Leftovers cleared: s10-8 caption and s10-7 l.44 (a second 1.1736 I had missed) → 1.1728 eV with E_g(0) = 1.1692 eV; figscripts/ch10/abs10_7.py and pair10_8.py edited and rerun (logs abs10_7.log, pair10_8.log written); no "1.1736" left in tex. F-rows l.210 (Ch11) "derived here" → "is \cref{eq:11.2-Ipol}"; also l.162 (Ch10) "is derived here" → "follows from the derivation of \cref{sec:10.9}". E.17 l.13 already points to 13.6/D.37 (no edit needed). D.37 strain tensor S_αβ → u_αβ (NOTATION entry 84 updated). 8.5 and 8.8: both named fixes are already in the text (8.5 l.14 "Its edge is not where θ_ep reaches one … 0.3 eV … bounds"; 8.8 l.22 points to App. E.16); no edit. Remaining status wording in 8.8 l.22 ("has not been done") is outside the named edit.

Rebuild: 0 LaTeX errors, 0 undefined citations (undefined references only to unwritten parts).

## SPINE fixes for the coordinator (line → new text)
- l.2165: `### 13.6 Soft phonons, resonances and the off-shell window` → `### 13.6 The off-shell window` (section retitled).
- l.2202: `### 13.8 Excitons with phonons and phonon-assisted absorption` → `### 13.8 Exciton replicas and bosonic absorption`.
- l.2229: "on rates known only to a factor of ten" → "on rates known only to a factor of ten (fifteen at 0.36 MeV, where the reach is the band 3e-30–3e-29 cm² between the 0.5 K fit and the 20 K data)".
- l.2246: "computed once and not\n  verified [CL]" → "resting on one set of force constants [CL]".
- l.2250: "computed once\n  with the nonlocal and truncation parts not separated" → "with the nonlocal and truncation parts not separated".
- l.2252: "route-S local-field numerics that narrow the interim factor [0.4, 1.8] (LE-41; App. E.16)" → "the screening correction relative to the optical calibration, 0.3–2.6 for the external factor and local-field wings [EST], with the pair channel's q-dependence beyond the calibration (and the residual from the spread of pair momenta) unsized; route-S supercell numerics would size it (LE-41; App. E.16)".
- l.2252–2253: "phonon-assisted-leading only at ≈ 0.43–0.51 MeV in a parabolic estimate [EST]" → "phonon-assisted band 0.43 to 0.52–0.56 MeV (E_L(0) = 1.815 eV) in the parabolic description [EST]".
- Already correct, no change: l.2189 (13.7 LO(iii), 8 meV), l.3698 (CW1-L9, 8 meV), l.2177 (GaAs Fano map in E.14, not E.26).
