# R17 brief FIX-GAP-EF-GRID: rerun GAP-EF-v2 predictions with the grid-commensurate cascade solver

## Background
The R17 WP8 errata (returns/R17/WP8-errata.md §1) found a bias in code/CW7/cascade_gf.py. A grid step h that does not divide E_g, θ_ii and ω₀ biases the mean pair number by −1.6% at h = 0.02. The fix is to require commensurability and raise an error otherwise.

code/GAP-EF-v2/cascade.py (and code/GAP-EF/cascade.py) round ω₀ onto the grid in the same way.

## Required
1. Port the commensurability requirement to code/GAP-EF-v2/ (copy it to code/GAP-EF-v3/, which you fix).
2. Rerun model.py and predict.py:
   - Verify each value against an independent Monte Carlo for Si, Ge and diamond.
   - Report the change in every ε_eh, F_eh and validation residual. Expect ≈ 1%, but state the actual numbers.
   - State whether any GAP-EF-v2 statement changes: Si F = 0.114 and its 2.6σ, the rms, the closed form, and the predictions table.
3. Write returns/R17/GAP-EF-v3-errata.md, containing:
   - replacement text for every changed number in GAP-EF-v2.md and in GAP-EF-v2-errata.md;
   - the checks, which must pass.

## Rules
Run no heavy numerics. Write only the errata file and code/GAP-EF-v3/. Do not commit. Final message ≤ 10 lines.
