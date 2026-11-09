# Ch16 post-revision check (isolated verifier, 2026-11-06)

Scope: tex/ch16/*.tex (with s16-summary), D-41, D-42, the E-6/E-11/E-20/E-21 narrow edits, figscripts/ch16 logs, the review
ledgers (R1–R13). No tex or script was edited. Independent recomputations were made in the scratchpad: the kinematic thresholds, the
TLS host term, the graphene v_D/g_c/subband/J0 numbers, (δn/n₀)², the heat-release factor and the F–H mass. zrte5_16.py was also
rerun from a scratch copy with the full NR row of 1910.02091 Table 1 (v = 1.1, 0.45, 1.0 e-3; Λ = 0.23, 0.215, 0.1 Å⁻¹; Δ = 11.8 meV).

Verdict: **ACCEPT WITH FIXES** (F1–F5 below; none of them touches a derivation).

## 1. R1, ZrTe₅

| Item | Status | Note / correction |
|---|---|---|
| 11.8 meV is the source's NR half-gap | CONFIRMED | 1910.02091 Table 1, NR row Δ = 11.8 meV; text below the table: gaps 31.2/23.6 meV ↔ Δ = 15.6/11.8 meV. |
| Hybrid (NR Δ with ISIF7 velocities and cutoff) | CONCERN (F1) | The source gives each structure as one self-consistent row: NR is v = (1.1, 0.45, 1.0)e-3 with Λ_y = 0.215 Å⁻¹. The hybrid is not a row of the table. The text discloses the velocity difference ("at most 10 %") but not the cutoff: Λ̃ = min v_iΛ_i is 0.191 eV (NR) against 0.180 eV (ISIF7), +6 %. The effect is small but not zero (scratch rerun, NR row, book halo): thresholds 8.0 keV isotropic and 9.6/7.1/**9.0** keV along x/y/z (book: 8.5 along z). Rate at 100 keV and 1e-38 is **108**/kg-yr (book: 122). Best reach 1.5e-40 at 38 keV (book: 1.36e-40). Published/total ratio **5200–6430** (book: 5490–6630). Absorption factor 6.3–6.4, ζ ≈ 1.25e-15. α̃ = 0.183, binding 0.10 meV, Sommerfeld shares 60/12/3 %, expansion parameter 1.02. Preferred fix: let the 11.8 meV row supply all its parameters (rerun zrte5_16, we16_9, fig16_1 and update 16.1, the opener, the summary and the nuisance row; the summary's "7.1 to 9.6 keV" is unchanged). Minimal fix: keep the hybrid, add the cutoff to the disclosure, and give the NR-row numbers in one sentence as the cross-check. |
| Thresholds 7.9 iso; 9.6/7.1/8.5 keV (hybrid) | CONFIRMED | Independent brentq: 7.93; 9.58, 7.10, 8.54 keV (v_max = 794.5 km/s). |
| Scattering factor 5500–6600 (book halo) | CONFIRMED (hybrid) | Log: 5490–6634 over 20 keV–1 MeV. With the full NR row it is 5200–6430 (see F1). |
| "4300 to 6600 over half-gaps 11.8, 15.6 and the halos of Fig. 16.1" | WRONG (F2) | 4293 is the (220, 232, **544**) halo at 15.6 meV, and that halo is not in Fig. 16.1: fig16_1.py plots only (220, 232, 600). Over the book halo and the 600 halo the range is 4800–6600 (minimum 4814, at 15.6 meV with the book halo). Either name the 544 halo in the text or print "4800 to 6600". |
| Halo band 0.8–1.1 (v₀ 220, v_E 232, v_esc 600) | CONFIRMED, wording CONCERN (F5) | Log: 0.79–1.09 (m ≥ 20 keV). The (220, 232, 544) halo gives 0.79–1.74, so the closure depends on choosing v_esc = 600. "a difference of halo" → "consistent with a difference of halo". |
| One-loop parameter 1.03 (0.93 at 15.6) | CONFIRMED | g α̃ ln(Λ̃/Δ) = 0.380 × 2.72 = 1.03. Stated as "at the edge of the expansion". |
| "at least 7.6" | CONFIRMED, located in 16.1 l.35, not D.41 | It is derived from v_D < v_max (scattering) plus α̃ < 1, so ε_bg > 2.75. α̃ < 1 is necessary, not sufficient (ZrTe₅ has α̃ = 0.19 but an expansion parameter of 1.03), so as a lower bound it is valid. The ratio ε_bg² is exact for any ε_D. ZrTe₅ (5500 ≫ 7.6) is consistent. D.41 claims only the exact ε_bg², ε_bg identities, which hold. |

## 2. R2, TLS scattering — CONFIRMED
Host: n_χ⟨v⟩σ̄(1+m/m_e)² · 4n_e²C_l/(ρc_l²) / (4ρ_T). With n_e = 6.615e23 cm⁻³, ρc² = 4.619e23 eV/cm³, C_l = 1.9e-4 and
⟨v⟩ = 354.1 km/s this gives 6.57e-3 /(kg·day·meV); the core term is ×2.457, so the total is **2.27e-2**. The averaged C = 2.6e-4 gives
×1.368, i.e. 3.1e-2. 16.7 (l.155–159), Table 16.1 (s16-9 l.30), the nuisance row and the summary (2.3e-3 per kg-day below 0.1 meV)
all agree. 16.8 l.162 quotes both P̄ (1.2e20 averaged, 0.88e20 C_l), consistently labeled.

## 3. R4, v_D = 3.02e-3 — CONFIRMED
3ta_cc/2 = 3·2.8·1.42/(2·1973.27) = 3.022e-3 (9.06e5 m/s). Kernel 35.4/21.3/7.7 → g_c = 0.166/0.212/0.339 (0.17/0.21/0.34).
Plasmon speed 6.9/5.4/3.4 v_max. Single channel 0.398. Subband pairs 2v_D/r_t = 1.70 eV. q⊥r_t ≥ 0.760, where J0² = 0.741, and 1.519,
where J0² = 0.25. 1 nm tube: 2Δ₁ = 0.80 eV, edge at 226 keV. limit16_2a: 10 % at 1.36 k_F, g_c 0.18–0.61. No stale 3.41e-3 remains
in tex or logs. The two-velocity clause is gone from Table 16.1.

## 4. R5, anthracene — CONFIRMED
WE 16.4 sets E_La = 3.1 + 0.197 + 0.016 = 3.31 eV, with E∓ = 3.100/3.131 eV (we16_4.log 3.3123, 3.1000, 3.1313). The crystal shift
is counted once. The f sums are 0.460 vs 0.491 (ratio 0.938 vs 0.941), consistent with f(L_a) = 0.23 at 3.1 eV scaled to 3.312 eV.
Limit Check 16.4a shifts its full model so that the lowest allowed Q→0 exciton sits at 3.100 eV (+0.266 eV). The binned line of
Fig. 16.4 is at 3.1 eV (fig16_4.log). Window 0.88–1.0 MeV with ratio 1.383. The two models use different shifts (+0.212 vs +0.266);
this is coherent because each anchors its lowest allowed state at 3.1 eV. "L_b has no dipole in the model": present.

## 5. R6, F–H threshold — CONFIRMED
The route opens at the free-exciton energy, which lies below the 14.2 eV gap, so the threshold mass is below 2·14.2/v_max² = 4.04 MeV.
"An upper bound on the threshold" and "at least 46 times less than 0.186 GeV" (186/4.04 = 46.0) are both correct. A sourced
exciton energy (≈12.6 eV would give 3.59 MeV) is still owed, which is logged. The Fig. 16.6 legend and docstring match.

## 6. R3, R7–R13 spot checks

| Item | Status |
|---|---|
| (δn/n₀)² = (7.29e22/2.69e24)² = 7.3e-4 → "7×10⁻⁴" (s16-7 l.220) | CONFIRMED |
| Dots 0.76–1.03 (qR = 8), 0.70–0.97 (qR = 3), 2.4–66 nearer the gap (limit16_3b.log) | CONFIRMED |
| Hochberg Eq. (5)/(7) double-count clause, "unless each … weight ½" (s16-3 l.27) | CONFIRMED |
| L^D throughout 16.5 and Limit Check 16.5a | CONFIRMED |
| Relaxation plateau: fastest systems at u = 1, π/4 from u² ~ ωτ₁(1) (s16-7 l.71) | CONFIRMED |
| Crossover 0.71 keV aligned, 1.2 keV orientation-averaged (tls16_7.log 0.706/1.224) | CONFIRMED |
| Heat release 0.15·(14.5/4.8)² = 1.37 → 1.4; text values 5.5/14.1 K → 0.99; source "roughly twice", all printed | CONFIRMED |
| Summary: 7.6 scattering, 2.75 absorption | CONCERN (F3): see below |
| Map caption: 1a; 2a–c; 3a,b; 4a; 5a; 6a; 7a–d; 8a–d = 17 | CONFIRMED |
| Process asides: the remaining "misprint" mentions (s16-5 l.37, summary) concern published formulas, so they are substance | CONFIRMED |
| US spelling: no British forms found in ch16 or D.41/42 | CONFIRMED |
| E.20 642/5.03 (25.34² = 642.1, √ = 5.03); E.11 V_b; E.21 exponent and M_1 present | CONFIRMED |

F3. Summary l.3, "…at every mass, wherever the one-loop response holds by at least 7.6 for scattering and 2.75 for absorption",
has two problems. (a) Punctuation: "by at least" attaches to "holds". Write "…at every mass; wherever the one-loop response holds,
the factors are at least…". (b) No section derives the 2.75 bound for absorption. It follows only for cones slower than v_max, since
absorption has no kinematic need for v_D < v_max: a cone with v_D > v_max has α/v_D < 2.75. Add "for cones slower than v_max" (or
state the absorption bound once in 16.1 l.35 with that condition). Also, the "7.6" of 16.1 l.37 (the ε_bg = |ε_D| peak at 50 meV) is
an unrelated value that can be confused with the bound. Optional: reword it as "|ε_D| = 7.6".

## 7. Summary and tables against the sections

| Item | Status |
|---|---|
| Summary ZrTe₅: 11.8 meV, 7.1–9.6 keV, 122/kg-yr, 1.4e-40 at 40 keV, 5500–6600 (book halo), ζ 1.2e-15, ×6.2, expansion ≈ 1 | CONFIRMED vs 16.1 (hybrid numbers; they would follow F1) |
| Nuisance rows: Sommerfeld 65/13/4 %, 0.11 meV, α̃ = 0.19, iso ×2.4–2.7, tube 1.36 k_F and 1.7 eV, dots, Frenkel 6.3/27/38 %, TLS 2.3e-2 | CONFIRMED |
| Table 16.1 and s16-9 l.9: "computed half-gaps 11.75–17.5 meV" | CONCERN (F4): 11.75 meV is the "Exp. [52]" (measured) row, not a computed one. Write "the rows of the table, computed and measured, span 11.75 to 17.5 meV", or "computed 11.8–17.5 meV". The thresholds 7.1–10.5 keV are unaffected (7.07 vs 7.10 keV). |
| Ch7 we:7-zrte5 and the E.20 table still carry 15.6 meV, labeled "implemented row" | Known, logged as owed (LOOSE-ENDS); not a Ch16 defect |

## Fixes required for acceptance
- F1 (R1): use the full NR row for the 11.8 meV central case, or disclose the cutoff too and quote the NR-row cross-check
  (108/kg-yr, 1.5e-40, 5200–6430, z threshold 9.0 keV, ζ 1.25e-15).
- F2 (16.1 l.64): "4300 to 6600 … halos of Fig. 16.1": name the (220, 232, 544) halo, or print 4800–6600.
- F3 (summary l.3): fix the punctuation and condition the 2.75 absorption bound on v_D < v_max (or derive it in 16.1).
- F4 (s16-9 l.9, Table 16.1): 11.75 meV is the measured row.
- F5 (Fig. 16.1 caption): "a difference of halo" → "consistent with a difference of halo".
