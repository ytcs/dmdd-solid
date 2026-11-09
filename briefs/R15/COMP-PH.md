# R15 compute brief COMP-PH: ground-state, phonon and dielectric inputs (Si, Ge, then small-cell survivors)

## Target
Produce the converged first-principles inputs that WP8-F and the PAER window need, with controls, for:
1. **Si and Ge (priority):** relaxed lattice; PBE band structure with the indirect gap, CBM valley positions and the scissor to experiment stated; DFPT phonon dispersion on a converged q grid, interpolated (q2r/matdyn) and compared with inelastic neutron data (CONTROLS); ε_∞; WP8-F G-F5 inputs: E_min^{ZPL}(q*) and ω_ν(Q*) on the PAER window grid of /home/user/dmdd-solid/returns/R8/WP3-v3.md §M3–§M4 (check the window 0.333–0.337 MeV quoted in returns/R13/WP8-F.md).
2. **Small-cell WP8-U survivors with GAP or [DB]-only dielectric/phonon entries** (2–4 atoms first: diamond, 3C-SiC, GaAs, LiF, NaF, then 4H-SiC and Al₂O₃ if the gate allows): Γ-point DFPT ε_∞, ε₀, Born charges Z*, ω_TO, ω_LO, ω_max, sound speeds from the acoustic slopes. Compare each with the [FT]/[DB] values in /home/user/dmdd-solid/returns/R13/WP8-U.md and /home/user/dmdd-solid/returns/R13/WP8-U-table.csv; report agreement.
Output a CSV /home/user/dmdd-solid/code/COMP-PH/properties.csv (material, property, value, unit, tag=[CALC], convergence note) in the WP8-U-table column format.

## Read
/home/user/dmdd-solid/code/ENV.md, /home/user/dmdd-solid/CONTROLS.md, /home/user/dmdd-solid/returns/R8/WP2-v3.md (phonon conventions), /home/user/dmdd-solid/returns/R8/WP3-v3.md §M3–§M4, §M10, /home/user/dmdd-solid/returns/R13/WP8-F.md §5, /home/user/dmdd-solid/returns/R13/WP8-U.md §4.

Return file: /home/user/dmdd-solid/returns/R15/COMP-PH.md (≤ 300 lines). ID: COMP-PH.

## Compute rules (user directive 2026-11-01; RULES.md, code/ENV.md)
- Environment: read /home/user/dmdd-solid/code/ENV.md first. If /root/mamba/envs/qe is missing, run `bash /home/user/dmdd-solid/code/setup-env.sh`. QE 7.6, SG15 ONCV PBE pseudopotentials (/root/pseudo/sg15). Never /usr/bin/pw.x.
- **Every multi-core job goes through `/home/user/dmdd-solid/code/run-heavy.sh <LABEL> <cmd…>`** (one heavy job at a time on 4 cores; other agents share the box). No job may bypass the lock.
- **Cost gate:** before each job, estimate its wall time and memory from the ENV.md benchmark scaled to your cutoff/grids (and from a small timed pilot). Run it only if it fits ≤ 3 h wall and ≤ 12 GB. Otherwise FORMULATE it: complete inputs, grids, convergence plan, cost estimate, for the user's larger compute. Record every gate decision in a table.
- Extra packages (e.g. wannier90, phonopy) may be installed into the qe env with `/root/bin/micromamba install -n qe -c conda-forge <pkg>` (MAMBA_ROOT_PREFIX=/root/mamba); list them, with versions, in code/<ID>/env-additions.md.
- Work directories (outdir, *.save, wavefunctions, EPW files) live only in /root/work/<ID>/. In /home/user/dmdd-solid/code/<ID>/ keep only inputs, scripts, small outputs (dyn files, frequency/band tables ≤ 1 MB each) and the convergence record.
- Convergence: ecut, k and q grids converged to stated tolerances, with the table in the return. Each computed number is tagged [CALC] (CONVENTIONS) and must pass its CONTROLS.md case or be marked FAILED-CONTROL.
- Follow /home/user/dmdd-solid/CONVENTIONS.md and /home/user/dmdd-solid/NOTATION.md; new symbols only in the closing 'Symbols' section. Literature (for controls) via /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-<ID>/, PDFs deleted at the end.
- Write only your return file and code/<ID>/. Do not commit. End with 'Symbols introduced/used', 'Interface flags', 'Proposed LIMITS rows'. Final message ≤ 15 lines.
