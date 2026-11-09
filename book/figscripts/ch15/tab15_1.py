"""Numbers of Sect. 15.1 that are not in a figure: aluminum scales, checks of the closed forms, and the loss-function
ratios at the kinematic edge q = omega/v_max.  Inputs and hypotheses: bcs15.py (docstring).  Output: tab15_1.log.
Run time a few seconds.
"""
import os
import numpy as np
import bcs15 as b

out = []


def pr(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


pr("== Aluminum scales ==")
pr(f"n_e = {b.NE_AL / (b.HBARC**3) * 1e24:.4e} cm^-3 (12 electrons per cube of a = 4.05 A)")
pr(f"k_F = {b.KF_AL:.1f} eV ; E_F(free) = {b.KF_AL**2 / 2 / b.ME:.2f} eV ; v_F(free) = {b.KF_AL / b.ME:.4e}"
   f" (book value v_F = {b.VF})")
pr(f"k_TF = {b.KTF_AL:.0f} eV")
pr(f"v_max = {b.VMAX:.4e} ; v_max/v_F = {b.XMAX:.4f} ; v_max/(2 v_F) = {b.XMAX / 2:.4f}")
cLA = b.alc.C_LA
pr(f"c_LA = sqrt(C11/rho) (0 K C11 = 114.3 GPa) = {cLA * 299792.458:.2f} km/s = {cLA:.3e} ; c_LA/v_max = {cLA / b.VMAX:.4f}")
for D, lab in ((b.DELTA_BULK, "bulk"), (b.DELTA_FILM, "film")):
    pr(f"{lab}: Delta = {D * 1e3:.2f} meV, 2Delta = {2 * D * 1e3:.2f} meV, m_min = 2(2Delta)/v_max^2 = "
       f"{4 * D / b.VMAX**2 / 1e3:.3f} keV, q_min(2Delta) = 2Delta/v_max = {2 * D / b.VMAX:.3f} eV, "
       f"coherence length v_F/(pi Delta) = {b.VF / (np.pi * D) * b.HBARC * 1e-4:.2f} um")
pr(f"ratio film/bulk Delta = {b.DELTA_FILM / b.DELTA_BULK:.3f}")
m = 1e3
pr(f"m_chi = 1 keV: omega_max = m v_max^2/2 = {0.5 * m * b.VMAX**2 * 1e3:.3f} meV ; q_max = 2 m v_max = "
   f"{2 * m * b.VMAX:.3f} eV ; q_max/k_TF = {2 * m * b.VMAX / b.KTF_AL:.2e}")
pr(f"  y_max (bulk) = {0.5 * m * b.VMAX**2 / b.DELTA_BULK:.2f} ; y_max (film) = {0.5 * m * b.VMAX**2 / b.DELTA_FILM:.2f}")
pr(f"  Q_max (bulk) = {2 * m * b.VMAX * b.VF / b.DELTA_BULK:.1f}")
# smallest momentum transfer that deposits omega, in units of the kinematic edge omega/v_max:
#   q_min/(omega/v_max) = (2/x)(1 - sqrt(1 - x)), x = 2 omega/(m v_max^2)  (from v_min(q, omega) = v_max)
for mm in (4 * b.DELTA_BULK / b.VMAX**2, 2 * 4 * b.DELTA_BULK / b.VMAX**2, 1e3, 1e4):
    xk = 2 * 2 * b.DELTA_BULK / (mm * b.VMAX**2)
    pr(f"  omega = 2 Delta, m_chi = {mm:.0f} eV ({mm / (4 * b.DELTA_BULK / b.VMAX**2):.1f} m_min): q_min/(omega/v_max) = "
       f"{(2 / xk) * (1 - np.sqrt(1 - xk)):.3f}")

pr("\n== Checks of the closed forms ==")
for y in (2.0001, 2.2, 2.5, 3.0, 4.0, 5.0, 10.0, 100.0):
    pr(f"g_I({y}) closed = {float(b.gI(y)):.6f} ; integral = {b.gI_int(y):.6f}")
pr(f"pi/2 = {np.pi / 2:.6f}")
for y in (2.2, 3.0, 5.0):
    Q = y / b.XMAX
    pb, pc = b.P_resp(y, Q, n=16)
    pn = b.P_nor(y, Q)
    pr(f"Im P_bare/Im P_nor at y={y}, Q={Q:.3f}: {pb.imag / pn.imag:.8f} vs g_I = {float(b.gI(y)):.8f}")
for Q in (1e-2, 1e-1):
    pb, pc = b.P_resp(2.5, Q, n=16)
    pr(f"q -> 0 cancellation y=2.5, Q={Q}: |P_cons| = {abs(pc):.3e}, |P_bare| = {abs(pb):.3e}, "
       f"P_cons/(Q^2/3y^2) = {pc.real / (Q * Q / (3 * 6.25)):.5f}")
pb, pc = b.P_resp(1e-6, 5.0, n=16)
pr(f"omega -> 0 (y = 1e-6, Q = 5): P_bare = {pb.real:.6f}, P_cons = {pc.real:.6f} (static value -1)")
import mpmath as mp
mp.mp.dps = 30


def _Fmp(p):
    if p > 1:
        return (mp.acosh(mp.sqrt(p)) - 1j * mp.pi / 2) / mp.sqrt(p * (p - 1))
    if p > 0:
        return -mp.asin(mp.sqrt(p)) / mp.sqrt(p * (1 - p))
    return -mp.asinh(mp.sqrt(-p)) / mp.sqrt(-p * (1 - p))


def resp_mp(y, Q):
    """(P_bare, P_cons) by tanh-sinh quadrature in p = (y^2 - s^2)/4 with breakpoints at p = 0 and 1 (30 digits);
    the Gauss-Legendre sums of bcs15.P_resp reach a floor near 1e-5 at Q = 1e4."""
    pmax, pmin = y * y / 4, (y * y - Q * Q) / 4
    pts = [pmin] + [t for t in (0, 1) if pmin < t < pmax] + [pmax]
    w = lambda p: 2 / (mp.sqrt(y * y - 4 * p) * Q)
    C = mp.quad(lambda p: w(p) * (-_Fmp(p) - 1) / p, pts)
    Fa = mp.quad(lambda p: w(p) * _Fmp(p), pts)
    PF = mp.quad(lambda p: w(p) * p * _Fmp(p), pts)
    pb = -1 - y * y / 4 * C
    return pb, pb - y * y / 4 * Fa**2 / PF


xm = mp.mpf(b.VMAX) / mp.mpf(b.VF)
for Q in (1e3, 1e4):
    pb, pc = resp_mp(xm * Q, Q)
    pn = -1 + xm / 2 * mp.log((1 + xm) / (1 - xm)) - 1j * mp.pi / 2 * xm
    pr(f"Delta -> 0 at x = v_max/v_F = {float(xm):.4f}, Q = {Q:.0e}: |P_cons - P_nor|/|P_nor| = "
       f"{float(abs(pc - pn) / abs(pn)):.2e} (mpmath)")

pr("\n== First-order Kramers-Kronig function s_BCS(y) ==")
for y in (0.0, 2.2, 2.5, 3.0, 5.0, 10.0, 20.0):
    pr(f"s_BCS({y}) = {b.s_bcs(y) if y > 0 else b.s_bcs(1e-6):.4f}")
for y in (20.0, 50.0, 100.0):
    pr(f"y s_BCS(y) at y = {y}: {y * b.s_bcs(y):.4f} ; pi^2/2 = {np.pi**2 / 2:.4f} ; pi^2/(2y) = {np.pi**2/(2*y):.4f}")

pr("\n== Loss-function ratios at the kinematic edge q = omega/v_max (bulk Delta) ==")
pr("y      Q       g_I    v_frac   Lb/(gI Ln)  Lc/(gI Ln)  Lc/Ln   Lc/Lb   s_BCS   1-2 s_BCS/Q  2 s_BCS/Q")
rows = {}
for y in (2.05, 2.2, 2.5, 3.0, 4.0, 5.0, 7.0, 10.0):
    Q = y / b.XMAX
    pb, pc = b.P_resp(y, Q, n=16)
    pn = b.P_nor(y, Q)
    D = b.DELTA_BULK
    Lb, Lc, Ln = b.loss(pb, Q, D), b.loss(pc, Q, D), b.loss(pn, Q, D)
    g = float(b.gI(y))
    v = (pc.imag - pb.imag) / pb.imag
    s = b.s_bcs(y)
    rows[y] = (Lb / (g * Ln), Lc / (g * Ln))
    pr(f"{y:<6} {Q:<7.3f} {g:.4f} {v:+.4f}  {Lb / (g * Ln):.4f}      {Lc / (g * Ln):.4f}      {Lc / Ln:.4f}  "
       f"{Lc / Lb:.4f}  {s:.4f}  {1 - 2 * s / Q:.4f}       {2 * s / Q:.4f}")

pr("\n== Same at four and sixteen times the edge momentum ==")
for fac in (4.0, 16.0):
    for y in (2.2, 3.0, 5.0, 10.0):
        Q = fac * y / b.XMAX
        pb, pc = b.P_resp(y, Q, n=16)
        pn = b.P_nor(y, Q)
        D = b.DELTA_BULK
        Lb, Lc, Ln = b.loss(pb, Q, D), b.loss(pc, Q, D), b.loss(pn, Q, D)
        g = float(b.gI(y))
        v = (pc.imag - pb.imag) / pb.imag
        s = b.s_bcs(y)
        pr(f"x{fac:<4.0f} y={y:<5} Q={Q:<8.2f} v_frac={v:+.4f} Lb/(gI Ln)={Lb / (g * Ln):.4f} "
           f"Lc/(gI Ln)={Lc / (g * Ln):.4f} 1-2s/Q={1 - 2 * s / Q:.4f}")

pr("\n== Threshold: L/L_nor at Q = 2.05/x_max (edge momentum of y = 2.05) ==")
Q = 2.05 / b.XMAX
for dy in (1e-9, 1e-6, 1e-4, 1e-3, 1e-2, 0.03, 0.1):
    y = 2 + dy
    pb, pc = b.P_resp(y, Q, n=24)
    pn = b.P_nor(y, Q)
    D = b.DELTA_BULK
    Lb, Lc, Ln = b.loss(pb, Q, D), b.loss(pc, Q, D), b.loss(pn, Q, D)
    pr(f"y-2 = {dy:.0e}: Im P_cons/Im P_nor = {pc.imag / pn.imag:.4f} ; Im P_bare/Im P_nor = {pb.imag / pn.imag:.4f} ;"
       f" Lc/Ln = {Lc / Ln:.4f} ; Lb/Ln = {Lb / Ln:.4f}")
pr(f"0.03 Delta = {0.03 * b.DELTA_BULK * 1e6:.1f} ueV")


out2 = []
pr("\n== Scan over all momenta reached by halo dark matter (Q from the edge y/x_max to 1e3): L_cons/(g_I L_nor) ==")
for ymin in (2.5, 3.0):
    lo, hi = 9, 0
    blo, bhi = 9, 0
    for y in np.geomspace(ymin, 50, 30):
        for Q in np.geomspace(y / b.XMAX, 1e3, 40):
            pb, pc = b.P_resp(y, Q, n=16)
            pn = b.P_nor(y, Q)
            D = b.DELTA_BULK
            r = b.loss(pc, Q, D) / (float(b.gI(y)) * b.loss(pn, Q, D))
            rb = b.loss(pb, Q, D) / b.loss(pc, Q, D)
            lo, hi = min(lo, r), max(hi, r)
            blo, bhi = min(blo, rb), max(bhi, rb)
    pr(f"y >= {ymin}: L_cons/(g_I L_nor) in [{lo:.4f}, {hi:.4f}] ; L_bare/L_cons in [{blo:.4f}, {bhi:.4f}]")
pr(f"v_F/Delta_BCS (bulk) = {b.VF / b.DELTA_BULK * b.HBARC * 1e-4:.2f} um")
mm = 2 * b.DELTA_BULK / (2 * cLA * b.VMAX)
pr(f"mass below which c_LA q_max = 2 c_LA m v_max < 2 Delta (bulk): {mm / 1e3:.2f} keV")
pr(f"(c_LA/v_max)^2 = {(cLA / b.VMAX)**2:.2e}")
pr(f"beta*2Delta at 10 mK: {2 * b.DELTA_BULK / (8.617333e-5 * 0.010):.0f}")
pr(f"Delta/T at 10 mK: {b.DELTA_BULK / (8.617333e-5 * 0.010):.1f} (thermal weight e^-Delta/T)")
pr(f"Delta/E_F = {b.DELTA_BULK / b.EF_AL:.2e}")
with open(os.path.join(b.HERE, "tab15_1.log"), "w") as f:
    f.write("\n".join(out) + "\n")

pr("\n== Further checks ==")
ss = [b.s_bcs(y) for y in np.concatenate([np.linspace(0.1, 1.95, 20), np.linspace(2.05, 50, 60)])]
pr(f"s_BCS on 0.1 <= y <= 50 (80 points): min = {min(ss):.4f}, all positive: {min(ss) > 0}")
for y in (5.0, 10.0, 20.0):
    pr(f"g_I({y}) - 1 = {float(b.gI(y)) - 1:.4f} ; (2 ln 2y - 1)/y^2 = {(2*np.log(2*y)-1)/y**2:.4f}")
for Q in (1e2, 1e3, 1e4, 1e5):
    y = 5.0
    pb, pc = b.P_resp(y, Q, n=24)
    pn = b.P_nor(y, Q)
    pr(f"y = 5, Q = {Q:.0e}: Q[Re(-P) - Re(-P_nor)] bare = {Q*(-pb.real + pn.real):.4f}, cons = {Q*(-pc.real + pn.real):.4f}"
       f" (s_BCS(5) = 1.0529)")
pr(f"(k_TF/q_max)^2 at q_max = 5.3 eV: {(b.KTF_AL/5.3)**2:.2e}")
pr(f"(Delta/qv_F)^2 at the edge of y = 5: {(b.XMAX/5)**2:.4f}")
with open(os.path.join(b.HERE, "tab15_1.log"), "w") as f:
    f.write("\n".join(out) + "\n")
