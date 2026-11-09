# THREADS ledger (seeded from SPINE at design time; revised after the spine reviews; the editor merges rows)
Part I numbers follow the revised Part I sections (2026-11-01, SPINE change log, second entry: Chap. 4 has nine sections, Chap. 6
gains the phonon self-energy in 6.4 and loses the method section). Parts II–III entries were designed in SPINE-II (2026-11-01).
ledgers/check_concepts.py checks that every column equals the "Threads" lines of the SPINE entries of all chapters.

| Thread | Opened | Advanced | Closed |
|---|---|---|---|
| T1 kinematic edge | 1.3 | 3.1, 3.3, 3.4, 7.2; 9.2, 10.1, 11.1, 13.1 | 21.3 |
| T2 screening | 4.4 | 4.5, 4.6, 4.8, 4.9, 5.5, 6.2, 7.3; 8.4, 10.2, 10.3, 10.5, 11.2, 13.4, 16.1 | 17.1 |
| T3 sum rules | 4.3 | 4.4, 4.5, 7.2; 8.3, 8.6, 10.2, 11.3, 12.5, 15.1 | 22.1 |
| T4 Born–Oppenheimer hierarchy | 5.1 | 5.7, 6.1, 6.3, 6.4; 8.5, 8.6, 11.5, 12.1, 13.6 | 17.4 |
| T5 silicon phonon-assisted window | 3.3 | 6.5; 13.1, 13.2, 13.3, 13.5 | 13.9 |
| T6 response → measured signal | 1.5 | 7.4; 8.2, 8.7, 16.6, 16.8, 18.1, 18.3, 19.1, 19.5, 20.5 | 21.6 |
| T7 theory uncertainty | 1.5 | 3.4, 4.6, 4.9, 6.3; 8.8, 10.10, 11.9, 13.7, 14.2, 15.2, 16.9, 18.5 | 21.4 |

**SPINE-II-REV (2026-11-02).** Section 13.7 was removed (its physics folded into 13.2, its method into App. E.5), so the silicon window is
now 13.9 and T5 closes there; temperature and zero-point renormalization (old 13.8, now 13.7) still advances T7. Sections 14.7 and 15.5
were merged into their chapter summaries (structural review S17); their T7 advances move to 14.2 (the 1/|𝐒| corrections as nuisances)
and 15.2 (the one-sided nuisance and the superconducting nuisance set). The guide to next targets moved from 17.7 to 21.7; it carries no
thread.

**Closures in Parts II–III (SPINE-II, 2026-11-01).** The closures the earlier note proposed are now in the entries: T2 closes in 17.1
(screening decides the comparison of sectors), T4 in 17.4 (the Migdal–phonon-assisted interference is the last use of the hierarchy), T3
in 22.1 (the sum-rule checks each open computation must pass). Moved by the restructure: T5 closes in 13.10 (was 13.9; Chap. 13 gained
the screening section), T1 in 21.3 (was 21.2; halo-independent bounds became 21.2), T7 in 21.4 (was 21.3), T6 in 21.6 (was 21.5). The
former "chapter (g) sections" of T7 are now the explicit uncertainty sections 10.10, 11.9, 14.7, 15.5, 16.9 (and 13.8, 18.5). The script
compares every column with the entries of all chapters.

## Parts II–III check (2026-11-01)
- **T1**: 9.2 draws the kinematic map; 10.1 and 11.1 give the electronic and acoustic edges; 13.1 the phonon-assisted onset against the
  zero-phonon threshold; 21.3 closes with the edge power laws and degeneracies of a limit. Consistent.
- **T2**: 8.4 fixes screening for every coupling; 10.2–10.5 apply it to the electronic sector; 11.2 to polar phonons; 13.4 to the
  phonon-assisted amplitude; 16.1 to Dirac materials; 17.1 closes it where it decides which sector dominates. Consistent.
- **T3**: 8.3 collects the exact relations, 8.6 the partial sum rules; 10.2 (loss-function bounds), 11.3 (coherent weight), 12.5 (Migdal
  sum rules) and 15.1 (conserving BCS response) use them; 22.1 closes with the checks every open computation must pass. Consistent.
- **T4**: 8.5–8.6 make the hierarchy explicit; 11.5 (anharmonic band), 12.1 (non-adiabatic joint response), 13.6 (soft and resonant
  regions) advance it; 17.4 closes with the cross-sector interference. Consistent.
- **T5**: 13.1–13.3 and 13.5 build the window from kinematics, amplitude, rate and optical limit; 13.9 (13.10 before SPINE-II-REV) closes
  with the established edges and the open items. Consistent.
- **T6**: 8.2 and 8.7 define the rate and the resolved response; 16.6 and 16.8 add defect final states and delayed signals; 18.1, 18.3,
  19.1, 19.5 and 20.5 carry the energy to quanta; 21.6 closes with the response libraries. Consistent.
- **T7**: 8.8 defines nuisances; each sector's uncertainty section advances it; 21.4 closes with the theory band of a limit. Consistent.

## Part I check against the revised sections (2026-11-01)
- **T1** opens in 1.3 (kinematic reach, m_min, the edge of η). 3.1 measures q against the zone; 3.3 sets E_min(q) and the indirect-gap
  thresholds against the reach; 3.4 shows how the gap problem moves m_min; 7.2 adds the meV pair-breaking threshold. Consistent.
- **T2** opens in 4.4 (proper/improper response, ε, L, electron-only versus total charge). Advances: 4.5 (electron-gas screening: RPA,
  Lindhard, plasmon), 4.6 (local fields and kernels in crystals), 4.8 (the screened interaction W^scr), 4.9 (the screened direct
  kernel of the BSE), 5.5 (lattice contribution, ε₀ versus ε_∞), 6.2 (screened e–ph vertex), 7.3 (background screening of Dirac
  electrons). Consistent.
- **T3** opens in 4.3 (f-sum rule, Kramers–Kronig). Advances: 4.4 (f-sum of L and ε₂), 4.5 (checks on the Lindhard and Mermin functions),
  7.2 (a bare BCS bubble violates the f-sum; a conserving response restores it). Consistent.
- **T4** opens in 5.1 (Born–Oppenheimer approximation and κ_BO). Advances: 5.7 (anharmonic order in κ_BO), 6.1 (non-adiabatic coupling and
  its power counting), 6.3 (second order in displacements: electron self-energies; Migdal's adiabatic theorem), 6.4 (the phonon
  self-energy and the phonon-side Migdal theorem). Consistent.
- **T5** is seeded in 3.3 (indirect gap, k_c, why a vertical transition at the gap needs a phonon). It advances in 6.5: phonon-assisted
  optical absorption is the q → 0 version of the window. Consistent.
- **T6** opens in 1.5 (signal chain). 7.4 adds defects and color centers as final states and readouts. Consistent.
- **T7** opens in 1.5. Part I advances: 3.4 (band-gap problem), 4.6 (spread of the response hierarchy), 4.9 (the BSE rung completes the
  hierarchy), 6.3 (zero-point renormalization of the gap). Consistent.
