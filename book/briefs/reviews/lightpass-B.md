# Light pass, part B: Chapters 13–22
Read briefs/reviews/lightpass-common.md first; it binds you. Scope: tex/ch13–ch22 and their figscripts. Items:
1. 14.2: X_αβ → the book's strain symbol (NOTATION).
2. Ch15: Al speeds 6.47/3.40 km/s are [100] values → the book's 0 K isotropic 6.63/3.30 km/s, or say [100] if direction matters. s16-8 l.~51 caption: Al 3.40 km/s and 2.73 g/cm³ → 3.30 km/s and 2.70 g/cm³.
3. Fig. 15.3b and Ch17 "up to 11.5 meV": they use the bare spin-current form. With 1/(1+λ) the crossing is 10.9 meV, as 15.4 states. Fix the Ch17 text, and rerun the Fig. 15.3b script with the 1/(1+λ) factor if the figure plots the bare form.
4. s16-1 l.~15: ZrTe₅ pair cost 31 → 23.6 meV (half-gap 11.8). Ch16 minimum mass 9 vs 9.5 keV: align with the accepted value.
5. 17.1: the "tables' gap 1.11 eV" aligned with Ch18/Ch21; part A does 10.2 and 10.9.
6. 21.7: the Fermi-function wording, per ledgers/REVIEWS/ch22/revision.md (Hayen Eq. 6, point-charge F₀ with prefactor 4, evaluated at r_A).
7. 22.2 l.~56: (Zα)² xenon 0.13 → 0.155.
8. Ge phonon-assisted edges (DC-4): Ch13 and 22.1 quote 0.2119–0.2141 MeV; DC-4 gives 0.21380 (continuum) and 0.21264 MeV (replica), safe to ≤ 0.0003 MeV under INS scaling. Bring the quoted window into agreement, or show the two are the same quantity, and quote TA frequencies only with their softness stated.
9. ledgers/SEAMS/18.3.md: 0.015 → 0.008 (the tex governs).
10. Acronyms whose first book-wide use is in Ch13–22: expand them there (list in figscripts/appB/gen_B3.log; expansions in gen_B3.py). Part A handles first uses in Ch1–12.
11. DC-RESULTS sweep for Ch13–22 (common rules). In particular: DC-93 CsI measured C_ij (Ch17/Ch21 ranking text: FOM ≈ 3.7–3.9 by rescaling, quoted with ≈); DC-41 ℓ_mfp scope wherever the conserving edge response is quoted; DC-67 (Si ε 3.7468, F 0.11398; no library tables; tail law C/x); DC-91 ω_max and partial sound speeds where Ch17 or Ch21 quote them for C, 3C-SiC, LiF or NaF.
