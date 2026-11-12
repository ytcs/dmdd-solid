# PBE silicon rerun (worked example we:E-si-bands, Sect. 23 / E-1.tex)

QE 7.6 (conda-forge), SG15 Si_ONCV_PBE-1.2, 60/240 Ry, Gamma-centred 12^3, fixed occupations, conv_thr 1e-12.
`run.py` = vc-relax + scf + bands along Gamma-X (step 0.005 x 2pi/a); `fine.py` = step 0.002 near the CBM.
`eigs_xml.txt` = full-precision eigenvalues from the XML data files (the printed ones are rounded to 0.1 meV,
which spoils parabola fits over +-0.02 x 2pi/a by ~1.5 %).

| quantity | book | rerun |
|---|---|---|
| relaxed a | 5.477 A | 5.4773 A |
| indirect gap | 0.602 eV | 0.6021 eV |
| k_c | (0.840 +- 0.003) 2pi/a | 0.840 (fine scan parabola: 0.839) |
| direct gap at Gamma | 2.55 eV | 2.549 eV |
| gap at 5.431 A, 40 Ry | 0.557 eV | 0.5574 eV |
| m_par, 9 / 13 / 17 pts (XML) | 0.955 / 0.958 / 0.951 | 0.953 / 0.954 / 0.955 |
| m_par, fine scan 9 / 13 / 17 pts | - | 0.956 / 0.956 / 0.956 |

All values reproduce except the third digit of the three mass fits; the stated conclusion
(m_par = 0.95 m_e, spread below 1 %, 4 % above the measured 0.92 m_e) holds.
