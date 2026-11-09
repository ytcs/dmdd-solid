"""Shell averages of the impact-ionization rates of ii.py (and exchange factors of exch.py), Keldysh fits, and the
phonon rates of phonon.py; writes data/rates_<tag>.json and data/rx_<tag>.npz (R_x(E) for mc.py).
Run: python3 rates_summary.py TAG [EXCHFILE]
"""
import fbc_common  # noqa: F401
import os
import sys
import json
import numpy as np
from scipy.optimize import curve_fit
from fbc_common import Grid, EG, NV, WORK, DATA

TAG = sys.argv[1] if len(sys.argv) > 1 else "refit_n12_nb20_s8_sig0.1"
EXF = sys.argv[2] if len(sys.argv) > 2 else None
EB = np.arange(0.0, 21.0, 0.25)


def shell(Ek, W, wt, bins=EB):
    """state-weighted average of W in energy bins (W at grid states, weights = star sizes)."""
    idx = np.digitize(Ek.ravel(), bins) - 1
    w = np.repeat(wt[:, None], Ek.shape[1], 1).ravel()
    num = np.bincount(idx, weights=(W.ravel() * w), minlength=len(bins))[:len(bins)]
    den = np.bincount(idx, weights=w, minlength=len(bins))[:len(bins)]
    with np.errstate(invalid="ignore", divide="ignore"):
        return num / den, den


def main():
    d = np.load(os.path.join(WORK, f"ii_{TAG}.npz"))
    g = Grid(int(d["n"]))
    E = d["E"]
    Eirr = E[g.irr]
    Ek = [Eirr[:, NV:] - EG, -Eirr[:, :NV]]
    out = {"E": (EB + 0.125).tolist(), "scr": [str(s) for s in d["scr"]]}
    for t, key in ((0, "tot_e"), (1, "tot_h")):
        for iv, s in enumerate(d["scr"]):
            m, den = shell(Ek[t], d[key][iv], g.weight)
            out[f"W_{'eh'[t]}_{s}"] = np.nan_to_num(m).tolist()
        # spread (k dependence) at a few energies for the primary screening
        sp = {}
        for E0 in (2.0, 3.0, 5.0, 8.0):
            sel = np.abs(Ek[t] - E0) < 0.25
            v = d[key][0][sel]
            v = v[v > 0]
            if len(v) > 3:
                sp[str(E0)] = [float(np.percentile(v, 10)), float(np.median(v)), float(np.percentile(v, 90))]
        out[f"spread_{'eh'[t]}"] = sp
    # Keldysh/Kane fits to the primary shell average, E in [E_g, 6] eV: W = P (E - E_th)^a
    for t in "eh":
        Wm = np.array(out[f"W_{t}_cap"])
        x = EB + 0.125
        sel = (x > 1.4) & (x < 6.0) & (Wm > 0)
        f = lambda xx, lp, a, eth: lp + a * np.log(np.maximum(xx - eth, 1e-6))
        try:
            p, _ = curve_fit(f, x[sel], np.log(Wm[sel]), p0=[np.log(1e12), 3.0, 1.1],
                             bounds=([0, 0.5, 0.5], [80, 10, 1.6]))
            out[f"fit_{t}"] = dict(P=float(np.exp(p[0])), a=float(p[1]), Eth=float(p[2]))
        except Exception as e:  # noqa: BLE001
            out[f"fit_{t}"] = str(e)
    if EXF:
        x = np.load(EXF)
        rx = {}
        for t, nb in (("e", None), ("h", None)):
            raw = x[f"{t}_raw_cap"]                  # (nr, 4, nb): sum d, sum f, ...
            Eks = Ek[0] if t == "e" else Ek[1]
            D = raw[:, 0, :]
            F = raw[:, 1, :]
            idx = np.digitize(Eks.ravel(), EB) - 1
            wt = np.repeat(g.weight[:, None], Eks.shape[1], 1).ravel()
            num = np.bincount(idx, weights=F.ravel() * wt, minlength=len(EB))[:len(EB)]
            den = np.bincount(idx, weights=2 * D.ravel() * wt, minlength=len(EB))[:len(EB)]
            with np.errstate(invalid="ignore", divide="ignore"):
                r = num / den
            # GD sampled vs factorised (check): shell averages
            GDs, _ = shell(Eks, np.nan_to_num(x[f"{t}_GD_cap"]), g.weight)
            out[f"GDsampled_{t}"] = np.nan_to_num(GDs).tolist()
            # pooled ratio of sums in 1 eV windows (sampling noise); windows whose sampled direct weight is below
            # 2 % of the 3-4 eV window take the value of the nearest robust window (threshold region)
            ker = np.ones(5)
            numw = np.convolve(np.pad(num, 2), ker, mode="valid")
            denw = np.convolve(np.pad(den, 2), ker, mode="valid")
            with np.errstate(invalid="ignore", divide="ignore"):
                rw = numw / denw
            ref = denw[(EB > 3) & (EB < 4)].mean()
            ok = np.isfinite(rw) & (denw > 0.02 * ref) & (EB >= 2.5)
            rs = np.interp(EB, EB[ok], rw[ok])
            rs = np.clip(rs, 0.5, 1.5)
            rx[t] = rs
            out[f"Rx_{t}"] = rs.tolist()
            out[f"Rx_{t}_raw"] = np.nan_to_num(r).tolist()
            raw_r = x[f"{t}_raw_resta"]
            num = np.bincount(idx, weights=raw_r[:, 1, :].ravel() * wt, minlength=len(EB))[:len(EB)]
            den = np.bincount(idx, weights=2 * raw_r[:, 0, :].ravel() * wt, minlength=len(EB))[:len(EB)]
            with np.errstate(invalid="ignore", divide="ignore"):
                out[f"Rx_{t}_resta_raw"] = np.nan_to_num(num / den).tolist()
        np.savez(os.path.join(DATA, f"rx_{TAG}.npz"), Ebins=EB + 0.125, Rx_e=rx["e"], Rx_h=rx["h"])
    json.dump(out, open(os.path.join(DATA, f"rates_{TAG}.json"), "w"), indent=1)
    for t in "eh":
        print(t, "fit", out[f"fit_{t}"])
        for E0 in (1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 15.0, 18.0):
            j = int(np.argmin(np.abs(EB + 0.125 - E0)))
            s = " ".join(f"{sv}={out[f'W_{t}_{sv}'][j]:.2e}" for sv in out["scr"])
            ex = f" Rx={out[f'Rx_{t}'][j]:.2f} GDs/GD={out[f'GDsampled_{t}'][j] / max(out[f'W_{t}_cap'][j], 1e-30):.2f}" \
                if EXF else ""
            print(f"  {t} E={E0:5.2f}: {s}{ex}")
        print("  spread", out[f"spread_{t}"])


if __name__ == "__main__":
    main()
