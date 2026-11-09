"""Angle between the Earth's galactic-frame velocity and a laboratory zenith axis over one sidereal day,
for several latitudes. Output: tex/figures/ch01/fig1_4.pdf. Every plotted number is sourced below.
  [B]  D. Baxter et al., Eur. Phys. J. C 81, 907 (2021), arXiv:2105.00599, Table 1 (solar velocity).
  [M]  C. McCabe, JCAP 02 (2014) 027, arXiv:1312.1355, App. B, Eq. (B3) and the J2000.0 values
       alpha_GP = 192.85948 deg, delta_GP = 27.12825 deg, l_CP = 122.932 deg quoted with it.
The direction is that of the solar velocity v_sun (|v_sun| = v_E^ref), i.e. the annual mean direction
up to a few degrees. Angle formula derived in Sect. 1.2.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

V_SUN = np.array([11.1, 238.0 + 12.2, 7.3])      # km/s, galactic (U, V, W) [B, Table 1]
L_CP, A_GP, D_GP = np.radians([122.932, 192.85948, 27.12825])   # [M, App. B]
sl, cl, sa, ca, sd, cd = np.sin(L_CP), np.cos(L_CP), np.sin(A_GP), np.cos(A_GP), np.sin(D_GP), np.cos(D_GP)
M = np.array([[-sl*sa - cl*ca*sd,  sl*ca - cl*sa*sd, cl*cd],      # x_gal = M x_equat [M, Eq. (B3)]
              [ cl*sa - sl*ca*sd, -cl*ca - sl*sa*sd, sl*cd],
              [ ca*cd,             sa*cd,            sd   ]])
u = M.T @ (V_SUN / np.linalg.norm(V_SUN))         # unit vector in equatorial coordinates
ra = np.arctan2(u[1], u[0]) % (2*np.pi)           # 20.91 h
dec = np.arcsin(u[2])                             # 47.54 deg

lst = np.linspace(0, 24, 961)                     # local sidereal time [h]
fig, ax = plt.subplots(figsize=(5.6, 3.4))
cols = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
styles = ["-", "--", "-.", ":"]
for lat_deg, col, ls in zip([90, 45, 0, -45], cols, styles):
    lat = np.radians(lat_deg)
    cospsi = np.sin(lat)*np.sin(dec) + np.cos(lat)*np.cos(dec)*np.cos(np.radians(15*lst) - ra)
    psi = np.degrees(np.arccos(np.clip(cospsi, -1, 1)))
    lab = {90: r"pole, $90^\circ$N", 45: r"$45^\circ$N", 0: "equator", -45: r"$45^\circ$S"}[lat_deg]
    ax.plot(lst, psi, color=col, ls=ls, lw=1.6, label=lab)
ax.axvline(np.degrees(ra)/15, color="0.6", lw=0.6)
ax.set_xlim(0, 24); ax.set_ylim(0, 180)
ax.set_xticks(range(0, 25, 4)); ax.set_yticks(range(0, 181, 30))
ax.set_xlabel("local sidereal time [h]")
ax.set_ylabel(r"angle $\theta_{\mathrm{lab}}$ between $\mathbf{v}_E$ and zenith [deg]")
ax.legend(frameon=False, fontsize=8, ncol=4, loc="upper center", bbox_to_anchor=(0.5, 1.13))
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch01", "fig1_4.pdf")
fig.savefig(out)
print(np.degrees(ra)/15, np.degrees(dec))
