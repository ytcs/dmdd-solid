# LAUNCHES

## R1 (2026-10-31)
| ID | Role | Brief | Return |
|---|---|---|---|
| D1 | derivation, golden-rule route | briefs/R1/D1.md | returns/R1/D1.md |
| D2 | derivation, Kubo/diagram route (independent) | briefs/R1/D2.md | returns/R1/D2.md |
| L1 | literature priority + lemma map | briefs/R1/L1.md | literature/L1.md |
| N1 | numerics: window, data-calibrated reach, pyscf C6 check | briefs/R1/N1.md | returns/R1/N1.md |
| N1 | STOPPED by user directive (2026-10-31: "hold off all numerical work; build the theory that drives it") | | partial outputs, if any, not used |

## R1b (2026-10-31, user request: catalog the full process space)
| ID | Role | Brief | Return |
|---|---|---|---|
| CAT-A | catalog of DM–solid-state processes | briefs/R1b/CAT-A.md | literature/CATALOG-A.md |
| CAT-B | experimental-analysis impact + theory gaps | briefs/R1b/CAT-B.md | literature/CATALOG-B.md |

## R2 (2026-10-31): hostile referees on D1 + D2 (rung 4). The independent re-derivation (rung 5) is satisfied by D1 ⟂ D2.
| ID | Role | Brief | Return |
|---|---|---|---|
| REF-A | hostile referee, isolated | briefs/R2/REF-A.md | referees/R2/REF-A.md |
| REF-B | hostile referee, isolated | briefs/R2/REF-B.md | referees/R2/REF-B.md |

## R3 (2026-10-31): open items from R2
| ID | Role | Brief | Return |
|---|---|---|---|
| X1 | soft-acoustic Q→0 structure, IR behaviour, replacement C7 | briefs/R3/X1.md | returns/R3/X1.md |
| X2 | full screening incl. pair-momentum Coulomb lines | briefs/R3/X2.md | returns/R3/X2.md |

## R4 (2026-10-31): scope v2, URF architecture
| ID | Role | Brief | Return |
|---|---|---|---|
| WP0 | URF architecture: master formula, exact relations, screening, expansion hierarchy, decomposition theorem | briefs/R4/WP0.md | returns/R4/WP0.md |

## R5 (2026-10-31): sector work packages WP1–WP6 launched in parallel; briefs/R5/WP{1..6}.md → returns/R5/WP{1..6}.md
| O4 | convention independence of X0/X+ split (Theorem D iv′/iv″) | briefs/R5/O4.md | returns/R5/O4.md |
| NOTATION-APPLY | campaign-wide conventions + symbol table + corrections index (queued until WP1–4 and O4 return) | briefs/R5/NOTATION-APPLY.md | CONVENTIONS.md, NOTATION.md v3, state/CORRECTIONS.md |

## R6-aborted (2026-10-31): 14 referees launched and then STOPPED within minutes by user directive ("once all packages return, do a full second pass to resolve all corrections and inconsistency before hostile review"). Their briefs are kept in briefs/R7-superseded/ and will be regenerated against the v2 returns. NOTATION-APPLY continues
| Package | Referees | Return |
|---|---|---|
| WP0 + O4 | REF-WP0-A/B | referees/R6/REF-WP0-{A,B}.md |
| WP1 | REF-WP1-A/B | … |
| WP2 | REF-WP2-A/B | … |
| WP3 + X1 + X2 | REF-WP3-A/B | … |
| WP4 | REF-WP4-A/B | … |
| WP5 | REF-WP5-A/B | … |
| WP6 | REF-WP6-A/B | … |
| NOTATION-APPLY | — | CONVENTIONS.md, NOTATION.md v3, state/CORRECTIONS.md |

## Revised plan (user directive, 2026-10-31)
1. NOTATION-APPLY (running): CONVENTIONS.md, NOTATION.md v3, state/CORRECTIONS.md, cross-return audit.
2. R6 SECOND PASS, revision:
   - REV-WP0 first: WP0-v2, absorbing every WP0 defect reported by WP1–WP6, O4, X1 and X2.
   - Then REV-WP1..WP6 in parallel, each against WP0-v2. WP3-v2 absorbs X1, X2 and O4 into the consolidated M1 theory.
   - Each produces returns/R6/<WP>-v2.md: standalone, corrected, in CONVENTIONS/NOTATION v3, with all owed corrections applied. The v1 returns stay untouched as the record.
3. R6 CONSISTENCY AUDIT: one agent reads all v2s and checks the cross-package interfaces, formulas, LIMITS statuses and symbols. Defects go back to the owning REV agent until clean.
4. R7 HOSTILE REVIEW: two isolated referees per v2 package.
5. Synthesis: the framework paper plus the M1 paper.

## R6 second pass (done): REV-WP0..WP6 → returns/R6/*-v2.md; AUDIT → returns/R6/AUDIT.md; audit fixes; RENAME-APPLY (NOTATION v4).
## R7 (2026-10-31): hostile review, 2 isolated referees per v2 package; briefs/R7/REF-<WP>-{A,B}.md → referees/R7/

## R8 (2026-10-31): correction round after R7. REV3-<WP> → returns/R8/<WP>-v3.md. WP0, WP1, WP2, WP4, WP5 in parallel; WP3 and WP6 after WP1/WP3 respectively (they read the predecessors' v3 if present). Then AUDIT-2 and an R8 targeted verification (1 referee per package, on the changed items only).

## R10 (2026-11-01): WP7 follow-up package
| ID | Scope | Brief | Return |
|---|---|---|---|
| WP7-B1 | electronic, low-dimensional and molecular channels from the master-formula-only class | briefs/R10/WP7-B1.md | returns/R10/WP7-B1.md |
| WP7-B2 | lattice, spin, amorphous, defect and Migdal-absorption channels from that class | briefs/R10/WP7-B2.md | returns/R10/WP7-B2.md |
| WP7-D | coherent classical-field regime, fermionic absorption, two-insertion processes; out-of-scope reasons | briefs/R10/WP7-D.md | returns/R10/WP7-D.md |
| WP7-T | low-T defect quantum kinetics (crowdions, defectons, TLS) | briefs/R10/WP7-T.md | returns/R10/WP7-T.md |
| WP7-E | energy-partition reconciliation (after WP7-T) | (queued) | |

## R13 (2026-11-01): WP5 erratum + WP8 — paused, then RESUMED 2026-11-01 (user): WP8-U, WP8-R launched; WP7-E merge done; WP5-ERR and WP8-F launched after the merge commit
| ID | Scope | Brief | Return |
|---|---|---|---|
| WP5-ERR | apply the WP7-E amendment A-1..A-16 → WP5-v4 | briefs/R13/WP5-ERR.md | returns/R13/WP5-v4.md |
| WP8-F | figures of merit per channel class | briefs/R13/WP8-F.md | returns/R13/WP8-F.md (launch after WP7 LIMITS merge) |
| WP8-U | pickable universe + property table (open data) | briefs/R13/WP8-U.md | returns/R13/WP8-U.md, WP8-U-table.csv |
| WP8-R | mode-selective phonon collection NR/ER go/no-go | briefs/R13/WP8-R.md | returns/R13/WP8-R.md |
| WP8-S | ranking synthesis (after F, U) | (queued) | |
| WP5-AUD | joint WP5-v4 + WP7-E audit and R×2 referees (FRAMEWORK WP7-E output); scope includes the yield-dependent sites of WP8-R and WP8-F, which are PROVISIONAL until it clears | (queued after WP5-ERR) | |
| REF-WP8 | 2 isolated referees each for WP8-U, WP8-R, WP8-F before WP8-S; plus a WP8-U top-up for any WP8-F property column missing from WP8-U-table.csv | (queued) | |
- R13 returns in (2026-11-01): WP5-v4, WP8-U (+ table), WP8-F, WP8-R. Next: WP5-AUD, REF-WP8 + WP8-U top-up, NOTATION-APPLY (R13), WP8-S.

## R14 (2026-11-01): audit, WP8 referees, gaps — wave 1 launched
| ID | Scope | Brief | Return |
|---|---|---|---|
| WP5-AUD | joint WP5-v4 + WP7-E audit; IF-R13-2/3/5; G-R3/G-R4 spec text; WP8-R/F yield sites | briefs/R14/WP5-AUD.md | returns/R14/WP5-AUD.md |
| WP8-U-TOP | WP8-F §5 property list; measured ε_eh/F_eh (radiation-detector literature); n_e and c_LA source disputes; G-R5 moduli; magnets/oxides | briefs/R14/WP8-U-TOP.md | returns/R14/WP8-U-top.md, WP8-U-table-v2.csv |
| GAP-EF | ε_eh, F_eh theory (residual anticorrelation term), validation, predictions; WP7-E IF-E9; ab initio computation spec | briefs/R14/GAP-EF.md | returns/R14/GAP-EF.md |
| REF-WP8-{U,R,F}-{A,B} | 6 isolated hostile referees on the R13 WP8 returns | briefs/R14/REF-*.md | referees/R14/ |
| wave 2 (queued) | GAP-FOM (G-F1 scalar-absorption FOM, G-F4 magnon nuisance row); GAP-LEE (G-F3/G-E2/G-R2 predictive LEE and zero-field gap-energy release), after WP5-AUD; R×2 on WP5-AUD; NOTATION-APPLY (R13: IF-R13-1, IF-R13-7, θ_X → θ_exc, check IF-R8-7/8) | | |
| blocked by the numerics hold | G-F2 (multiphonon anharmonic spread), G-F5 (PAER window ab initio), G-R1 (phonon transport for ζ_O, σ_pos, r), IF-R8-10 (GaAs Γ/δ map), ab initio ε_eh/F_eh | specs exist | |

## R15 (2026-11-01): first in-box ab initio computations (user directive; code/ENV.md, run-heavy.sh lock, ≤ 3 h / ≤ 12 GB per job, else formulated)
| ID | Scope | Brief | Return |
|---|---|---|---|
| COMP-PH | Si, Ge bands/phonons vs neutron controls; G-F5 PAER-window inputs; Γ DFPT dielectrics for small-cell survivors | briefs/R15/COMP-PH.md | returns/R15/COMP-PH.md, code/COMP-PH/properties.csv |
| COMP-PAER | Si PAER window, rate, reach (M1 tier B); tier H if the gate passes, else formulated | briefs/R15/COMP-PAER.md | returns/R15/COMP-PAER.md |
| later compute (queued) | GaAs Γ/δ map (IF-R8-10); third-order force constants for G-F2 if phono3py installs; ε_eh/F_eh cascade after GAP-EF's spec; G-R1 phonon transport formulated only | | |
| CMPMC-AUD | audit of the CMPMC (G4CMP port) models, constants and shortcuts against WP2/WP5/WP7-E/WP7-T/WP8-R and the literature; tests; patches; usage verdict per module (gate for every CMPMC number) | briefs/R15/CMPMC-AUD.md | returns/R15/CMPMC-AUD.md |

## R16 (2026-11-01): loose-ends closure (state/LOOSE-ENDS.md, 179 rows; user: close all loose ends before writing)
| ID | Scope | Brief | Status |
|---|---|---|---|
| CW2, CW3, CW4 | lattice/Migdal; architecture/O4/WP7-D; spin/SC/Dirac/low-dim | briefs/R16/CW{2,3,4}.md | launched |
| CW1 | electronic/excitons/M1 window | briefs/R16/CW1.md | after COMP-PH, COMP-PAER |
| CW6 | transport + WP8-R-v2 | briefs/R16/CW6.md | after CMPMC-AUD |
| CW7 | uncertainty/FOM + WP8-U-v2, WP8-F-v2 | briefs/R16/CW7.md | after GAP-EF |
| CW5 | defects/TLS/cascade/LEE (+GAP-LEE) | briefs/R16/CW5.md | after REF-WP5-AUD-A/B, GAP-EF |
| CW8 | literature/novelty, coordinator bookkeeping, SPINE/DONE readiness | (coordinator, last) | |
- R14 GAP-EF returned (19/19); REF-GAP-EF-A/B launched. R16 CW5, CW7 launched (inputs complete).
- R16 returns in: CW3 (24 rows, 28/28), CW4 (21, 18/18), CW5 (26 + GAP-LEE, 21/21). VER-CW3/4/5 launched (1 isolated referee each, changed items only). CW8 merges after verification.

## R19 (2026-11-06): full-band carrier cascade (user request)
| FBC | Si full-band cascade stage 1 (EPM bands, screened-Coulomb impact ionization, deformation-potential phonons at mK, DM/photon seeds) | briefs/R19/FBC.md | returns/R19/FBC.md |
