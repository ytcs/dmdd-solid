# DC-2 replacement route: DFT+α pre-registration (written before any run, 2026-11-05)

Method change, not a fix: the spec's HSE06 route failed its control (returns/R18/DC-2.md). DFT+α (Abdurrazaq et al., arXiv:2512.08857v1, unrefereed preprint, fit without SOC) is semi-empirical.

Stage 1, feasibility (stop if it fails): stock QE 7.6, PBE + noncollinear SOC, a_exp 5.658 Å, a shift on Ge 4s-like states via the HUBBARD card. No custom projector. If stock QE cannot do this with SOC, stop: a custom projector is INF-level work.

Stage 2, fit: one parameter α, tuned to E_g(L) = 0.744 and E_g(Γ) = 0.89 eV.
Fit criterion: both within ±0.05 eV at one α, with L below Γ. One parameter against two numbers: failure to reach both is a possible and reportable outcome.

Stage 3, tests that α was NOT fitted to:
- T1: Δ_SO at Γ₈–Γ₇ valence = 0.29 ± 0.03 eV (measured 0.29).
- T2: X₁c above VBM = 0.87 ± 0.08 eV (measured ≈ 0.85–0.90).
If T1 or T2 fails, the bands may not be used for the Ge window, however good the fit.

Stage 4, only if all pass: Wannier bands (direct 512-k nscf, 16 spinor sp³ WFs as COMP-PH §6.2), then E_min^ZPL(q) with code/COMP-PH/emin.py and phwin.py on DC-4 force constants. Results carry the tag [CALC, semi-empirical α] in the same sentence as any number.

Not allowed: tuning a second parameter, valley-selective scissors, HSE mixing changes.

## Amendment 1 (written after the α scan at k 4³, 60 Ry; before any Δ-line calculation)
Scan result: at α = 1.0, Γ 0.911, L 0.746, Δ_SO 0.295, X 1.013. Fit passes. T1 passes (Δ_SO barely depends on α, so it is a weak test). **T2 as written FAILS: X 1.013 vs 0.87 ± 0.08.**
Suspected defect in T2: the measured 0.85–0.90 eV is, as far as I recall, the Δ-valley minimum near X, not the X point. Not verified when writing this.
T2 stays recorded as failed. New test T2′, fixed now: Δ-line conduction minimum (k along Γ–X, scan 0.70–1.00 X) = 0.87 ± 0.08 eV above VBM, at the converged α. The target value must be confirmed from a source before scoring T2′. Convergence: repeat at k 8³, 80 Ry; retune α there only in the fit sense of stage 2.

## Score (k 8³, 80 Ry, PseudoDojo FR PBE standard, stock QE 7.6, α = 1.0 eV on Ge-4s, ortho-atomic)
Fit PASS: L 0.749, Γ 0.918, Γ − L = +0.169. T1 PASS, weak: Δ_SO 0.295 (independent of α). T2 as written FAILED: X 1.014. T2′ PASS: Δ minimum 0.826 at 0.80 X, inside 0.87 ± 0.08, but ≈ 0.1 eV below 0.92 eV implied by L + 0.18 (arXiv:1010.0961); treat the Δ valley as possibly low by that much.
Paper's α = 1.4 does not transfer: its projector differs from stock ortho-atomic (at α = 1.4 here Γ 1.30, L 1.02).

## Amendment 2 (decision by the user's stand-in; written before any mass was extracted)
DFT+α is accepted as a separate item (DC-2-alpha), not a DC-2 close: DC-2 as specified is CLOSED, FAILED-CONTROL. Parameter-free Ge bands still need GW (INF-1).
New test T3, the one that matters for E_min^ZPL(q), from the Wannier bands: m_l = 1.59 ± 0.15, m_t = 0.082 ± 0.010, Γ mass 0.038 ± 0.005 m_e, and these should barely move with α. If T3 fails, the route fails for the Ge window whatever the gap fit.
Also: identify the state called the Γ CBM (Γ₂′ s-like, not Γ₁₅). Spread should be near the PBE+SOC value (29 Å²). Wannier CBM residual within ±5 meV. Hostile referee before VALIDATED. Tag [CALC, semi-empirical α], with the fit and the independent checks stated in the same sentence as any Ge window number. Report the Δ tension as is; no second parameter.

## Final score: route FAILS (T3)
See returns/R18/DC-2-alpha.md. No further stages run.
