# R10 brief WP7-E: reconciling the energy partition (yields, defects, delayed release)

## Target
Deliver one time-resolved energy and charge balance law per event, as scoped in FRAMEWORK.md "WP7-E", that
makes the following parts consistent with each other:
- WP5-v3 (cascade, NR partition, displacement thresholds, stored energy ≠ E_d);
- WP7-T (stored-energy distribution p_st (5.1) and release-time kernel 𝒦^{rel} (5.2); mK tunnelling
  kinetics);
- the literature yield models (Lindhard, R&K, measured quenching data).

## Required
1. **The balance law.** E_dep = E_pairs + Q_prompt + E_stored(t) + E_esc + E_sensor-loss, with each term
   defined from the WP0-v3 final-state-resolved response and the WP5-v3 cascade. E_stored(t) relaxes
   through 𝒦^{rel}.
   - Prove: energy conservation (exact); no double counting of E_d (WP5 counts it once, WP7-T fixes only its
     time profile); yield models acting only on the electronic share.
2. **Charge.**
   - Trapping and release on defect levels, shared between the yield and the detector response with no
     double counting.
   - The measured-charge observable, P(N_eh^{meas} | event, t).
3. **The observable map.**
   - Map onto: prompt heat; measured charge; the delayed-event rate and spectrum (the low-energy-excess
     model from stored energy and sensor-film relaxation, with the 1/t and t^{−3/2} laws of WP7-T).
   - State which detector types see which terms.
4. **Literature limits.** For Lindhard (L20), R&K (L21), Kinchin–Pease (L22) and the measured quenching
   data, state the implicit defect assumption each one folds in, and show each as a limit of the balance
   law. Quote them from full text, or cite the WP5-v3 quotes.
5. **The amendment to WP5-v3.** Write the exact text and equation changes WP5 needs, as an "Amendment to
   WP5-v3" section. Do NOT edit WP5-v3 itself.
6. **Uncertainty.** Nuisance parameters for the new terms, in WP6-v3 types.

## Read
- /home/user/dmdd-solid/returns/R10/WP7-T.md, /home/user/dmdd-solid/returns/R8/WP5-v3.md, /home/user/dmdd-solid/returns/R8/WP0-v3.md, /home/user/dmdd-solid/returns/R8/WP6-v3.md
  (nuisance types), /home/user/dmdd-solid/returns/R8/WP2-v3.md (the multiphonon hand-off);
- /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/state/CORRECTIONS.md.
## Rules
- Theory only. Run no numerical simulations; sympy checks of ≤ 2 min are fine. Put the checks in
  /home/user/dmdd-solid/code/WP7-E/checks.py, and they must pass.
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py, fetching into
  /home/user/dmdd-solid/literature/papers-WP7-E/. Verify every arXiv ID against the API. Delete the PDFs at the end.
- Write /home/user/dmdd-solid/returns/R10/WP7-E.md (≤ 550 lines). End with three sections: "Symbols introduced/used" (against
  NOTATION), "Interface flags" and "Proposed LIMITS rows".
- Do not edit any other file. Do not commit.
- Your final message is a summary of ≤ 15 lines.
