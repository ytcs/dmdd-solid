"""FBC step 5b: run the full-band cascade for the seeds of seeds.py over omega = 2-20 eV, and the one-sided
high-energy runs for eps_eh and F_eh.  One configuration per call; results in data/mc_<name>.npz.
Run: python3 run_mc.py NAME [key=value ...]
  keys: ii (ii tag), seeds (seeds tag), phonon (refit|scissor), scr (0..3), dscale, xiscale, rx (0/1), mode (full|eo),
        phon (0/1: phonon emission on/off), nev (events per omega and seed), types (comma list), he (0/1: high-energy runs),
        omegas (all|coarse)
"""
import fbc_common  # noqa: F401
import os
import sys
import time
import json
import numpy as np
from fbc_common import WORK, DATA, EG, NV
from mc import Model, pn

NAME = sys.argv[1]
cfg = dict(ii="refit_n12_nb20_s8_sig0.1", seeds="refit_n12_m100_q4", phonon="refit", scr="0", dscale="1",
           xiscale="1", rx="1", mode="full", phon="1", nev="10000", types="heavy,light,photon", he="1",
           omegas="all", rxfile="", nhe="40000", seed="1", hedos="band", temp="0", dse="", dsh="", wlo="1", whi="1", off="0")
for a in sys.argv[2:]:
    k, v = a.split("=")
    cfg[k] = v


ERRMAX = [0.0]


def main():
    t0 = time.time()
    rng = np.random.default_rng(int(cfg["seed"]))
    rxf = cfg["rxfile"] or os.path.join(DATA, f"rx_{cfg['ii']}.npz")
    M = Model(cfg["ii"], exch_file=rxf if (cfg["rx"] == "1" and os.path.exists(rxf)) else None,
              phonon=cfg["phonon"], scr=int(cfg["scr"]), dscale=float(cfg["dscale"]), xiscale=float(cfg["xiscale"]),
              phonons_on=cfg["phon"] == "1", hedos=cfg["hedos"], temp=float(cfg["temp"]),
              dscale_e=float(cfg["dse"]) if cfg["dse"] else None, dscale_h=float(cfg["dsh"]) if cfg["dsh"] else None,
              wlo=float(cfg["wlo"]), whi=float(cfg["whi"]))
    print(f"model loaded {time.time() - t0:.0f} s (R_x {'on' if M.Rx is not None else 'off'})", flush=True)
    S = np.load(os.path.join(WORK, f"seeds_{cfg['seeds']}.npz"))
    oms = S["omegas"]
    if cfg["omegas"] == "coarse":
        oms = oms[::2]
    nev = int(cfg["nev"])
    res = {}
    for ty in cfg["types"].split(","):
        P, mean, var, part, nf = [], [], [], [], []
        for o in oms:
            if ty == "photonfine" or ty.startswith("H:"):
                # energy split from a share histogram (photon_fine.py 28^3, or 'H:<file>:<key>' e.g. the 20^3
                # stage-1 seeds); labels random on the shell (memory negligible, sec. 6)
                if ty == "photonfine":
                    H = np.load(os.path.join(WORK, "photon_fine_refit_n28.npz"))["H"]
                else:
                    _, fn, key = ty.split(":")
                    H = np.load(os.path.join(WORK, fn))[key]
                j = int(round(o / 0.05))
                row = H[j - 2:j + 3].sum(0)
                ex = o - EG
                Eb = (np.arange(len(row)) + 0.5) * 0.05
                w = np.where((Eb < ex) & (Eb > 0), row, 0.0)
                if w.sum() <= 0:
                    w = np.where(Eb < ex, 1.0, 0.0)
                pick = rng.choice(len(w), nev, p=w / w.sum())
                Ee = np.clip(Eb[pick] + (rng.random(nev) - 0.5) * 0.05, 0, ex)
                en = np.stack([Ee, ex - Ee]).T
                ke, be = M.relabel(0, en[:, 0], rng)
                kh, bh = M.relabel(1, en[:, 1], rng)
                seeds = dict(Ee=en[:, 0], Eh=en[:, 1], ke=ke, be=be, kh=kh, bh=bh)
            else:
                # v2: the stored seed samples are ordered by q sample (radial bin), so any subset must be a random
                # one: fixed permutation, then the slice [off, off + nev) (independent seed draws for off = 0 / nev)
                o0 = int(cfg["off"])
                ntot = len(S[f"eng_{ty}_{o}"])
                perm = np.random.default_rng(12345).permutation(ntot)[o0:o0 + nev]
                lab = S[f"lab_{ty}_{o}"][perm]
                en = S[f"eng_{ty}_{o}"][perm].astype(float)
                seeds = dict(Ee=en[:, 0], Eh=en[:, 1], ke=lab[:, 0], be=lab[:, 1], kh=lab[:, 2], bh=lab[:, 3])
            r = M.run(seeds, rng, mode=cfg["mode"])
            N = r["N"]
            # energy identity
            err = np.abs(N * EG + r["Eph"] + r["Eres"] - (en.sum(1) + EG)).max()     # seeds carry omega - E_g
            assert err < 1e-9, f"energy identity violated: {err}"
            ERRMAX[0] = max(ERRMAX[0], err)
            P.append(pn(N, 16))
            mean.append(N.mean())
            var.append(N.var())
            part.append([N.mean() * EG, r["Eph"].mean(), r["Eres"].mean()])
            nf.append(r["nfirst"].mean())
        ty = ty.replace(":", "_").replace(".npz", "")
        res[ty] = dict(P=np.array(P), mean=np.array(mean), var=np.array(var), part=np.array(part), nfirst=np.array(nf))
        print(f"{ty} done {time.time() - t0:.0f} s; <N>(5, 10, 20 eV) = "
              f"{np.interp([5, 10, 20], oms, res[ty]['mean']).round(3)}", flush=True)
    he = {}
    if cfg["he"] == "1":
        nhe = int(cfg["nhe"])
        # one-sided seeds: electron with omega - E_g, hole at the valence maximum (book sec. 18.2)
        kvbm = int(np.argmin(np.abs(M.Ek[1][:, 3]).ravel()))
        for o in (25.0, 50.0, 100.0):
            Ee = np.full(nhe, o - EG)
            seeds = dict(Ee=Ee, Eh=np.zeros(nhe), ke=np.zeros(nhe, int), be=np.zeros(nhe, int),
                         kh=np.full(nhe, kvbm), bh=np.full(nhe, 3))
            if o - EG <= 19.5:
                seeds["ke"], seeds["be"] = M.relabel(0, Ee, rng)
            r = M.run(seeds, rng, mode=cfg["mode"])
            N = r["N"]
            err = np.abs(N * EG + r["Eph"] + r["Eres"] - o).max()
            assert err < 1e-9
            ERRMAX[0] = max(ERRMAX[0], err)
            he[o] = dict(mean=N.mean(), var=N.var(), n=nhe, Eph=r["Eph"].mean(), Eres=r["Eres"].mean(),
                         var_Eph=r["Eph"].var(), var_Eres=r["Eres"].var(), cov=np.cov(r["Eph"], r["Eres"])[0, 1])
            print(f"one-sided {o} eV: <N> = {N.mean():.4f}, Var = {N.var():.4f} ({time.time() - t0:.0f} s)", flush=True)
        o1, o2 = 50.0, 100.0
        eps = (o2 - o1) / (he[o2]["mean"] - he[o1]["mean"])
        F = (he[o2]["var"] - he[o1]["var"]) / (he[o2]["mean"] - he[o1]["mean"])
        # errors: mean err sigma/sqrt(n); var err var*sqrt(2/(n-1)) (Gaussian approx)
        dm = np.hypot(np.sqrt(he[o2]["var"] / nhe), np.sqrt(he[o1]["var"] / nhe))
        dv = np.hypot(he[o2]["var"] * np.sqrt(2 / nhe), he[o1]["var"] * np.sqrt(2 / nhe))
        Dn = he[o2]["mean"] - he[o1]["mean"]
        he["eps"], he["deps"] = eps, eps * dm / Dn
        he["F"], he["dF"] = F, np.hypot(dv / Dn, F * dm / Dn)
        he["bN"] = he[o2]["mean"] - o2 / eps
        print(f"eps_eh = {eps:.4f} +- {he['deps']:.4f} eV, F_eh = {F:.4f} +- {he['dF']:.4f}, b_N = {he['bN']:.3f}")
    out = dict(cfg=json.dumps(cfg), omegas=oms, energy_err=ERRMAX[0])
    for ty, r in res.items():
        for k, v in r.items():
            out[f"{ty}_{k}"] = v
    out["he"] = json.dumps({str(k): v for k, v in he.items()}, default=float)
    np.savez(os.path.join(DATA, f"mc_{NAME}.npz"), **out)
    print(f"total {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
