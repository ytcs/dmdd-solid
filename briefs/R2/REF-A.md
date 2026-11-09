# Round R2, referee brief REF-A (hostile)

## Your role
You are a hostile referee. Find the errors. Do not be helpful, do not polish, and do not propose new
physics beyond what is needed to state a correction.

## Material under review
Two returns claim to be independent derivations of the same result, the one-phonon-assisted DM–electron
scattering rate in crystals:
- /home/user/dmdd-solid/returns/R1/D1.md (golden-rule route), with scripts in /home/user/dmdd-solid/code/D1/;
- /home/user/dmdd-solid/returns/R1/D2.md (Kubo/diagram route), with scripts in /home/user/dmdd-solid/code/D2/.

## Read only
These two returns and their scripts, plus /home/user/dmdd-solid/STATEMENT.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/CONTROLS.md and /home/user/dmdd-solid/DONE.md.
Do NOT read referees/, state/, literature/ or other briefs. You may use your own knowledge and standard
textbooks. Do not web-search for this specific process. Run no numerical simulations; sympy or algebra
checks of ≤ 2 min are allowed.

## Rubric
DONE.md rung 4, plus the following items:
1. Verify the claimed term-by-term agreement of D1 eq. (1)–(4) with D2 eq. (2.1)–(2.2), including all
   factors of N, Ω, 2π, spin and α versus e².
2. The Pauli/exchange theorem (unrestricted band sum on shell): is it right, including the fermion signs and
   the on-shell substitution? Does it fail off shell in a way that affects anything claimed?
3. The f-sum rule / Debye–Waller claims. D2 says the Allen–Heine DW tadpole adds nothing to the first moment
   and the compensation comes from the Fan/vertex non-phonon cuts. D1 says the DW reduction of the zero-phonon
   weight compensates. Who is right, or are they saying the same thing?
4. The C7 limit. D1 has i ℓ_Q (û·q) ρ_cv; D2 has i u^{zp}·(q − m_eΔv) ρ_cv. Which is correct? Derive it.
5. Screening. Is "DFPT-screened g inside, plus one external 1/ε(q,ω), with static-lattice ε₁" correct, with no
   double screening? Check the conditions (ω ≫ ω_LO, ε₂ ≪ ε₁, O(g²)).
6. The adiabatic claim (D1 §4): standard DFPT gives only path B. Check it.
7. The resonance / well-definedness prescription, and the claim of no interference with the zero-phonon line
   at O(g²).
8. D2's claim that the C8 decoy may fail for GaAs under DM kinematics: is the argument sound as stated?
9. Optical limit C1: check that the reduction to the velocity-form phonon-assisted optical ε₂ is correct,
   including the length/velocity gauge and the nonlocal-commutator issue.
10. The recipe (D1 §7): is the Wannier tensor F_ij(R,q) route correct for keV-scale q, including Umklapp?
    Is anything missing (e.g. PAW augmentation, nonlocal pseudopotentials in the density vertex)?

## Output
Write /home/user/dmdd-solid/referees/R2/REF-A.md (≤ 300 lines). Start with a verdict table, one row per claim: STANDS / STANDS
WITH CORRECTION / FALLS, plus a one-line reason. Then give the detailed arguments, each with an explicit
derivation. Your final message is a summary of ≤ 15 lines.
