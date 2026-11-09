"""Derived numbers for the return: rate crossing energies, the effective random-k constant A(E) of the full-band kernels
(book eq:18.1-randomk inverted, as Nielsen-Fischetti arXiv:2610.16949 Eq. (11)), phonon-competition and photon-vs-DM
statistics, per-omega tables with envelopes.  Writes data/derived.json.  Run: python3 derived.py
"""
import fbc_common  # noqa: F401
import os
import json
import numpy as np
from fbc_common import DATA, EG

TAG = "refit_n12_nb20_s8_sig0.1"


def main():
    r = json.load(open(os.path.join(DATA, f"rates_{TAG}.json")))
    ph = np.load(os.path.join(DATA, "phonon_refit.npz"))
    S = json.load(open(os.path.join(DATA, "summary.json")))
    E = np.array(r["E"])
    out = {}
    for t, nm in (("e", "e"), ("h", "h")):
        Wph = ph[f"W_{nm}"].sum(0) + ph[f"Wac_{nm}"]
        wph = np.interp(E, ph["E"], Wph)
        rx = np.array(r[f"Rx_{t}"])
        for s in ("cap", "resta", "rpa0", "rpaw"):
            Wii = np.array(r[f"W_{t}_{s}"]) * rx
            ratio = Wii / wph
            ok = (E > 1.5) & (E < (18 if t == "e" else 12))
            # crossing W_ii = W_ph and the 1 % point
            def cross(level):
                i = np.where(ok & (ratio >= level))[0]
                if not len(i):
                    return None
                i = i[0]
                return float(np.interp(np.log(level), np.log(ratio[i - 1:i + 1] + 1e-300), E[i - 1:i + 1]))
            out[f"cross_{t}_{s}"] = cross(1.0)
            out[f"p1pct_{t}_{s}"] = cross(0.01 / 0.99)
            # A(E) = (W_ph/W_ii) (2 pi/105) (E - E_g)^{7/2} / (E - 0.063)^{1/2}
            A = (wph / np.maximum(Wii, 1e-300)) * (2 * np.pi / 105) * np.maximum(E - EG, 0) ** 3.5 / np.sqrt(np.maximum(E - 0.063, 1e-9))
            out[f"A_{t}_{s}"] = {f"{x:.2f}": float(A[np.argmin(np.abs(E - x))]) for x in (2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0)}
        out[f"Wph_{t}"] = {f"{x:.1f}": float(np.interp(x, ph["E"], Wph)) for x in (1, 2, 3, 5, 8)}
        out[f"Rx_{t}"] = {f"{x:.1f}": float(np.interp(x, E, rx)) for x in (2.5, 3, 4, 6, 10, 15)}
    oms = np.array(S["omegas"])
    # phonon competition: P(N >= 2) with and without phonon emission
    nop = S["variants"].get("nophonon")
    if nop:
        out["phcomp"] = {f"{o}": dict(full=S["Pge2"]["heavy"][int(np.argmin(np.abs(oms - o)))],
                                       nophon=nop["Pge2_heavy"][int(np.argmin(np.abs(oms - o)))],
                                       mean_full=S["mean"]["heavy"][int(np.argmin(np.abs(oms - o)))],
                                       mean_nophon=nop["mean_heavy"][int(np.argmin(np.abs(oms - o)))],
                                       tv=nop["tv_heavy"][int(np.argmin(np.abs(oms - o)))])
                         for o in (2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 8.0)}
    pf = os.path.join(DATA, "mc_photonfine.npz")
    if os.path.exists(pf):
        d = np.load(pf)
        P = d["photonfine_P"]
        H = np.array(S["P_heavy"])
        L = np.array(S["P_light"])
        def tvv(a, b):
            m = min(a.shape[1], b.shape[1])
            return 0.5 * np.abs(a[:, :m] - b[:, :m]).sum(1)
        tv_h = tvv(P, H)
        tv_l = tvv(P, L)
        sel = oms >= 3.4
        out["photon_vs_dm"] = dict(max_heavy=float(tv_h[sel].max()), at=float(oms[sel][np.argmax(tv_h[sel])]),
                                   max_light=float(tv_l[sel].max()),
                                   rep={f"{o}": float(tv_h[int(np.argmin(np.abs(oms - o)))]) for o in (4.5, 5, 6, 8, 10, 15, 20)},
                                   P2ratio_5=float((1 - P[:, :2].sum(1))[np.argmin(np.abs(oms - 5))] /
                                                   (1 - H[:, :2].sum(1))[np.argmin(np.abs(oms - 5))]),
                                   mean=dict(zip([f"{o}" for o in (5, 10, 15, 20)],
                                                 [float(d["photonfine_mean"][np.argmin(np.abs(oms - o))]) for o in (5, 10, 15, 20)])))
        out["P_photonfine"] = P[:, :8].tolist()
    # per-omega table with the all-variant envelope of P(N) bins for the heavy seed
    var = S["variants"]
    labs = [l for l in ("resta", "rpa0", "rpaw", "D2x0.6", "D2x1.6", "scissor", "noexch", "rxthr", "half2") if l in var]
    tab = {}
    for o in (3.0, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 10.0, 12.0, 15.0, 20.0):
        i = int(np.argmin(np.abs(oms - o)))
        rows = {"P": S["P_heavy"][i][:7], "mean": S["mean"]["heavy"][i], "Pge2": S["Pge2"]["heavy"][i],
                "mean_lo": min(var[l]["mean_heavy"][i] for l in labs), "mean_hi": max(var[l]["mean_heavy"][i] for l in labs),
                "Pge2_lo": min(var[l]["Pge2_heavy"][i] for l in labs), "Pge2_hi": max(var[l]["Pge2_heavy"][i] for l in labs),
                "tv_book": S["tv"]["bookDM"][i], "tv_rk1": S["tv"]["rk1"][i], "tv_rkinf": S["tv"]["rkinf"][i],
                "tv_step": S["tv"]["step"][i], "P_book": S["P_book"][i][:7], "mean_book": S["mean_book"][i],
                "tv_book_lo": min(var[l]["tvbook_heavy"][i] for l in labs),
                "tv_book_hi": max(var[l]["tvbook_heavy"][i] for l in labs),
                "tv_step_lo": min(var[l]["tvstep_heavy"][i] for l in labs),
                "tv_step_hi": max(var[l]["tvstep_heavy"][i] for l in labs),
                "tv_eo": var["eo"]["tv_heavy"][i] if "eo" in var else None,
                "tv_half2": var["half2"]["tv_heavy"][i] if "half2" in var else None}
        tab[f"{o}"] = rows
    out["table"] = tab
    json.dump(out, open(os.path.join(DATA, "derived.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k not in ("table", "P_photonfine")}, indent=0)[:4000])


if __name__ == "__main__":
    main()
