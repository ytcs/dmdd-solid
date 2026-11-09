# Final consistency pass: silicon gap and silicon nuclear mass

Rules: briefs/reviews/lightpass-common.md. No symbol changed, so no NOTATION clash entry (104 unused). Build: latexmk, outdir /tmp/claude-0/build-final-cons (result at the end). Lint (skills/long-form-writing/scripts/lint.py, BANNED-TERMS.txt) on the 15 changed tex files: 83 hits, 0 blocking.

## 1. Room-temperature gap of silicon (1.11 / 1.12 eV)

How the book defines 1.11 eV: 10.2 (fig:10-screening, we:10-fsum), 10.10 (sec:10.10-gap) and 21.6 (we:21-libentry) call it the step-model gap of pair creation that accompanies the Knapen--Kozaczuk--Lin tables, whose scissor puts the gap at 1.17 eV. Computations (rate10_2.py EG = 1.11, Ch12 mig12/mom12_5, Ch18 E_g = 1.160) are unchanged.

Room temperature, 1.11 -> 1.12 eV:
- tex/ch04/s4-2.tex:82 -> "silicon gap of 1.12 eV at 300 K"; e^{-beta omega} = 1.53e-19, still "2e-19" at one figure. figscripts/ch04/fig4_2.py:100 assert updated to 1.12 eV, 1.53e-19; reran, passes.
- tex/ch04/s4-4.tex:101 (fig:4-siloss caption) -> "room-temperature gap, 1.12 eV". figscripts/ch04/fig4_5.py:11 (docstring) and :208 (marker axvline 1.12); reran, fig4_5.pdf regenerated.
- tex/ch04/s4-7.tex:121 -> "(1.12 eV at 300 K; app:E.1)".
- tex/ch04/s4-2.tex:134 -> "its gap removes all weight below 1.17 eV". Neither room temperature nor a table threshold (free-gas worked example vs real silicon); set to the book's detector gap (3.3: "the book uses 1.17 eV"). Editor may prefer 1.12 eV at 300 K.

Table threshold, wording only (text called 1.11 eV the tables' scissor gap, which contradicts 10.10 and 21.6):
- tex/ch10/s10-3.tex:17 "the gap that the tables fix by a scissor shift; the physical gap at low temperature is 1.17 eV" -> "the step-model gap that accompanies the tables; their scissor puts the gap at the physical low-temperature value, 1.17 eV".
- tex/ch10/s10-5.tex:102 "(scissor gap 1.11 eV;" -> "(threshold 1.11 eV, the step-model gap that accompanies them;".
- tex/ch12/s12-1.tex:78, tex/ch12/s12-4.tex:86 "(scissor gap 1.11 eV," -> "(threshold 1.11 eV, the step-model gap that accompanies the tables,".
- tex/ch12/s12-3.tex:46 "which puts the gap at the scissor value 1.11 eV instead of the physical 1.17 eV and stops at" -> "counted from 1.11 eV, the step-model gap that accompanies it, rather than from its scissor gap, the physical 1.17 eV; the table stops at".
- tex/ch12/s12-3.tex:72 "(scissor gap 1.11 eV," -> "(threshold 1.11 eV, the step-model gap that accompanies them,"; :126 "scissor gap 1.11 eV)" -> "threshold 1.11 eV, the step-model gap that accompanies the tables)".
- tex/ch12/s12-5.tex:143 "the table's scissor gap" -> "the step-model gap that accompanies the table".

Checked, already correct, left: ch10 s10-1:61/65/68 and ch21 s21-1:80 (Essig et al. tables, whose scissor really is 1.11 eV); ch10 s10-2, s10-4, s10-9, s10-10; ch17 s17-1, s17-3, s17-5; ch21 s21-6; ch01 s1-3:72, ch02 s2-2:61, ch03 s3-3:24, ch18 s18-3:52 (1.11 eV named as the projection / step-model value); ch13 s13-2:115 (1.17 - 0.064), s13-8:58 (an energy distance); ch21 s21-7:77 (a ratio); appF F-rows (already "1.11 eV of the tables"); every 1.12 eV (all 300 K) and 1.17 eV. Ch18 E_g = 1.160 untouched.
Not touched: Ch12 figscript comments that still say "scissor gap 1.11 eV" (fig12_1/3/4.py, limit12_3a.py, mig12.py, mom12_5.py, we12_4.py); comments only, nothing printed.

## 2. Silicon nuclear mass (26.06 -> 26.16 GeV, natural silicon)

No passage that used 26.06 GeV treats 28Si as an isotope (ch11 s11-6 and ch20 s20-2 do, and use isotope masses; untouched). All moves are last-digit.
- tex/ch01/s1-3.tex:91 (fig:1-kinematics caption), :97 (tab:1-kinematics caption) -> "M = 26.16 GeV, the mean atomic mass of natural silicon". Table entries unchanged at quoted precision (5.4 ueV, 0.54 meV, 54 meV, 5.3 eV, 0.50 keV); 47 MeV unchanged (46.77).
- tex/ch01/s1-3.tex:147 -> natural silicon, mu = (1 x 26.16/27.16) GeV = 0.963 GeV; :149 -> 2 x 26160 MeV; q = 5.10 MeV, E_R = 0.50 keV, 0.142 unchanged.
- tex/ch01/s1-4.tex:114 -> "the mean atomic mass of natural silicon, 26.16 GeV"; 99.6 MeV, 1.215, 953, 3.96, 3100 unchanged.
- figscripts/ch01/fig1_5.py:37 M_SI = 28.0855 u; reran, fig1_5.pdf regenerated.
- tex/ch05/s5-1.tex:139 "For 28Si, M = 26.06 GeV, m_e/M = 1.961e-5" -> "For natural silicon, M = 26.16 GeV, m_e/M = 1.953e-5"; :141 kappa^2 4.43e-3 -> 4.42e-3, kappa^3 2.95e-4 -> 2.94e-4 (kappa 0.0665, kappa a0 0.0352 A, 0.120 eV, 0.53 and 12.4 kappa^2 unchanged). figscripts/ch05/fig5_1.py:7, :37, :41 use MNAT; reran, fig5_1.pdf regenerated. figscripts/ch05/we5_4.py:101-105 bond coordinate with natural mass: 0.0484 -> 0.0483 A, text "0.048 A" unchanged.
- tex/ch06/s6-1.tex:3 v_N 1.96e-4 -> 1.95e-4, 59 -> 58 km/s; :147 v_N 1.96e-4 -> 1.95e-4, 1 - P_0 7.2e-4 -> 7.1e-4 (m_e v_N 100 eV, 37 times, 2.9e-4, 91 unchanged). figscripts/ch06/fig6_1.py:18, :131, :136 natural mass; reran, passes, fig6_1.pdf regenerated.
- tex/ch08/s8-5.tex:7 "0.0665 for 28Si" -> "0.0665 for natural silicon"; :38 (tab:8-params caption) "M = 26.06 GeV (28Si)" -> "M = 26.16 GeV (natural silicon)". figscripts/ch08/tab8_4.py:5, :16, :36-37 natural mass (kappa 0.0665 unchanged; kappa^2 4.428e-3 -> 4.420e-3, not quoted in ch08).
- tex/ch08/s8-6.tex:3 v_N 1.96e-4 -> 1.95e-4 (quotes 6.1).
- figscripts/ch08/limit8_2a.py:25, :45 M = 28.0855 u; reran, output identical.
- figscripts/ch02/fig2_3.py:13, :25 natural mass; reran, fig2_3.pdf regenerated. Numbers quoted in ch02 (q_max R = 0.090, F^2 = 0.998 at 1 GeV) unchanged.
- figscripts/appD/check_D_b.py:5-6, :113, :120-121, :124-125 kappa_BO check of Sect. 5.1 on natural mass (asserts 4.42e-3, 2.94e-4; dropped the 5.10e4 assert of the 28Si ratio); reran, passes. D-13 text untouched.
- figscripts/ch03/fig3_1.py:14 comment updated (Sect. 1.3 now uses 26.16 GeV).
No 26.06 GeV remains in tex/ or in any figscript (check17.py "LiF=26.06" is a plasma frequency in eV).

Checked: tex/ch12/s12-5.tex:90 (v_N = 1.96e-4 at E_R = 500 eV, M = 26.16 GeV) is consistent, q/M = 1.9551e-4.
