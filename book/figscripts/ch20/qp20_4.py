"""Quasiparticle yield of a superconducting film (Sect. 20.4): every number printed in Sect. 20.4, Fig. 20.4
(fig:20-yield, fig20_4.pdf), Limit Check 20.4a (lim:20.4a, limit20_4a.pdf) and Worked example 20.4.
Log: qp20_4.log.  Run: python qp20_4.py > qp20_4.log   (about two minutes, numpy/scipy/matplotlib only).

MODEL: the Kaplan cascade in a lumped film at T = 0 (Sect. 20.4, eq:20.4-emit, eq:20.4-split, eq:20.4-tpb, eq:20.4-ppb).
Energies in units of Delta_BCS.  Kernels at T = 0 (Kaplan et al., PRB 14, 4854 (1976), as quoted by Leman,
arXiv:1109.1193, Sect. IV items 3-4, p. 16):
  quasiparticle at E emits a phonon W in [0, E - 1] with density  a2F(W) rho(E - W) [1 - 1/(E (E - W))],
      rho(x) = x / sqrt(x^2 - 1)  (BCS density of states over the normal one, eq:7.2-dos),
      MODELLING CHOICE: a2F(W) = b W^2 (low-frequency Debye form of Kaplan et al.; Al a2F of Sect. 6.4 is
      phonon-like only below a few meV, so the model is used up to 60 Delta = 10.8 meV at Delta = 0.18 meV);
  phonon W >= 2 breaks a pair into (E, W - E) with density [E (W - E) + c] / sqrt((E^2 - 1)((W - E)^2 - 1)),
      c = +1 for a phonon (case I coherence factor, eq:7.2-cohE), c = -1 for a photon (case II), the
      photon form being Guruswamy et al. Eq. (1) (arXiv:1401.1937);
  pair-breaking rate  1/t_pb(W) = I(W) / (pi t0),  I(W) = integral of the case-I split density (in Delta units),
      so that t_pb(2 Delta) = t0 (Kaplan's characteristic phonon time; t0 = 0.26 ns for Al as used by
      Guruswamy et al. p. 3);
  film loss: every phonon leaves the film at the rate 1/t_l, independent of energy (Guruswamy et al. p. 2);
      a phonon above 2 Delta breaks a pair with probability p_pb = 1/(1 + t_pb/t_l) = I/(I + pi t0/t_l);
      phonons below 2 Delta are lost (they cannot break pairs at T = 0).
  Quasiparticles stay in the film and end at the gap edge; no recombination during the cascade (low density).
  Yield: Y_qp(W0) = Delta <N_qp> / W0 for a phonon that has broken its first pair (absorption is not counted).
METHODS: (i) expected-value recursion on an energy grid (Gauss-Legendre quadrature after the substitutions
  E = 1 + (W - 2) sin^2(theta) for the pair split and x = 1 + (U - 1) s^2 for the emitted-phonon kernel, which
  remove the inverse-square-root edges); fixed-point iteration to 1e-12; (ii) event Monte Carlo with the same
  kernels (rejection sampling in theta and s) as a check and for the spectrum of phonons a film returns.
EXTERNAL REFERENCE POINTS (all quoted, none fitted):
  Guruswamy, Goldie, Withington, arXiv:1401.1937 Fig. 4: eta_s(h nu_s/Delta) for tau_l/tau0phi = 0.5, 1, 2, 4, 8,
      read off the figure at h nu = 5, 6, 7, 8, 10 Delta (200-dpi digitization; reading uncertainty ~0.005).
      Chang-Scalapino kinetic equations, measured Al a2F, T/Tc = 0.1, probe 20 aW/um^3, photon seed.
  Infinite-volume asymptote 0.57-0.6 (Al, Nb, Sn), quoted in arXiv:1401.1937 p. 2.
  Isotope-scattering and anharmonic constants of Si and Ge: Leman, arXiv:1109.1193 Table I (A_iso 2.43e-42 and
      3.67e-41 s^3; A_anh 7.41e-56 and 6.43e-55 s^4; v_t 5400 and 3250 m/s); Ge A_anh 1.61e-55 (Hertel & Pyle) and
      1.65e-54 s^4 (Hernandez et al.) as in Sect. 20.2.
  Film escape ratio of a 60 nm Al film from Sect. 20.3 (0 K constants): t_l/t0 = 0.72 (AMM) - 0.94 (DMM).
"""
import os
import math
import random
import numpy as np
from numpy.polynomial.legendre import leggauss
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch20")
os.makedirs(FIG, exist_ok=True)

DELTA_MEV = 0.18          # Al gap Delta_BCS (meV), measured bulk value used in Sect. 7.2 (Savrasov Table III)
H_MEV_THZ = 4.135667696   # h in meV per THz
T0_NS = 0.26              # Kaplan characteristic phonon time of Al, as used by arXiv:1401.1937 p. 3

NQ = 160
_x, _w = leggauss(NQ)


def gl(a, b):
    """Gauss-Legendre nodes/weights on [a, b] (broadcasts over arrays a, b)."""
    a = np.asarray(a, float)[..., None]
    b = np.asarray(b, float)[..., None]
    return 0.5 * (b - a) * _x + 0.5 * (b + a), 0.5 * (b - a) * _w


TH, WTH = gl(0.0, 0.5 * np.pi)
TH, WTH = TH.ravel(), WTH.ravel()
S01, WS01 = gl(0.0, 1.0)
S01, WS01 = S01.ravel(), WS01.ravel()


def pair_nodes(W, c=+1.0):
    """Nodes E, E' and weights k such that sum k f(E) = int dE split-density f(E), for phonon/photon energy W >= 2."""
    W = np.atleast_1d(np.asarray(W, float))[:, None]
    E = 1.0 + (W - 2.0) * np.sin(TH) ** 2
    Ep = W - E
    k = 2.0 * (E * Ep + c) / np.sqrt((E + 1.0) * (Ep + 1.0)) * WTH
    return E, Ep, k


def I_of(W):
    return pair_nodes(W, +1.0)[2].sum(axis=1)


def p_pb(W, r):
    I = I_of(W)
    return np.ones_like(I) if np.isinf(r) else I / (I + np.pi / r)


def emit_weight(E, x):
    """Emitted-phonon density at final quasiparticle energy x (phonon E - x), without the rho(x) factor."""
    return (E - x) ** 2 * (1.0 - 1.0 / (E * x))


def rho_nodes(E, U):
    """Nodes x in [1, U] and weights for int_1^U rho(x) g(x) dx with x = 1 + (U-1) s^2 (U > 1 array)."""
    U = np.asarray(U, float)[:, None]
    x = 1.0 + (U - 1.0) * S01 ** 2
    w = 2.0 * x * np.sqrt(U - 1.0) / np.sqrt(x + 1.0) * WS01
    return x, w


class Cascade:
    def __init__(self, r, Emax=62.0, h=0.01):
        self.r = r
        self.Eg = np.arange(1.0, Emax + h / 2, h)
        self.Wg = np.arange(2.0, Emax + h / 2, h)
        self.nq = np.ones_like(self.Eg)
        self.npb = 2.0 * p_pb(self.Wg, r)
        self.ppb = p_pb(self.Wg, r)
        self.solve()

    def nq_at(self, E):
        return np.where(E < 3.0, 1.0, np.interp(E, self.Eg, self.nq))

    def np_at(self, W):
        return np.where(W < 2.0, 0.0, np.interp(W, self.Wg, self.npb))

    def solve(self, tol=1e-12, itmax=200):
        hi = self.Eg >= 3.0
        E = self.Eg[hi]
        # normalization Z(E) = int_1^E rho(x) w(E,x) dx
        x, wz = rho_nodes(E, E)
        Z = (wz * emit_weight(E[:, None], x)).sum(axis=1)
        xa, wa = rho_nodes(E, E - 2.0)              # final qp energies for phonons W = E - x >= 2
        Ka = wa * emit_weight(E[:, None], xa)
        xb, wb = gl(np.full_like(E, 3.0), E)        # final qp energies x >= 3 (regular)
        Kb = wb * emit_weight(E[:, None], xb) * xb / np.sqrt(xb ** 2 - 1.0)
        Ep, Epp, kp = pair_nodes(self.Wg, +1.0)
        Ip = kp.sum(axis=1)
        for it in range(itmax):
            A = (Ka * self.np_at(E[:, None] - xa)).sum(axis=1)
            B = (Kb * (self.nq_at(xb) - 1.0)).sum(axis=1)
            nq_new = self.nq.copy()
            nq_new[hi] = 1.0 + (A + B) / Z
            Nabs = ((self.nq_at(Ep) + self.nq_at(Epp)) * kp).sum(axis=1) / Ip
            np_new = self.ppb * Nabs
            d = max(np.abs(nq_new - self.nq).max(), np.abs(np_new - self.npb).max())
            self.nq, self.npb = nq_new, np_new
            if d < tol:
                break
        self.iters = it + 1

    def N_abs(self, W, c=+1.0):
        """Mean number of quasiparticles from a quantum of energy W that has broken its first pair."""
        E, Ep, k = pair_nodes(W, c)
        return ((self.nq_at(E) + self.nq_at(Ep)) * k).sum(axis=1) / k.sum(axis=1)

    def Y(self, W, c=+1.0):
        W = np.atleast_1d(np.asarray(W, float))
        return self.N_abs(W, c) / W


# ---------------------------------------------------------------- event Monte Carlo (check; returned spectrum)
def _bound(f, a, b, n=400):
    return 1.15 * max(f(a + (b - a) * i / n) for i in range(n + 1))


def mc_events(W0, r, nev, c=+1.0, seed=1, follow_subgap=False, emin=1e-3):
    rnd = random.Random(seed)
    yields, closure = [], 0.0
    esc_sub, esc_above = [], []
    for _ in range(nev):
        stack = [W0]
        first = True
        nqp = 0
        out = 0.0
        while stack:
            W = stack.pop()
            if W < 2.0:
                out += W
                if follow_subgap:
                    esc_sub.append(W)
                continue
            if not first:
                I = I_of(W)[0]
                pb = 1.0 if math.isinf(r) else I / (I + math.pi / r)
                if rnd.random() >= pb:
                    out += W
                    if follow_subgap:
                        esc_above.append(W)
                    continue
            cc = c if first else 1.0
            first = False
            Wm2 = W - 2.0
            g = lambda t: (1 + Wm2 * math.sin(t) ** 2) * (W - 1 - Wm2 * math.sin(t) ** 2) + cc
            gg = lambda t: g(t) / math.sqrt((2 + Wm2 * math.sin(t) ** 2) * (W + 1 - (1 + Wm2 * math.sin(t) ** 2)))
            gmax = _bound(gg, 0.0, 0.5 * math.pi, 64)
            while True:
                t = 0.5 * math.pi * rnd.random()
                if rnd.random() * gmax <= gg(t):
                    break
            E1 = 1.0 + Wm2 * math.sin(t) ** 2
            nqp += 2
            for E in (E1, W - E1):
                while E >= 3.0 or (follow_subgap and E - 1.0 > emin):
                    U = E
                    f = lambda s: emit_weight(U, 1 + (U - 1) * s * s) * (1 + (U - 1) * s * s) / math.sqrt(2 + (U - 1) * s * s)
                    fmax = _bound(f, 0.0, 1.0, 64)
                    while True:
                        s = rnd.random()
                        if rnd.random() * fmax <= f(s):
                            break
                    xnew = 1.0 + (U - 1.0) * s * s
                    stack.append(U - xnew)
                    E = xnew
                if follow_subgap:
                    out += E - 1.0
                    if E - 1.0 > 0:
                        esc_sub.append(E - 1.0)
        yields.append(nqp / W0)
        if follow_subgap:
            closure = max(closure, abs(nqp + out - W0))
    yv = np.array(yields)
    return yv.mean(), yv.std(ddof=1) / math.sqrt(nev), np.array(esc_sub), np.array(esc_above), closure


# ---------------------------------------------------------------- main
if __name__ == "__main__":
    print("# Sect. 20.4: Kaplan cascade in a lumped film, T = 0, a2F = b W^2; energies in Delta_BCS")
    print("## pair-breaking integral I(W) and t_pb/t0 = pi/I")
    for W in (2.0 + 1e-9, 2.5, 3.0, 4.0, 5.0, 10.0, 40.0, 100.0):
        I = I_of(W)[0]
        print(f"W = {W:7.3f}  I = {I:9.5f}  t_pb/t0 = {np.pi / I:.4f}   I/W = {I / W:.4f}")
    # checks against independent quadrature values (CMPMC test table, 12 digits): I(2.5)=3.54521, I(3)=3.96636,
    # I(5)=5.75328, I(10)=10.505, I(40)=40.1943
    for W, ref in ((2.5, 3.54521), (3.0, 3.96636), (5.0, 5.75328), (10.0, 10.505), (40.0, 40.1943)):
        assert abs(I_of(W)[0] - ref) < 2e-5 * ref, (W, I_of(W)[0], ref)
    print(f"WE 20.4: t_pb(3 Delta) = {np.pi / I_of(3.0)[0]:.3f} t0 = {np.pi / I_of(3.0)[0] * T0_NS:.3f} ns (t0 = {T0_NS} ns)")
    print(f"WE 20.4: 3 Delta = {3 * DELTA_MEV:.2f} meV = {3 * DELTA_MEV / H_MEV_THZ * 1e3:.0f} GHz; "
          f"2 Delta = {2 * DELTA_MEV:.2f} meV = {2 * DELTA_MEV / H_MEV_THZ * 1e3:.1f} GHz; "
          f"4 Delta = {4 * DELTA_MEV:.2f} meV = {4 * DELTA_MEV / H_MEV_THZ * 1e3:.0f} GHz")

    # Al: v_F = 6.75e-3 c (free-electron value of Sect. 6.4/7.2); longitudinal sound speed: the isotropic (Voigt)
    # value of Sect. 20.3 from the 0 K elastic constants C11, C12, C44 = 114.3, 61.9, 31.6 GPa (Kamm & Alers, as
    # tabulated in arXiv:2109.13551 Table 2) at rho = 2.70 g/cm^3: c_LA = 6.63 km/s (amm20_3.log)
    vF = 6.75e-3 * 2.99792458e8
    mu = (114.3 - 61.9 + 3 * 31.6) / 5 * 1e9
    Bm = (114.3 + 2 * 61.9) / 3 * 1e9
    vL = math.sqrt((Bm + 4 * mu / 3) / 2700.0)
    vT = math.sqrt(mu / 2700.0)
    print(f"Al: v_F = {vF:.3g} m/s, c_LA (Voigt, 0 K) = {vL:.0f} m/s, c_T = {vT:.0f} m/s, v_F/c_LA = {vF / vL:.0f}, v_F/c_T = {vF / vT:.0f}")
    print(f"Delta/(v_F q) at E_ath = 2 Delta (longitudinal): {1 / (2 * vF / vL):.2e}")
    print(f"Delta/h = {DELTA_MEV / H_MEV_THZ * 1e3:.1f} GHz")
    print(f"Ge Debye energy (f_D = 8.64 THz, Leman Table I) = {8.64 * H_MEV_THZ:.2f} meV")
    for r in (4.0,):
        print(f"p_pb at r = {r}: 3 Delta {p_pb(3.0, r)[0]:.3f}, 10 Delta {p_pb(10.0, r)[0]:.3f}")
        print(f"escape probability of a 200 Delta phonon (near the Al Debye energy) at r = {r}: {1 - p_pb(200.0, r)[0]:.4f}")
    rs = [0.5, 1.0, 2.0, 4.0, 8.0, np.inf]
    cas = {r: Cascade(r) for r in rs}
    for r in rs:
        print(f"r = t_l/t0 = {r}: converged in {cas[r].iters} iterations")
    cas60 = {r: Cascade(r) for r in (0.72, 0.94)}

    print("## below 4 Delta: Y = 2/W for every r (phonon and photon seeds)")
    Wl = np.linspace(2.0 + 1e-6, 4.0 - 1e-6, 41)
    for r in rs:
        for c in (+1.0, -1.0):
            dev = np.abs(cas[r].Y(Wl, c) - 2.0 / Wl).max()
            assert dev < 1e-12, (r, c, dev)
    print("max |Y - 2/W| on (2, 4) Delta, all r, both seeds: < 1e-12")
    print("WE 20.4: Y(3 Delta) =", f"{cas[np.inf].Y(3.0)[0]:.6f}", "= 2/3; sub-gap energy = 1 Delta per event")

    print("## no-loss limit (infinite volume), phonon seed")
    for W in (4.0 + 1e-6, 4.5, 5.0, 6.0, 8.0, 10.0, 20.0, 40.0, 60.0):
        print(f"W = {W:6.2f}: Y_inf(phonon) = {cas[np.inf].Y(W)[0]:.4f}   Y_inf(photon) = {cas[np.inf].Y(W, -1.0)[0]:.4f}")
    Wf = np.arange(4.0005, 60.0, 0.001)
    Yinf = cas[np.inf].Y(Wf)
    i = np.argmax(Yinf)
    print(f"no-loss maximum: Y = {Yinf[i]:.4f} at W = {Wf[i]:.3f} Delta; Y(60) = {Yinf[-1]:.4f}")
    print(f"no-loss range over 10-60 Delta: {Yinf[Wf >= 10].min():.4f} - {Yinf[Wf >= 10].max():.4f}")

    print("## lumped film, phonon seed: Y(W, r)")
    hdr = "W/Delta " + " ".join(f"r={r:>4}" for r in rs)
    print(hdr)
    for W in (3.0, 4.0 + 1e-6, 5.0, 6.0, 8.0, 10.0, 20.0, 30.0, 40.0, 60.0):
        print(f"{W:7.2f} " + " ".join(f"{cas[r].Y(W)[0]:.4f}" for r in rs))
    for r in rs[:-1]:
        y = cas[r].Y(Wf)
        j = np.argmax(y)
        print(f"r = {r}: local maximum above 4 Delta Y = {y[j]:.4f} at {Wf[j]:.3f} Delta; "
              f"Y(10)/Y_inf(10) = {cas[r].Y(10.0)[0] / cas[np.inf].Y(10.0)[0]:.4f}; "
              f"Y(40)/Y_inf(40) = {cas[r].Y(40.0)[0] / cas[np.inf].Y(40.0)[0]:.4f}")
    # 60 nm aluminum film of Sect. 20.3 (0 K constants): t_l/t0 = 0.72 (AMM) - 0.94 (DMM)
    for r, c in cas60.items():
        print(f"60 nm film, r = {r}: Y(5) = {c.Y(5.0)[0]:.4f}, Y(10) = {c.Y(10.0)[0]:.4f}, Y(16) = {c.Y(16.0)[0]:.4f}, "
              f"Y(24) = {c.Y(24.0)[0]:.4f}, Y(60) = {c.Y(60.0)[0]:.4f}")
    # arrival band of down-converted primaries: 10-90 % of the absorbed primary energy in the mean-field estimate of
    # Sect. 20.5 lies between 2.45 and 7.88 meV (0.59-1.91 THz), i.e. 13.6-43.8 Delta_Al (kern20_5.log)
    WLO, WHI = 2.45 / DELTA_MEV, 7.88 / DELTA_MEV
    print(f"arrival band {WLO:.1f}-{WHI:.1f} Delta = {2.45/H_MEV_THZ:.2f}-{7.88/H_MEV_THZ:.2f} THz")
    print(f"{WLO:.1f} Delta phonon = 2.45 meV: quasiparticles at Y = 1: {WLO:.1f}; no loss: {WLO * cas[np.inf].Y(WLO)[0]:.2f};"
          f" r = 0.5: {WLO * cas[0.5].Y(WLO)[0]:.2f}; Y range {cas[0.5].Y(WLO)[0]:.3f} - {cas[np.inf].Y(WLO)[0]:.3f}")
    print("variation of Y across the arrival band, per r, and the loss against the no-escape yield:")
    for r in rs:
        y = cas[r].Y(np.array([10.0, WLO, WHI]))
        yi = cas[np.inf].Y(np.array([10.0, WLO, WHI]))
        print(f"  r = {r}: Y({WLO:.1f}) = {y[1]:.4f}, Y({WHI:.1f}) = {y[2]:.4f}, change {100 * (y[2] / y[1] - 1):+.1f} %; "
              f"loss 1 - Y/Y_inf at 10, {WLO:.1f}, {WHI:.1f} Delta: {100*(1-y[0]/yi[0]):.1f}, {100*(1-y[1]/yi[1]):.1f}, "
              f"{100*(1-y[2]/yi[2]):.1f} %")
    for r, c in cas60.items():
        y = c.Y(np.array([WLO, WHI]))
        print(f"  60 nm film r = {r}: Y({WLO:.1f}) = {y[0]:.4f}, Y({WHI:.1f}) = {y[1]:.4f}, loss {100*(1-y[0]/0.5904):.1f}-{100*(1-y[1]/0.5904):.1f} %")

    print("## phonon (case I) versus photon (case II) seed")
    for r in (1.0, np.inf):
        for W in (5.0, 10.0):
            a, b = cas[r].Y(W)[0], cas[r].Y(W, -1.0)[0]
            print(f"r = {r}, W = {W}: phonon {a:.4f}, photon {b:.4f}, difference {a - b:+.4f}")

    print("## comparison with Guruswamy et al. Fig. 4 (photon seed; Chang-Scalapino equations, measured a2F, T/Tc = 0.1)")
    fig4 = {0.5: [0.475, 0.437, 0.409, 0.385, 0.354], 1.0: [0.504, 0.479, 0.457, 0.442, 0.416],
            2.0: [0.534, 0.520, 0.506, 0.495, 0.479], 4.0: [0.564, 0.558, 0.545, 0.540, 0.533],
            8.0: [0.605, 0.605, 0.597, 0.594, 0.594]}
    Wfig = np.array([5.0, 6.0, 7.0, 8.0, 10.0])
    maxd = {}
    for r, vals in fig4.items():
        y = cas[r].Y(Wfig, -1.0)
        d = y - np.array(vals)
        maxd[r] = np.abs(d).max()
        print(f"r = {r}: cascade " + " ".join(f"{v:.4f}" for v in y) + " | Fig.4 " + " ".join(f"{v:.3f}" for v in vals)
              + " | cascade - Fig.4 " + " ".join(f"{v:+.4f}" for v in d))
    print(f"max |cascade - Fig.4| for r <= 4: {max(maxd[r] for r in (0.5, 1.0, 2.0, 4.0)):.4f}; at r = 8: {maxd[8.0]:.4f}")
    d8 = cas[8.0].Y(Wfig, -1.0) - np.array(fig4[8.0])
    print(f"r = 8 offset range: {d8.min():+.4f} to {d8.max():+.4f}")
    print("Fig.4 ratio eta(10)/eta(5) at r = 0.5:", f"{fig4[0.5][4] / fig4[0.5][0]:.3f};",
          "reduction of r=0.5 against the no-loss 0.59 at 10 Delta:",
          f"{1 - fig4[0.5][4] / 0.59:.3f}")

    print("## Monte Carlo check of the recursion")
    for (W, r, c) in ((5.0, 1.0, -1.0), (10.0, 1.0, +1.0), (10.0, np.inf, +1.0), (20.0, 2.0, +1.0)):
        m, e, _, _, _ = mc_events(W, r, 20000, c=c, seed=int(W * 10 + (0 if np.isinf(r) else r)))
        rec = cas[r].Y(W, c)[0]
        print(f"W = {W}, r = {r}, c = {c:+.0f}: MC {m:.4f} +- {e:.4f}, recursion {rec:.4f}, diff {m - rec:+.4f} ({(m - rec) / e:+.1f} sigma)")

    print("## phonons a thick film (electrode) returns to the substrate")
    spectra = {}
    for W0 in (20.0, 40.0):
        for r in (2.0, 4.0, 8.0):
            m, e, sub, above, clos = mc_events(W0, r, 4000, follow_subgap=True, seed=int(7 * W0 + r))
            esc = np.concatenate([sub, above])
            Eret = esc.sum() / 4000
            fsub_E = sub.sum() / esc.sum()
            # after recombination the quasiparticle energy (Y W0 per seed) returns as 2-Delta phonons
            tot = esc.sum() + m * W0 * 4000
            f2 = (sub.sum() + m * W0 * 4000) / tot
            f4 = (esc[esc < 4.0].sum() + m * W0 * 4000) / tot
            f10 = (esc[esc < 10.0].sum() + m * W0 * 4000) / tot
            print(f"seed {W0:4.0f} Delta, r = {r}: Y = {m:.4f}; prompt return {Eret / W0:.4f} of seed, of which "
                  f"{fsub_E:.4f} below 2 Delta; all returned energy incl. recombination: at or below 2 Delta {f2:.4f}, "
                  f"below 4 Delta {f4:.4f}, below 10 Delta {f10:.4f}; energy closure {clos:.1e}")
            spectra[(W0, r)] = (sub, above, m)
    # ballistic flight of 2 Delta_Al phonons in Si and Ge (isotope f^4, anharmonic f^5; Leman Table I)
    f2 = 2 * DELTA_MEV / H_MEV_THZ * 1e12
    for name, Aiso, Aanh, vt in (("Si", 2.43e-42, 7.41e-56, 5400.0), ("Ge", 3.67e-41, 6.43e-55, 3250.0)):
        giso, ganh = Aiso * f2 ** 4, Aanh * f2 ** 5
        print(f"{name}: f(2 Delta_Al) = {f2 / 1e9:.1f} GHz; isotope rate {giso:.3g} /s, mean free path (v_t) "
              f"{vt / giso:.3g} m; anharmonic rate {ganh:.3g} /s")
    # Ge anharmonic constants of Sect. 20.2 (1.61e-55 Hertel-Pyle, 6.43e-55 Leman, 1.65e-54 Hernandez): decay time of a
    # longitudinal 2 Delta_Al phonon
    print("Ge: decay time of a longitudinal 2 Delta_Al phonon, A_anh = 1.61e-55 / 6.43e-55 / 1.65e-54 s^4: "
          + " / ".join(f"{1/(A*f2**5):.2f} s" for A in (1.61e-55, 6.43e-55, 1.65e-54)))
    # prompt Ge phonon in Delta units (Ge Debye energy 35.7 meV, quoted in Sect. 20.4 via E.25)
    print(f"Ge prompt phonon 35.7 meV = {35.7 / DELTA_MEV:.0f} Delta_Al; ratio to 2 Delta_Al = {35.7 / (2 * DELTA_MEV):.0f}")

    # ------------------------------------------------------------ figures
    plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
    cols = {0.5: "#1f77b4", 1.0: "#2ca02c", 2.0: "#ff7f0e", 4.0: "#d62728", 8.0: "#9467bd", np.inf: "k"}

    # Fig. 20.4: (a) Y_qp(E_ath) from 2 to 60 Delta for six r; (b) returned spectrum of a thick film
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.4, 2.9), gridspec_kw={"width_ratios": [1.25, 1]})
    Wp = np.concatenate([np.linspace(2.0005, 3.9995, 200), np.geomspace(4.0005, 60.0, 600)])
    for r in rs:
        lab = r"$\infty$" if np.isinf(r) else f"{r:g}"
        ax.plot(Wp, cas[r].Y(Wp), color=cols[r], lw=1.2 if np.isinf(r) else 1.0, label=lab)
    ax.axvspan(2.0, 4.0, color="0.9", lw=0)
    ax.axvspan(2.45 / DELTA_MEV, 7.88 / DELTA_MEV, color="#fde9c9", lw=0, alpha=0.6)
    ax.set_xscale("log")
    ax.set_xlim(2.0, 60.0)
    ax.set_ylim(0.25, 1.02)
    ax.set_xticks([2, 3, 4, 6, 10, 20, 40, 60])
    ax.set_xticklabels(["2", "3", "4", "6", "10", "20", "40", "60"])
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_xlabel(r"$E_{\mathrm{ath}}/\Delta_{\mathrm{BCS}}$")
    ax.set_ylabel(r"$Y_{\mathrm{qp}}$")
    ax.legend(title=r"$t_l/t_0$", fontsize=7, title_fontsize=7, ncol=2, loc="upper right", frameon=False)
    ax.text(2.1, 0.28, "(a)")
    sub, above, m = spectra[(40.0, 4.0)]
    bins = np.linspace(0, 6, 61)
    hs, _ = np.histogram(sub, bins=bins, weights=sub)
    ha, _ = np.histogram(above, bins=bins, weights=above)
    norm = 4000 * 40.0 * (bins[1] - bins[0])
    bx.bar(bins[:-1], hs / norm, width=bins[1] - bins[0], align="edge", color="#1f77b4", lw=0, label="sub-gap")
    bx.bar(bins[:-1], ha / norm, width=bins[1] - bins[0], align="edge", bottom=hs / norm, color="#ff7f0e", lw=0,
           label="escaped above gap")
    bx.annotate("", xy=(2.0, 0.0), xytext=(2.0, 0.35), arrowprops=dict(arrowstyle="<-", color="k", lw=1.2))
    bx.text(2.15, 0.215, f"recombination\nat $2\\Delta_{{\\mathrm{{BCS}}}}$:\n{m:.2f} of seed", fontsize=7)
    bx.set_xlim(0, 6)
    bx.set_ylim(0, 0.36)
    bx.set_xlabel(r"returned phonon energy $/\Delta_{\mathrm{BCS}}$")
    bx.set_ylabel(r"energy per unit $\Delta_{\mathrm{BCS}}$, per seed energy")
    bx.legend(fontsize=7, frameon=False, loc="center right", bbox_to_anchor=(1.0, 0.45))
    bx.text(0.15, 0.335, "(b)")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig20_4.pdf"))

    # Limit Check 20.4a: 2 Delta/E (derived below 4 Delta) against the cascade and the kinetic-equation points
    fig, ax = plt.subplots(figsize=(4.8, 3.2))
    Wa = np.linspace(2.0005, 10.0, 800)
    ax.axvspan(2.0, 4.0, color="0.88", lw=0)
    ax.plot(Wa, 2.0 / Wa, "k--", lw=1.0, label=r"$2\Delta_{\mathrm{BCS}}/E_{\mathrm{ath}}$")
    for r in (0.5, 1.0, 2.0, 4.0, 8.0, np.inf):
        lab = r"$\infty$" if np.isinf(r) else f"{r:g}"
        ax.plot(Wa, cas[r].Y(Wa, -1.0), color=cols[r], lw=1.0, label=lab)
        if not np.isinf(r):
            ax.plot(Wfig, fig4[r], "o", ms=3.2, mfc="none", color=cols[r])
    ax.set_xlim(2.0, 10.0)
    ax.set_ylim(0.3, 1.02)
    ax.set_xlabel(r"$E_{\mathrm{ath}}/\Delta_{\mathrm{BCS}}$ (photon energy for the points)")
    ax.set_ylabel(r"$Y_{\mathrm{qp}}$")
    ax.legend(title=r"$t_l/t_0$", fontsize=7, title_fontsize=7, ncol=2, frameon=False, loc="upper right")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "limit20_4a.pdf"))
    print("figures written: fig20_4.pdf, limit20_4a.pdf")
