"""Worked example 10.2 of Sect. 10.2 (the f-sum bound on the silicon rate at m_chi = 1 MeV) and the numbers of the
subsection on sum-rule bounds.  Prints every number quoted there and asserts the key ones.

Bound (Sect. 10.2, eq:10.2-Kn and eq:10.2-bound; Barker et al. arXiv:2608.05282 Eqs. (5)-(9)):
  R <= C int dq q^3 F^2 eta_n^max(q) K_n(q),   K_n <= (pi/2) omega_p^(n+1) [1 - 1/eps(q,0)]^((1-n)/2),  -1 <= n <= 1,
  eta_n^max(q) = max_{omega_th <= omega <= q v_max} omega^(-n) eta(v_min).
Inputs: rate10_2.py; static step 1 - 1/eps(q,0) from the RPA + LF table (valence electrons only, a stated limitation);
  omega_p = 31.1 eV with all 14 electrons per atom (Sect. 4.3); 16.6 eV valence for comparison.
Below the first momentum of the table (0.49 keV) the step is held at its value there (kinematics at 1 MeV starts at
  q_min = E_g / v_max = 0.42 keV).
"""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rate10_2 as R

d = R.load()
m = 1e6
light = False
wth = R.EG
qmin = wth / R.VMAX
qmax = 2 * m * R.VMAX
qg = np.linspace(qmin * 1.0001, qmax * 0.9999, 1500)
step = np.interp(qg, d["q"], d["step_lf"])
C = R.coeff(m)
conv = R.to_per_kg_yr(1.0)


def bound(n, wp=R.WP_ALL, stp=None):
    s = step if stp is None else stp
    K = np.pi / 2 * wp**(n + 1) * s**((1 - n) / 2)
    return conv * C * np.trapezoid(qg**3 * R.fdm2(qg, light) * R.eta_max(qg, m, n, wth) * K, qg)


R_lf = R.total(m, "lf", d, light)
R_rpa = R.total(m, "rpa", d, light)
R_ip = R.total(m, "ip", d, light)
b1 = bound(1)
b1v = bound(1, wp=R.WP_VAL)
b0 = bound(0)
bm1 = bound(-1)
bm1c = bound(-1, stp=np.ones_like(qg))
print("m_chi = 1 MeV, heavy mediator, sigma_e = 1e-37 cm^2, threshold E_g, rho_chi = 0.3 GeV/cm^3")
print("  kinematic window: q from %.2f to %.2f keV; omega_max = m v_max^2/2 = %.2f eV" % (qmin / 1e3, qmax / 1e3,
                                                                                        m * R.VMAX**2 / 2))
print("  computed: RPA+LF %.2f, RPA %.2f, IP %.1f  events/kg/yr" % (R_lf, R_rpa, R_ip))
print("  bounds:   n=+1 (omega_p 31.1) %.3g; n=+1 (16.6, not a bound) %.3g; n=0 %.3g; n=-1 (step) %.3g; "
      "n=-1 (step->1) %.3g" % (b1, b1v, b0, bm1, bm1c))
print("  ratios bound/computed(RPA+LF): n=+1 %.0f, n=0 %.1f, n=-1 %.2f, n=-1 cons %.2f" % (b1 / R_lf, b0 / R_lf,
                                                                                       bm1 / R_lf, bm1c / R_lf))
print("  IP rate / n=-1 bound = %.2f ; IP / conservative n=-1 bound = %.2f" % (R_ip / bm1, R_ip / bm1c))
# eta_n^max at a typical q and the location of the maximum for n = +1
qq = 2000.0
for n in (1, 0, -1):
    print("  eta_%+d^max(2 keV) = %.4g" % (n, R.eta_max(np.array([qq]), m, n, wth)[0]))
w = np.geomspace(wth, qq * R.VMAX - qq**2 / (2 * m), 4000)
print("  at q = 2 keV the n=+1 maximum of eta/omega sits at omega = %.2f eV (the threshold)" %
      w[np.argmax(R.eta(w / qq + qq / (2 * m)) / w)])
print("  static step at 0.5, 1, 2, 3.7, 5 keV: " + ", ".join("%.2f" % np.interp(x, d["q"], d["step_lf"])
                                                        for x in (500, 1000, 2000, R.Q0, 5000)))

# 10 MeV for comparison (one sentence in the text)
for mm in (10e6,):
    qg2 = np.linspace(wth / R.VMAX * 1.0001, min(2 * mm * R.VMAX, d["q"][-1]) * 0.9999, 1500)
    st2 = np.interp(qg2, d["q"], d["step_lf"])
    C2 = R.coeff(mm)
    out = {}
    for n in (1, -1):
        K = np.pi / 2 * R.WP_ALL**(n + 1) * st2**((1 - n) / 2)
        out[n] = conv * C2 * np.trapezoid(qg2**3 * R.eta_max(qg2, mm, n, wth) * K, qg2)
    Rl = R.total(mm, "lf", d, False)
    print("m = 10 MeV heavy (q <= 22.5 keV): computed %.3g; n=+1 bound %.3g (x%.0f); n=-1 bound %.3g (x%.1f)"
          % (Rl, out[1], out[1] / Rl, out[-1], out[-1] / Rl))

assert bm1 > R_lf and b0 > R_lf and b1 > R_lf
assert abs(R.OMEGA_PE - 0.513) < 0.002
