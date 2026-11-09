"""Worked example 11.8 (Sect. 11.7): daily-modulation amplitude of silicon and GaAs at 45 deg N, electronic and lattice parts.
Prints every number of the example; also used by fig11_7.py and limit11_7a.py for the rate multipoles.

Set-up: m_chi = 2 MeV (so that every momentum transfer, q <= 2 m_chi v_max = 10.6 keV = 2.84 q0, lies inside the range of the
model response), heavy mediator (F_DM = 1), the book's halo (aniso11.py), latitude 45 deg N, crystal [001] along the local vertical,
[100] east, [010] north; |v_E| = 250.5 km/s with the direction of v_sun (Sect. 1.2).
Rate multipoles (eq:11.7-rate, cubic): R(t)/Rbar = 1 + sum_{l >= 4} sqrt(4 pi) (R_l/R_0) Y^c_l(vhat_E(t)), with
  electronic:  R_l = sum_omega-bins int dq q^3 Upsilon_l(v_min(q, omega)) L_l(q, omega)      (eq:10.2-rate structure, T = 0)
               L_l from the EPM head-only RPA loss function (elf11_7.py, NK = 12, ten directions, fit l = 0, 4, 6, 8);
               omega bins of 1 eV centred on 2 ... 7 eV (omega <= m v_max^2/2 = 7.0 eV); q grid 0.15 ... 2.8 q0 (the runs
               elf11_7_<MAT>_NK12.npz, q = 0.4-2.8 q0, and elf11_7_<MAT>_NK12_lowq.npz, q = 0.15, 0.25 q0), log-linear
               interpolation of L_l in q.  The l >= 10 remainder (fit residual) is estimated with |Upsilon_10| and printed.
  lattice:     R_l = sum_n int dq q Upsilon_l(q/2m) e^{-2W}(2W)^n/n! s_{n,l}(q),  2W = q^2 <u_x^2>, <u_x^2> = 2.45e-3 A^2 (WE 5.7),
               s_{1,l}, s_{2,l} from lat11_7.npz (exact coherent one- and two-phonon weights per direction), n >= 3 treated
               as isotropic (their coherent corrections are below 3 %, Sect. 11.3); threshold below the phonon band.
               v_min of order n: q/2m + n wbar_1(q)/q, wbar_1 = 1/<omega^-1> = 30.4 meV (the mean energy of P_1, Sect. 11.3) for
               q >= q_BZ and 30.4 meV x q/q_BZ below (acoustic, about 4 km/s); the run without the omega/q term is printed.
  GaAs lattice: one phonon only (gaas11_7.npz), the two-phonon weight being 3 % of it at 10 keV; omega/q dropped (in silicon
               keeping it changes R4/R0 at 2 MeV by < 1e-5); Debye-Waller factor with
               <u_x^2> = 1.9e-3 A^2, the mean of the Ga (2.0e-3) and As (1.7e-3) site values of the DarkELF tensors (lat11_7.log);
               it changes the GaAs result by < 1 % (e^{-2W} >= 0.94 for q <= 10.6 keV).
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import aniso11 as AN  # noqa: E402

C_KMS = AN.C_KMS
HBARC = 1973.269804
Q0 = 3728.94           # eV, alpha m_e
LS = (0, 4, 6, 8)


def electronic_multipoles(mat, m_chi, wbins=None, tag=""):
    """R_l for l in LS (dict), summed over omega bins up to the kinematic limit; also returns per-q contributions."""
    zs = [np.load(os.path.join(HERE, "elf11_7_%s_NK12%s.npz" % (mat, t))) for t in ("", "_lowq") if
          os.path.exists(os.path.join(HERE, "elf11_7_%s_NK12%s.npz" % (mat, t)))]
    Q = np.concatenate([z["Q"] for z in zs])
    Lall = np.concatenate([z["L"] for z in zs], axis=1)
    o = np.argsort(Q)
    Q, Lall = Q[o], Lall[:, o]
    DIRS, BIN = zs[0]["DIRS"], zs[0]["BIN"]
    c, res = AN.fit_cubic(DIRS, Lall)                 # each (nq, nbin)
    wmax = 0.5 * m_chi * (AN.VESC + AN.VE)**2 / C_KMS**2
    qf = np.geomspace(Q[0], Q[-1], 400) * Q0
    Rl = {l: 0.0 for l in LS}
    Rl["u4w"] = 0.0          # R_0-weighted Upsilon_4/Upsilon_0 (diagnostic)
    Rl["edge"] = 0.0         # share of R_0 with v_min > 600 km/s
    for ib, w in enumerate(BIN):
        if w - 0.5 > wmax or (wbins is not None and w not in wbins):
            continue
        vmin = (w / qf + qf / (2 * m_chi)) * C_KMS
        u0 = AN.upsilon(0, vmin)
        L0 = np.interp(np.log(qf / Q0), np.log(Q), c[0][:, ib])
        Rl["u4w"] += np.trapezoid(qf**3 * AN.upsilon(4, vmin) * L0, qf)
        Rl["edge"] += np.trapezoid(qf**3 * u0 * L0 * (vmin > 600), qf)
        # size of the l >= 10 remainder: |Upsilon_10| x (rms fit residual) x Lbar, relative to the l = 0 rate (Lbar = L_0 Y_00)
        rq = np.interp(np.log(qf / Q0), np.log(Q), res[:, ib])
        Rl["hi"] = Rl.get("hi", 0.0) + np.trapezoid(qf**3 * np.abs(AN.upsilon(10, vmin)) * rq * L0, qf)
        for l in LS:
            Ll = np.interp(np.log(qf / Q0), np.log(Q), c[l][:, ib])
            Rl[l] += np.trapezoid(qf**3 * AN.upsilon(l, vmin) * Ll, qf)
    return Rl, (Q, BIN, c, res)


def lattice_multipoles(m_chi, ux2=2.45e-3, wterm=True):
    z = np.load(os.path.join(HERE, "lat11_7.npz"))
    qk, s1, s2 = z["qgrid"], z["s1"], z["s2"]                    # keV; (4, nq) for l = 0, 4, 6, 8
    qmax = 2 * m_chi * (AN.VESC + AN.VE) / C_KMS / 1e3          # keV
    qf = np.geomspace(qk[0], min(qmax, qk[-1]) * 0.9999, 1500)
    x = (qf * 1e3 / HBARC)**2 * ux2                               # 2W
    w1, w2, w3 = np.exp(-x) * x, np.exp(-x) * x**2 / 2, np.exp(-x) * (np.exp(x) - 1 - x - x**2 / 2)
    qbz = float(z["qbz"])
    w1bar = 30.4e-3 * np.minimum(1.0, qf / qbz) if wterm else 0.0 * qf     # eV
    vm = {n: (qf * 1e3 / (2 * m_chi) + n * w1bar / (qf * 1e3)) * C_KMS for n in (1, 2, 3)}
    Rl = {}
    for i, l in enumerate(LS):
        a1 = np.interp(np.log(qf), np.log(qk), s1[i])
        a2 = np.interp(np.log(qf), np.log(qk), s2[i])
        a3 = np.sqrt(4 * np.pi) if l == 0 else 0.0
        Rl[l] = np.trapezoid(qf * (AN.upsilon(l, vm[1]) * w1 * a1 + AN.upsilon(l, vm[2]) * w2 * a2
                                   + AN.upsilon(l, vm[3]) * w3 * a3), qf)
    return Rl


def gaas_lattice_multipoles(m_chi, ux2=1.9e-3):
    z = np.load(os.path.join(HERE, "gaas11_7.npz"))
    qk, s = z["q"], z["s"]
    qmax = 2 * m_chi * (AN.VESC + AN.VE) / C_KMS / 1e3
    qf = np.geomspace(qk[0], min(qmax, qk[-1]) * 0.9999, 1500)
    dw = np.exp(-(qf * 1e3 / HBARC)**2 * ux2)
    Rl = {}
    for i, l in enumerate(LS):
        a = np.exp(np.interp(np.log(qf), np.log(qk), np.log(np.abs(s[0])))) if l == 0 else \
            np.interp(np.log(qf), np.log(qk), s[i] / s[0]) * np.exp(np.interp(np.log(qf), np.log(qk), np.log(np.abs(s[0]))))
        Rl[l] = np.trapezoid(qf * AN.upsilon(l, qf * 1e3 / (2 * m_chi) * C_KMS) * dw * a, qf)
    return Rl


def day_curve(Rl, lat=45.0, R=np.eye(3), nh=288):
    h = np.linspace(0, 2 * np.pi, nh, endpoint=False)
    v = AN.vhat_crystal(lat, h, R)
    r = 1 + sum(np.sqrt(4 * np.pi) * Rl[l] / Rl[0] * AN.ycub(l, v) for l in LS if l > 0)
    return h, r


def amp(r):
    return (r.max() - r.min()) / (r.max() + r.min())


def best_orientation(Rl, lat=45.0, n=3000, seed=1):
    from scipy.spatial.transform import Rotation
    Rs = Rotation.random(n, random_state=seed).as_matrix()
    a = np.array([amp(day_curve({l: Rl[l] for l in LS}, lat, R, 96)[1]) for R in Rs])
    return a.max(), Rs[a.argmax()]


if __name__ == "__main__":
    m = 2e6
    print("halo: v_max = %.1f km/s; m_chi = 2 MeV: q_max = %.2f keV = %.2f q0, omega_max = %.2f eV"
          % (AN.VESC + AN.VE, 2 * m * (AN.VESC + AN.VE) / C_KMS / 1e3, 2 * m * (AN.VESC + AN.VE) / C_KMS / Q0,
             0.5 * m * ((AN.VESC + AN.VE) / C_KMS)**2))
    out = {}
    for mat in ("Si", "GaAs"):
        if not os.path.exists(os.path.join(HERE, "elf11_7_%s_NK12.npz" % mat)):
            continue
        Rl, (Q, BIN, c, res) = electronic_multipoles(mat, m)
        h, r = day_curve(Rl)
        out[mat + "_el"] = (Rl, r)
        print("%s electronic: R_0-weighted <Ups4/Ups0> = %.4f; share of R_0 with v_min > 600 km/s = %.3f; "
              "l >= 10 remainder estimate sqrt(4 pi) |Ups10| resid Lbar / R_0 = %.1e"
              % (mat, Rl["u4w"] / Rl[0], Rl["edge"] / Rl[0], np.sqrt(4 * np.pi) * Rl["hi"] / Rl[0]))
        print("%s electronic (EPM RPA head), 2 MeV: R4/R0 = %+.5f, R6/R0 = %+.5f, R8/R0 = %+.6f; A_day(45N, [001] up) = %.4f; "
              "rate max at h = %.1f h" % (mat, Rl[4] / Rl[0], Rl[6] / Rl[0], Rl[8] / Rl[0], amp(r), h[r.argmax()] * 12 / np.pi))
        for ib in range(0, 6):
            print("   bin %4.1f eV: L4/L0 at q = 0.4, 1.0, 2.0 q0: %s; fit residual (rms, rel. to Lbar) %s"
                  % (BIN[ib], np.round([np.interp(x, Q, c[4][:, ib] / c[0][:, ib]) for x in (0.4, 1.0, 2.0)], 3),
                     np.round([np.interp(x, Q, res[:, ib]) for x in (0.4, 1.0, 2.0)], 3)))
    Rnw = lattice_multipoles(m, wterm=False)
    print("Si lattice without the omega/q term: R4/R0 = %+.5f, A_day = %.4f" % (Rnw[4] / Rnw[0], amp(day_curve(Rnw)[1])))
    Rl = lattice_multipoles(m)
    h, r = day_curve(Rl)
    out["Si_lat"] = (Rl, r)
    print("Si lattice (one + two phonons coherent, n >= 3 incoherent), 2 MeV: R4/R0 = %+.5f, R6/R0 = %+.5f, R8/R0 = %+.6f; "
          "A_day = %.4f" % (Rl[4] / Rl[0], Rl[6] / Rl[0], Rl[8] / Rl[0], amp(r)))
    for mm in (0.5e6, 0.7e6, 1e6, 1.5e6, 3e6, 4e6, 5e6, 10e6):
        R2 = lattice_multipoles(mm)
        print("   Si lattice m = %4.1f MeV: R4/R0 = %+.5f, A_day(45N, [001] up) = %.4f" % (mm / 1e6, R2[4] / R2[0], amp(day_curve(R2)[1])))
    if os.path.exists(os.path.join(HERE, "gaas11_7.npz")):
        Rg = gaas_lattice_multipoles(m)
        hg, rg = day_curve(Rg)
        out["GaAs_lat"] = (Rg, rg)
        print("GaAs lattice (one phonon), 2 MeV: R4/R0 = %+.5f, R6/R0 = %+.5f; A_day = %.4f" % (Rg[4] / Rg[0], Rg[6] / Rg[0], amp(rg)))
    # orientation scan and the [001] || Earth-axis mounting
    for key in out:
        a_best, Rb = best_orientation(out[key][0])
        print("%s: best orientation at 45N gives A_day = %.4f (3000 random orientations)" % (key, a_best))
    # [001] along the Earth's axis (crystal z = celestial pole): pole in (E, N, U) = (0, cos lat, sin lat)
    lat = np.radians(45.0)
    zc = np.array([0, np.cos(lat), np.sin(lat)])
    xc = np.array([1.0, 0, 0])
    yc = np.cross(zc, xc)
    Rpole = np.array([xc, yc, zc])
    for key in out:
        h, r = day_curve(out[key][0], R=Rpole)
        spec = np.abs(np.fft.rfft(r - r.mean()))
        h0, r0 = day_curve(out[key][0])
        sp0 = np.abs(np.fft.rfft(r0 - r0.mean()))
        print("%s, [001] up at 45N: harmonics 1..4 per sidereal day (relative) %s" % (key, np.round(sp0[1:5] / sp0[1:5].max(), 3)))
        print("%s with [001] along the Earth's axis: A_day = %.4f, dominant harmonic = %d per sidereal day"
              % (key, amp(r), spec.argmax()))
    # Y^c_4 range along the 45N [001]-up path
    h = np.linspace(0, 2 * np.pi, 288, endpoint=False)
    y4 = AN.ycub(4, AN.vhat_crystal(45.0, h))
    print("Y^c_4 along the path: min %.3f max %.3f (sphere: %.3f at [111], %.3f at [100])"
          % (y4.min(), y4.max(), AN.ycub(4, np.ones(3) / np.sqrt(3)), AN.ycub(4, np.array([1, 0, 0.]))))
    # combined calorimetric signal: rate-weighted mean amplitude (needs the absolute rates; printed by fig11_7.py)
