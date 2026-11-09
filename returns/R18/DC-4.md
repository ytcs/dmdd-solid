# R18 / DC-4: Ge DFPT on a 6³ q grid

Spec: state/DEFERRED-COMPUTE.md DC-4; returns/R15/COMP-PH.md §3.2–§3.3, §6.3. Records: code/DC-4/ (out/merged/ holds all 16 dyn files, Ge.fc, Ge_window_q6.json). PBE, SG15 Ge_ONCV_PBE-1.2, 80 Ry, k 8³, a_exp 5.658 Å, tr2_ph 10⁻¹⁶, asr crystal.

## Provenance of the q points
q1–8: conda QE 7.6 on CPU. The first run died with the session at q9. q9–16: QE 7.6 GPU build, standard path (the fork's Sternheimer engine declined this case under strict mode). q8 run on both as a cross-check: **max |Δω| 0.005 cm⁻¹ over 6 modes**, q̂ and dyn0 identical. Merged by file.

## Result [CALC]
| quantity | 4³ (COMP-PH) | 6³ | test | verdict |
|---|---|---|---|---|
| ω_TA(Q*), q̂-minimised, q* = 0.56 keV | 6.817 meV | **6.703 meV** | Δ ≤ 0.3 meV | PASS (0.114) |
| largest Δω_TA over the window grid | – | 0.285 meV at q = 1.36 keV | ≤ 0.3 meV | PASS, narrowly |
| on-axis TA, LA at q* | 6.83, 22.1 meV | 6.708, 21.995 meV | | |
| ϑ of the TA minimum at q* | 0.10 | 0.05 | off axis in both | |
| PAER continuum edge | 0.21383 MeV | **0.21380 MeV** | | |
| PAER replica edge (E_x^b 4.0 meV [E]) | 0.21267 MeV | **0.21264 MeV** | | |

INS control (Γ, X, L, pre-registered 5%): Γ, X and L lie on both grids, so COMP-PH §3.2's values stand and the grid cannot change them. **TA FAILED-CONTROL: X_TA −13.5%, L_TA −11.6%.** Other branches pass (−0.1% to −2.3%). Cause not proved: consistent with PBE at a lattice compressed relative to PBE equilibrium; the LDA run in progress tests this.

## Consequences
- LE-16's q-grid part closes. COMP-PH placeholders GE_QCONV, GE_K, GE_WTA, GE_AXIS can be filled from this table; GE_TABLE and GE_INS stand from §3.2 with the failed TA control.
- Because TA is soft, 6.70 meV should be read with COMP-PH's INS scaling (≈ 7.7 meV); the edge moves by ≤ 0.0003 MeV either way, so the edge values are robust to the failed control.
- ω_ν(Q*) is ready for a window calculation, but no valid Ge E_min(q) exists (DC-2, DC-2-alpha closed).

Run by Claude (LLM); not refereed.

## Addendum: LDA at a_exp (PseudoDojo pw standard, 3d valence, conda QE 7.6 on CPU, 80 Ry, k 8³, 6³ q). Deviation from the PBE convention.
Run crashed once at q1 (pools disagreed at tr2_ph 10⁻¹⁶: check_all_convt) and was resumed with recover, tr2_ph 10⁻¹⁵.

**Γ is INVALID: q1 gives T₂g at −16.91 THz (imaginary), measured 9.12.** The crash was inside Γ's first representation, those three modes are the wrong ones, and every other q is sensible, so a corrupted recovery is the first suspect; not proved, and LDA's near-gapless Γ may contribute. q1 must be recomputed cleanly (≈ 10 min). Until then Ge.fc and anything interpolated from it (ω_TA(Q*), edges) are **not usable**.

X and L are on-grid and come from their own q points:
| mode | LDA (THz) | INS | dev | PBE dev |
|---|---|---|---|---|
| X_TA | 2.288 | 2.38 | −3.9% | −13.5% |
| X_LA | 6.882 | 7.14 | −3.6% | −0.6% |
| X_TO | 7.762 | 8.17 | −5.0% | −0.1% |
| L_TA | 1.757 | 1.86 | −5.5% | −11.6% |
| L_LA | 6.404 | 6.63 | −3.4% | −2.3% |

Reading: TA improves about threefold, which supports the explanation that PBE's TA softness comes from a_exp being compressed relative to PBE equilibrium; it does not prove it. LDA is soft on all branches by about 4–5%, with L_TA marginally outside 5%. No functional passes every branch here.
