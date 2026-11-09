# R6 revision brief REV-WP0: WP0-v2 (architecture)

## Your package
/home/user/dmdd-solid/returns/R4/WP0.md, extended by /home/user/dmdd-solid/returns/R5/O4.md (Theorem D (iv′)/(iv″)), /home/user/dmdd-solid/returns/R3/X1.md (the C7
soft limit) and /home/user/dmdd-solid/returns/R3/X2.md (the pair-channel screening that refines WP0 §5).

## Defects reported against WP0
These are recorded in SOTA/CORRECTIONS, from WP1, WP2, WP3, WP4, WP5, WP6, O4 and X1/X2. Examples:
- WP6 W1–W5;
- WP5 (§7 seeding: q integrated out too early, tr(𝔇) placement, plasmon double count);
- WP4 (hyperfine factor and sign; Theorem D scope for gapless targets; L15/L16 pointers; table 6.1; wind-odd
  rates in P,T-broken targets);
- WP1 (continuity relation; SOC and the f-sum; Ge core estimates; transverse LFE; spin XC; (7.2) needs
  inversion);
- WP2 (x_coh; 2W for non-cubic sites);
- WP3 (4.9 vs C7a–e; 5.6–5.7 vs X2's M̃; L7d sectors; Migdal–PAER interference for any e+N coupling; boost
  mass m_A; ZG is deterministic);
- O4's Theorem D amendments.

## Authoritative inputs (in order of precedence)
1. /home/user/dmdd-solid/CONVENTIONS.md and /home/user/dmdd-solid/NOTATION.md (v3). All symbols and conventions must follow them exactly.
2. /home/user/dmdd-solid/state/CORRECTIONS.md and /home/user/dmdd-solid/state/SOTA.md: every owed correction to your package and every defect
   other packages reported against it.
3. /home/user/dmdd-solid/returns/R6/WP0-v2.md (for WP1–WP6): the revised architecture. Cite its equation numbers, not v1's.

## Task
Produce a standalone, corrected v2 of your package that a referee can read without the v1. Requirements:
- **Apply every owed correction.** List each one in a closing table: correction ID/source → where applied →
  how. If you disagree with a correction, do not apply it silently: argue it in a section
  "Contested corrections", with a derivation.
- **Resolve every inconsistency** with WP0-v2 and with the other packages' interfaces as recorded in
  SOTA/CORRECTIONS. Where an interface quantity is owned by another package (e.g. WP2's multiphonon S_NN
  feeding WP5), use its recorded form and flag any mismatch in "Interface flags".
- **Keep everything that was right.** Do not drop content to save space; compress the prose instead.
- **Keep the tags** DERIVED (with hypotheses) / ESTIMATED / CONJECTURED, and the source-formula quotes with
  arXiv ID and equation number for each LIMITS entry.
- **Re-run or update** your package's checks script into /home/user/dmdd-solid/code/<WP>-v2/. All checks must pass. Sympy only;
  no numerical simulations.
- **End with** "Symbols introduced/used" (it should now be empty of deviations).
- **Do not edit** any v1 return, referee report or state file.

Write /home/user/dmdd-solid/returns/R6/WP0-v2.md (≤ 650 lines). Your final message is a summary of ≤ 15 lines, including the
count of corrections applied and contested, and any interface flags.
