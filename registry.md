# Registry: approach families

| Family | Status | Rounds | Notes |
|---|---|---|---|
| Golden-rule 2nd-order perturbation theory (DM × e-ph), Bloch basis | used (final, R17): cross-checked against D2 on shell (SOTA R1 #1), absorbed into WP3 (M.1) (REFEREED R7); the tier-H pipeline DC-1 computes it | R1–R17 | D1 |
| Kubo / diagrammatic: phonon self-energy and vertex corrections to the density–density response | used (final, R17): WP3 (M.1)–(M.14) (REFEREED R7); δρ^V in Kubo (Matsubara) form (CW1 (CW1.20), CLAIMED + VERIFIED) | R1–R17 | D2 (independent route) |
| Adiabatic Herzberg–Teller: derivative of frozen-phonon transition density (DFPT) | covered (final, R17): error ~ω_Q/δ (SOTA R1 #8, CLAIMED); its numerical test is CONTROLS C6 inside DC-1 (not run) | R1–R17 | via D1/D2 and C6 |
| Special-displacement (ZG) supercell + existing DM–e codes | FORMULATED (final, R17): COMP-PAER tier H (DC-1) and X2 Route S (DC-17, CW1 §18 + errata E-15 meshes); not run | R1–R17 | computational route T3c |
| Data-calibrated optical-limit estimate from measured Si indirect absorption | used (final, R17: R15 COMP-PAER rate/reach [E, ×/÷10], with the finite-q vertex ℱ_ρ(q); CLAIMED; the T-transfer of 77 K data is CW1 (CW1.23)); replaced by DC-1 when run | R1, R15, R17 | N1 (tier B estimate); COMP-PAER IF-CP-3: dipole extrapolation alone overstates S̄ ×10–40 |
| First-principles single-channel check (pyscf, 8-atom cubic Si, X phonon folded to Γ) | superseded (final, R17): the same check is CONTROLS C6 (8-atom frozen phonon at X) of DC-1; not run | R1–R17 | N1 (C6) |
| URF architecture: coupled e–N–spin response matrix S_{OO′} + expansion hierarchy | used (final, R17): WP0-v3 REFEREED (R7); basis 17 one-body rows + 𝔘_C (CONVENTIONS §7, R17) | v2–R17 | WP0 |
| Sector expansions WP1–WP6 | REFEREED (R7, v3; WP5 v4 R14/R16); closure packages CW1–CW7 CLAIMED + VERIFIED (CW1 final R17); WP8 (U, F, S) VERIFIED (R17) | v2–R17 | after WP0 |
| Low-T defect quantum kinetics: crowdions, defectons, tunneling two-level systems (TLS). Covers (i) energy partition / delayed stored-energy release at mK, (ii) pre-existing defects/TLS as sub-meV target states, (iii) metal-film sensor layers (Al, W, WSi) | covered (final, R17): WP7-T (REFEREED, R12); R16 CW5 closures CLAIMED + VERIFIED | R10–R16 | Not in WP4/WP5 v2 beyond classical MD annealing (WP5 R4 is conjectured only). Candidate follow-up package after R7. R16: WP5 R4 → CW5 §3.5 (exact gap) |
