# R15 compute brief COMP-PAER: Si PAER numbers (M1 tiers B and, if it fits, H)

## Target
The original M1 deliverable (state/STATEMENT-v1-PAER.md T5, T6; DONE.md tiers B and H): Si (then Ge) PAER kinematic window, rate and projected reach, computed from the refereed recipe /home/user/dmdd-solid/returns/R8/WP3-v3.md §M10 (with §M3–§M8 and the X2 screening; LIMITS L8).
1. **Tier B (T5) first:** the Si window where PAER is the leading ER channel, and the rate dℛ/dω and reach for heavy and light mediators in it, from first-principles inputs at reduced cost (DFT bands + scissor, DFPT/EPW e–ph at the valley-connecting Q, the N_W-only Wannier route valid for q ≲ 0.5αm_e, adiabatic/DFPT variant (M.12) with its ω_Q/δ error bar), with uncertainty and all inputs. Halo and normalisations per CONVENTIONS §8–§9.
2. **Tier H (T6) if the cost gate passes:** the converged spectrum per §M10 (ASR on g keeping its O(Q) part, dynamical quadrupoles in long-range g, shared gauge for g and ρ, Bethe-ridge remainder by Sternheimer or a large disentangled manifold with an N_W test), convergence tables. If it does not fit, formulate it completely (inputs, grids, per-step cost) for the user's compute.
3. **Controls** CONTROLS.md C1–C8 as applicable (WP3-v3 §M9), in particular the zero-phonon limit, the f-sum, the soft-acoustic C7 and the phonon-assisted optical absorption near the indirect edge against measured ε₂/α(ω) (LIMITS L9).
Use COMP-PH outputs if present in /home/user/dmdd-solid/code/COMP-PH/ (it runs in parallel; coordinate only through those files, read-only).

## Read
/home/user/dmdd-solid/code/ENV.md, /home/user/dmdd-solid/state/STATEMENT-v1-PAER.md, /home/user/dmdd-solid/DONE.md, /home/user/dmdd-solid/CONTROLS.md, /home/user/dmdd-solid/returns/R8/WP3-v3.md, /home/user/dmdd-solid/returns/R3/X1.md, /home/user/dmdd-solid/returns/R3/X2.md, /home/user/dmdd-solid/returns/R8/WP6-v3.md (halo, reach statistics), /home/user/dmdd-solid/LIMITS.md (L8, L9).

Return file: /home/user/dmdd-solid/returns/R15/COMP-PAER.md (≤ 400 lines). ID: COMP-PAER.

## Compute rules (user directive 2026-11-01; RULES.md, code/ENV.md)
- Environment: read /home/user/dmdd-solid/code/ENV.md first. If /root/mamba/envs/qe is missing, run `bash /home/user/dmdd-solid/code/setup-env.sh`. QE 7.6, SG15 ONCV PBE pseudopotentials (/root/pseudo/sg15). Never /usr/bin/pw.x.
- **Every multi-core job goes through `/home/user/dmdd-solid/code/run-heavy.sh <LABEL> <cmd…>`** (one heavy job at a time on 4 cores; other agents share the box). No job may bypass the lock.
- **Cost gate:** before each job, estimate its wall time and memory from the ENV.md benchmark scaled to your cutoff/grids (and from a small timed pilot). Run it only if it fits ≤ 3 h wall and ≤ 12 GB. Otherwise FORMULATE it: complete inputs, grids, convergence plan, cost estimate, for the user's larger compute. Record every gate decision in a table.
- Extra packages (e.g. wannier90, phonopy) may be installed into the qe env with `/root/bin/micromamba install -n qe -c conda-forge <pkg>` (MAMBA_ROOT_PREFIX=/root/mamba); list them, with versions, in code/<ID>/env-additions.md.
- Work directories (outdir, *.save, wavefunctions, EPW files) live only in /root/work/<ID>/. In /home/user/dmdd-solid/code/<ID>/ keep only inputs, scripts, small outputs (dyn files, frequency/band tables ≤ 1 MB each) and the convergence record.
- Convergence: ecut, k and q grids converged to stated tolerances, with the table in the return. Each computed number is tagged [CALC] (CONVENTIONS) and must pass its CONTROLS.md case or be marked FAILED-CONTROL.
- Follow /home/user/dmdd-solid/CONVENTIONS.md and /home/user/dmdd-solid/NOTATION.md; new symbols only in the closing 'Symbols' section. Literature (for controls) via /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-<ID>/, PDFs deleted at the end.
- Write only your return file and code/<ID>/. Do not commit. End with 'Symbols introduced/used', 'Interface flags', 'Proposed LIMITS rows'. Final message ≤ 15 lines.
