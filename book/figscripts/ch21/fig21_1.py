"""Fig. 21.1 (fig:21-kernel): rate kernel k(v) of the silicon electron-recoil channel (heavy mediator, sigma_e = 1e-37 cm^2)
at m_chi = 1, 10 and 100 MeV, with the laboratory speed distributions of the standard halo and of a debris flow.
Output: tex/figures/ch21/fig21_1.pdf and fig21_1.log (every number quoted from the figure).
Kernel: kernel21.py (tabulated form factor of Essig et al. [E16], App. D.29 normalization, onset 1.2 eV).
Halo: standard halo at v_E^ref ([B] Table 1; eq:1.2-Fspeed); debris flow of Kuhlen, Lisanti and Spergel [KLS] Eq. (7),
v_flow = 340 km/s, at v_E^ref (halo21.py).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kernel21 import kernel, vth, prefactor, rate_eta, CKM  # noqa: E402
from halo21 import fspeed_shm, fspeed_df, eta_shm, VMAX, V_FLOW, VE_REF  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch21", "fig21_1.pdf")
LOG = open(os.path.join(HERE, "fig21_1.log"), "w")


def say(s):
    print(s)
    LOG.write(s + "\n")


v = np.linspace(1.0, 820.0, 3280)
fig, ax = plt.subplots(figsize=(5.0, 3.5))
cols = {1e6: "C0", 1e7: "k", 1e8: "C3"}
for m, ls in [(1e6, "-."), (1e7, "-"), (1e8, "--")]:
    k = kernel(m, v)
    ax.semilogy(v, k, color=cols[m], ls=ls, lw=1.3, label=f"{m/1e6:g} MeV")
    vt = vth(m)
    say(f"m = {m/1e6:g} MeV: prefactor {prefactor(m):.3e} /kg/yr; kernel opens at v = {vt:.1f} km/s "
        f"(sqrt(2*1.2 eV/m) = {np.sqrt(2*1.2/m)*CKM:.1f}; sqrt(2*1.15 eV/m) = {np.sqrt(2*1.15/m)*CKM:.1f})")
    for vv in [300.0, 400.0, 500.0, 600.0, 700.0, 794.5]:
        say(f"    k({vv:.0f} km/s) = {float(kernel(m, vv)):.3e} /kg/yr")
    # check: int F k dv equals sum w eta
    Rk = np.trapezoid(fspeed_shm(v) * k, v)
    Re = rate_eta(m, lambda u: eta_shm(u))
    say(f"    SHM rate: int F_chi k dv = {Rk:.4e}; P sum w eta = {Re:.4e} /kg/yr (ratio {Rk/Re:.4f})")
ax.set_xlim(0, 820)
ax.set_ylim(3e2, 5e6)
ax.set_xlabel(r"dark-matter speed $v$ (km/s)")
ax.set_ylabel(r"$k(v)$ (kg$^{-1}$ yr$^{-1}$)")
ax.axvline(VMAX, color="0.5", lw=0.6)
ax.legend(fontsize=7.5, loc="upper left", frameon=False, title=r"$m_\chi$", title_fontsize=7.5)
bx = ax.twinx()
bx.fill_between(v, fspeed_shm(v) * 1e3, color="0.85", lw=0, zorder=0)
bx.plot(v, fspeed_df(v) * 1e3, color="C2", lw=1.0)
bx.set_ylim(0, 6)
bx.set_ylabel(r"$F_\chi(v)$ ($10^{-3}$ s/km)")
bx.annotate("standard\nhalo", xy=(250, 2.2), xytext=(110, 2.6), fontsize=7, color="0.35", ha="center",
            arrowprops=dict(arrowstyle="-", color="0.5", lw=0.5))
bx.text(V_FLOW + VE_REF - 10, 3.6, "debris\nflow", fontsize=7, color="C2", ha="right")
ax.set_zorder(bx.get_zorder() + 1)
ax.patch.set_visible(False)
say(f"debris flow occupies {V_FLOW - VE_REF:.1f} to {V_FLOW + VE_REF:.1f} km/s at v_E^ref; "
    f"peak height {fspeed_df(V_FLOW + VE_REF - 1e-6)*1e3:.3f} e-3 s/km")
say(f"SHM speed distribution peak: {fspeed_shm(v).max()*1e3:.3f} e-3 s/km at {v[np.argmax(fspeed_shm(v))]:.0f} km/s")
vt1 = vth(1e6)
msk = v > vt1
say(f"fraction of standard-halo particles faster than the 1 MeV onset {vt1:.1f} km/s: {np.trapezoid(fspeed_shm(v)[msk], v[msk]):.3f}")
fig.tight_layout()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT)
say(f"wrote {os.path.relpath(OUT, HERE)}")
