# R17 brief DEFERRED-COMPUTE: the complete ledger of deferred computations

## Purpose
The user will direct another agent to run every computation the campaign deferred under the directive "derive and specify now, compute later". Build the single authoritative work list: /home/user/dmdd-solid/state/DEFERRED-COMPUTE.md.

It must be usable by an agent that has never seen this campaign. Each item stands alone, with absolute paths.

## Sources: sweep all of them
- **state/LOOSE-ENDS.md:** every compute-formulate and compute-in-box row, and every CLOSED-AS-EXACT-GAP row whose missing step is a computation.
- **Specifications in the returns:**
  - WP0–WP6 v3 "computation specification" / "Exact remaining gaps" sections, WP5-v4, WP7-*-v2, WP7-E-v3;
  - GAP-EF-v2 §5 plus its errata;
  - COMP-PAER tier H (code/COMP-PAER/tierH/) and its stages 5–6 (new code);
  - COMP-PH: the survivor Γ-DFPT batch, specified not run;
  - CW1–CW7 and their errata: every spec, including fork inputs in code/CW3/fork/, code/CW2/inputs/, code/CW5/LE-128/, LE-137/;
  - WP8-R / CW6 CMPMC run specs;
  - WP8-F gaps G-F2 and G-F5;
  - IF-R8-10, the GaAs Γ/δ map;
  - the ab initio ε_eh/F_eh route.
- **Owed data that only a computation or measurement can supply:**
  - CsI elastic constants;
  - YIG and the magnets;
  - CaWO₄ and Li₂MoO₄ ε₀, ω_LO/TO and Z*;
  - every GAP cell in returns/R16/WP8-U-table-v4.csv that a DFT/DFPT run could fill.
- **Missing infrastructure:**
  - GW / full-frequency ε⁻¹ in qe-rtsc (https://github.com/ytcs/qe-rtsc/issues/1);
  - the PAER density vertex and kernel code;
  - CMPMC design-note items (DESIGN_NOTES.md in /home/user/cmpmc) and the unvalidated modules.
- **R15-era CMPMC runs** affected by the Kaplan-buffer bug: the recheck list.

## Format
1. Summary table, one row per item:

   ID (DC-n) | quantity | material(s) | why it matters (book section / narrative) | code (QE fork / EPW / BerkeleyGW-or-fork-GW / CMPMC / MD-MLIP / other) | spec location (file § or path) | inputs ready? (path or "to write") | depends on (other DC-n, or new code) | cost estimate (core-h or GPU-h, with its source) | priority (P1 narrative-critical / P2 completes a channel / P3 refinement)

2. Then one section per item:
   - the physics it serves;
   - the exact quantity and its units;
   - the method and the approximation level;
   - convergence parameters and acceptance tests (the CONTROLS case it must pass);
   - pitfalls;
   - where the result goes back into the book or the returns.

3. A dependency graph: which new code or infrastructure blocks which items.
4. A recommended execution order.
5. Totals.

## Rules
Read only; write only state/DEFERRED-COMPUTE.md. Do not commit. Deduplicate items listed in several places, and keep every source pointer. Final message ≤ 10 lines: item count by priority and code, total cost, and the critical-path blockers.
