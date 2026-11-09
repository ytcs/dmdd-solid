"""Limit Check 21.1a (lim:21.1a): eta(v_min) of the standard halo model in closed form at the reference Earth speed
(App. D.1; [E16] Eqs. (B.4)-(B.5)) against the fuller result, the same closed form averaged over a year of exposure
with the exact |v_E(t)| (eq:1.2-vE, eq:1.2-vorb). Output: tex/figures/ch21/limit21_1a.pdf and limit21_1a.log.

Plotted
  top:    eta(v_min) in natural units (times c): closed form at v_E^ref = 250.5 km/s (literature form, solid);
          year average <eta>_t with |v_E(t)| on 7305 equally spaced days (fuller result, dashed);
          untruncated Maxwellian at v_E^ref, v_esc -> infinity (dotted), to show what the escape cut does.
  bottom: ratio <eta>_t / eta_ref (dashed) and its leading correction, the second-order Taylor term in
          delta v_E(t) = |v_E(t)| - v_E^ref: 1 + [eta_v <dv> + eta_vv <dv^2>/2] / eta (dash-dotted).
  shaded: v_min below the speed where the ratio reaches 1.1 (closed form at v_E^ref within 10 % of the year average),
          found with brentq on the closed forms (not read from the plotting grid).
Halo: [B] Table 1 and Eq. (11) via halo21.py.
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from halo21 import eta_shm, fspeed_shm, vE_of_t, VE_REF, VESC, VMAX, CKM  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch21", "limit21_1a.pdf")
LOG = open(os.path.join(HERE, "limit21_1a.log"), "w")


def say(s):
    print(s)
    LOG.write(s + "\n")


# closed form against quadrature of F_chi/v
for u in [0.0, 300.0, 600.0, 780.0]:
    num = quad(lambda v: fspeed_shm(v) / v, max(u, 1e-9), VMAX, limit=400)[0]
    assert abs(num / eta_shm(u) - 1) < 1e-6
say("closed form = quadrature of F_chi/v to 1e-6 at v_min = 0, 300, 600, 780 km/s")

t = np.arange(7305) * (365.25 / 7305)
vE = vE_of_t(t)
dv = vE - VE_REF
say(f"|v_E(t)|: min {vE.min():.1f}, max {vE.max():.1f}, mean {vE.mean():.2f} km/s; "
    f"<dv> = {dv.mean():.3f} km/s, <dv^2> = {np.mean(dv**2):.2f} (km/s)^2, rms {np.sqrt(np.mean(dv**2)):.2f}")
say(f"largest laboratory speed over the year: {VESC + vE.max():.1f} km/s (reference {VMAX:.1f})")


def eta_avg(u):
    u = np.atleast_1d(u)
    return np.array([np.mean(eta_shm(x, vE)) for x in u])


def eta_corr(u, h=0.5):
    e0 = eta_shm(u)
    ep, em = eta_shm(u, VE_REF + h), eta_shm(u, VE_REF - h)
    d1, d2 = (ep - em) / (2 * h), (ep - 2 * e0 + em) / h**2
    return e0 + d1 * dv.mean() + 0.5 * d2 * np.mean(dv**2)


def ratio(u):
    return eta_avg(u)[0] / float(eta_shm(u)) - 1


for target in [0.01, 0.10]:
    u_b = brentq(lambda x: ratio(x) - target, 300.0, VMAX - 1e-6, xtol=1e-6)
    say(f"<eta>_t / eta_ref = {1 + target:.2f} at v_min = {u_b:.2f} km/s (v_max - v_min = {VMAX - u_b:.2f})")
    if target == 0.10:
        U10 = u_b
for u in [0.0, 300.0, 500.0, 600.0, 700.0, 760.0, 780.0, 790.0]:
    r = eta_avg(u)[0] / float(eta_shm(u))
    rc = float(eta_corr(u)) / float(eta_shm(u))
    ru = float(eta_shm(u, VE_REF, np.inf)) / float(eta_shm(u))
    say(f"v_min = {u:5.0f}: eta_ref = {float(eta_shm(u))*CKM:9.4g} (nat), <eta>_t/eta_ref = {r:.4f}, "
        f"second-order estimate {rc:.4f}, untruncated/truncated = {ru:.3f}")
for u in [794.5, 800.0, 805.0]:
    say(f"v_min = {u:.1f}: eta_ref = {float(eta_shm(u))*CKM:.3g}, <eta>_t = {eta_avg(u)[0]*CKM:.3g} (nat)")
# where the second-order estimate is itself within 1 % of the year average
u_c = brentq(lambda x: float(eta_corr(x)) / eta_avg(x)[0] - 1.01, 760.0, VMAX - 1, xtol=1e-6)
say(f"second-order estimate within 1 % of the year average below v_min = {u_c:.2f} km/s")

u = np.linspace(0, 812, 2031)
ea = eta_avg(u)
er = eta_shm(u)
eu = eta_shm(u, VE_REF, np.inf)
ec = eta_corr(u)
fig, (ax, bx) = plt.subplots(2, 1, figsize=(5.0, 4.4), sharex=True, gridspec_kw=dict(height_ratios=[2.2, 1]))
ax.semilogy(u, er * CKM, color="k", lw=1.4, label=r"closed form at $v_{\mathrm{E}}^{\mathrm{ref}}$")
ax.semilogy(u, ea * CKM, color="C3", lw=1.2, ls="--", label=r"year average with $|\mathbf{v}_{\mathrm{E}}(t)|$")
ax.semilogy(u, eu * CKM, color="C0", lw=1.0, ls=":", label=r"no escape cut ($v_{\mathrm{esc}}\to\infty$)")
ax.set_ylim(1e-3, 3e3)
ax.set_ylabel(r"$\eta(v_{\mathrm{min}})$ (units of $1/c$)")
ax.legend(fontsize=7.5, loc="lower left", frameon=False)
for a in (ax, bx):
    a.axvspan(0, U10, color="0.9", lw=0)
    a.axvline(VMAX, color="0.5", lw=0.6)
ax.text(VMAX - 8, 1.5e3, r"$v_{\mathrm{max}}$", fontsize=7.5, ha="right", color="0.3")
m = er > 0
bx.plot(u[m], ea[m] / er[m], color="C3", lw=1.2, ls="--", label="year average / closed form")
bx.plot(u[m], ec[m] / er[m], color="0.3", lw=1.0, ls="-.", label="second-order correction")
bx.axhline(1.1, color="0.6", lw=0.5, ls=":")
bx.set_ylim(0.95, 1.6)
bx.set_xlim(0, 812)
bx.set_xlabel(r"$v_{\mathrm{min}}$ (km/s)")
bx.set_ylabel("ratio")
bx.legend(fontsize=7.5, loc="upper left", frameon=False)
fig.tight_layout()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT)
say(f"wrote {os.path.relpath(OUT, HERE)}")
