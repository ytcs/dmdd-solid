# R16 revision brief REV-GAP-EF: GAP-EF v2

## Target
Produce /home/user/dmdd-solid/returns/R16/GAP-EF-v2.md: a standalone, corrected version of returns/R14/GAP-EF.md that absorbs every item of referees/R14/REF-GAP-EF-A.md (K1–K14) and REF-GAP-EF-B.md. The v1 return stays untouched as the record. Priority (user directive): §1, the derivation of ε_eh and F_eh, must read as a textbook passage, with hypotheses, steps, limits and leading corrections.

## Required
1. Fix every FALLS item: the final-state (renewal) model is a **lower bound** on F_eh in every computed case; fix the random-parking sentence sign, and withdraw or replace LIMITS row L41.
2. Apply each STANDS-WITH-CORRECTION item:
   - Klein's overstatement is 36–39%;
   - R&K agreement is at their MC scatter (~2%), not 0.5%;
   - the plasmon claim is UNRESOLVED;
   - F_Si = 0.114 is an untuned model value equal to R&K's, nearly 𝒜_ph-independent, and 2.6σ below 0.119; say so plainly;
   - "observed" fit language is not "derived" or "predicts", and k₂ spans 1.2–2.3 eV;
   - GaN 8.9 eV is not a named measurement, so use EBIC 9.59 or exclude it and restate the rms;
   - 4H-SiC: correct the "ab initio does better" list, confront the F ≤ 0.04 limit (the model gives ≥ 0.051), and handle the measured tension openly;
   - β-Ga₂O₃: include it or justify the exclusion;
   - fix the CsI phonon-energy grid bug and rerun predictions;
   - (EF12) needs energy-independent capture probability;
   - make (EF13) consistent with WP5-v4 (W4′): ℋ_eff unchanged, bare heat +N_X·E_x^b, plus the extra variance;
   - fix the 0911.1532 typo (F_unc = 0.0443977) in check C2 and tighten its tolerance;
   - rename the NOTATION clashes σ_c, w₀ and Φ_t;
   - correct the L42 attribution.
3. If /home/user/dmdd-solid/returns/R16/EF-LIT.md exists when you reach validation, add any ε_eh/F_eh it found for Al₂O₃, CaWO₄, LiF, NaF to the validation set ([FT] only).
4. End with a closing table (one row per referee item → resolution → location), then 'Symbols introduced/used', 'Interface flags' (including the owed WP5 correction IF-EF1 restated), 'Proposed LIMITS rows'.

## Rules
Checks: code/GAP-EF-v2/ (copy code/GAP-EF/, fix, extend; ≤ 2 min, must pass). No first-principles numerics. Literature via skills/breakthrough-maths/scripts/lit.py into literature/papers-GAP-EF-v2/, PDFs deleted. Follow CONVENTIONS and NOTATION. Write only the return and code/GAP-EF-v2/. Do not commit. Final message ≤ 15 lines.
