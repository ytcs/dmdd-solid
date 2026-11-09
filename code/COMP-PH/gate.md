# COMP-PH cost-gate record (limit: <= 3 h wall, <= 12 GB per job; one heavy job at a time via run-heavy.sh)
Benchmark (ENV.md): Si 2-atom, 20 Ry, 8^3 k: SCF 2 s; DFPT 4^3 q: 3.5 min. Scaling used: wall ~ (ecut/20)^1.5 x (N_el/8) x (N_irr q / 8); RAM from pw.x/ph.x "Estimated" lines.
| # | job family | estimate (wall, RAM) | basis | decision | measured |
|---|---|---|---|---|---|
| 1 | Si SCF pilot 40 Ry 8^3 | 10 s, < 0.1 GB | benchmark x (2)^1.5 | RUN | 4.4 s, 24 MB |
| 2 | ecut scans, 7 materials x 9 cutoffs (30-120 Ry), 8^3 k, SCF | <= 60 s each, < 1 GB | pilot x (120/40)^1.5 x N_el/8 | RUN | see conv/ |
| 3 | k scans Si 60 Ry (4-14), GaAs/C extra ecut 140-160 | < 2 min each, < 0.2 GB | pilot scaling | RUN | <= 73 s (lock wait excluded) |
| 4 | Si vc-relax 60 Ry 12^3 | 2 min, < 0.1 GB | 10 x SCF | RUN | 63 s |
| 5 | Si Gamma DFPT + epsil, 60/80 Ry, k 8-18 | 2-10 min, < 0.2 GB | benchmark x (60/20)^1.5 / 8 q | RUN | 65-331 s |
| 6 | Si DFPT 4^3 q (8 q), 60 Ry, k 8 | 25-35 min, 35 MB | benchmark 3.5 min x 5.2 x load 2 | RUN | 1486 s (a_PBE), 599 s (a_exp) |
| 7 | Si DFPT 6^3 q (16 q) | 60 min, 35 MB | 2 x row 6 | RUN | 2216 s |
| 8 | Si DFPT 8^3 q (29 q) | 1.5-2 h, 35 MB | 3.6 x row 6 | RUN (<= 3 h) | 4707 s |
| 9 | Si Wannier: nscf 10^3 / 14^3 full grid nosym, 16 bands | 5 / 15 min, < 0.5 GB | SCF x N_k | RUN | 237 s / 412 s (+ pw2wan, w90 < 2 min) |
| 10 | Ge Gamma DFPT 60/80 Ry k 8 (pilot) | 3-5 min | 2.2 x Si Gamma | RUN | 146 / 244 s |
| 11 | Ge DFPT 4^3 q, 80 Ry, k 8 | 40-70 min, < 0.2 GB | 9 x row 10 (Si q4/Gamma ratio) | RUN | 7589 s (low-symmetry q: 55 min each; estimate low by 2x, still < 3 h) |
| 12 | Ge DFPT 6^3 q | ~4 h (16 q x 16 min) | 2 x row 11 measured | FORMULATED (over gate) | - |
| 13 | Small-cell Gamma DFPT + 4^3 q batch (C, 3C-SiC, GaAs, LiF, NaF, 4H-SiC, Al2O3) | 2-atom: 0.5-6 h each (4^3 q) at 90-140 Ry, Gamma-only 5-30 min; 4H-SiC (8 at.) ~10-20 h; Al2O3 (10 at., Al 11 e) ~30-60 h, 2-6 GB | N_el, ecut^1.5, nat^2 scaling of row 6 | FORMULATED (coordinator rescope 2026-11-01; 4H/Al2O3 also over gate) | inputs in formulated/ |
| 14 | Ge HSE06+SOC bands + Wannier (E_min^ZPL(q), correct L/Gamma order) | 8^3 full grid nosym, nq 4^3, FR: ~20-60 h CPU, 4-8 GB | EXX ~ N_q x N_k x N_b^2 FFTs | FORMULATED (over gate) | inputs in formulated/Ge-HSE-SOC/ |
| 15 | Ge Gamma DFPT 80 Ry k 10 | 6 min | row 10 x 1.4 | RUN | 330 s |
