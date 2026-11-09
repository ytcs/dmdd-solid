"""FBC step 5: full-band cascade Monte Carlo.

State of a carrier: type (electron/hole), continuous kinetic energy E (exact energy bookkeeping), and a grid label
(k, band) with e_label within DW of E.  At each collision (only ratios of rates matter, book sec. 18.1):
  p_ii = W_ii(label) / (W_ii(label) + W_ph(E)),   W_ii = R_x(E) * Gamma_D(label)   (ii.py, exch.py),
  phonon: mode j with probability W_j(E)/W_ph(E); E -= hbar omega_j; intervalley/optical modes put the carrier on a
     random state of the new shell (random k: exact for q-independent coupling); acoustic emission keeps the label
     (small q) unless its energy has drifted by more than DW_AC;
  impact ionization: (p, n1') drawn from the carrier's own golden-rule distribution (tab_e/tab_h of ii.py, rotated
     from the irreducible wedge), the pair (k2, v, c) at momentum p and energy omega drawn from the pair table of p
     with weight sum_G |w(p+G)|^2 |rho_cv(k2, p+G)|^2 in a window +-DWP (interference between the carrier and pair
     vertices neglected in the choice of the pair only); the three product energies are rescaled to E - E_g exactly.
A carrier is terminal when E < E_g (no further ionization is possible); its E is the residual kinetic energy.
Electrons above E_TOP (beyond the rate tables) ionize with probability one and split E - E_g with the joint density
g_e g_e g_h of the band DOS (high-energy rule, used only for omega > 20 eV, i.e. for eps and F).
Energy identity per event: omega = N E_g + E_ph(above threshold) + E_res, checked to 1e-9 eV.
Mode 'full' (k-resolved first generation, labels kept) or 'eo' (energy-only: every carrier re-drawn on its shell
before every collision = the iso-energy reduction eq:18.1-isoenergy of the same kernels).
"""
import fbc_common  # first: single-threaded BLAS  # noqa: F401
import os
import numpy as np
from fbc_common import Grid, EG, NV, WORK, DATA

DW = 0.05          # label window (eV)
DW_AC = 0.10
DWP = 0.10         # pair window (eV)
E_TOP = 19.5       # electrons above: high-energy rule


class Model:
    def __init__(self, ii_tag, exch_file=None, phonon="refit", scr=0, dscale=1.0, xiscale=1.0, rx=True,
                 phonons_on=True, load_tables=True, hedos="band", temp=0.0, dscale_e=None, dscale_h=None,
                 wlo=1.0, whi=1.0):
        d = np.load(os.path.join(WORK, f"ii_{ii_tag}.npz"))
        self.n = int(d["n"])
        self.g = Grid(self.n)
        g = self.g
        self.E = d["E"]
        self.ce = d["ce"]
        self.ne = len(self.ce)
        self.ecb = float(np.min(self.E[:, NV]))     # grid CBM; kinetic energies measured from the model CBM below
        self.ecb = EG                                # bands are calibrated: CBM at E_g above the VBM
        # kinetic energies per state
        self.Ek = [self.E[:, NV:] - self.ecb, -self.E[:, :NV]]                  # (N, ne), (N, NV)
        self.nb = [self.ne, NV]
        # shell sampling: sorted energies of all states
        self.sorted = []
        for t in (0, 1):
            fl = self.Ek[t].ravel()
            o = np.argsort(fl)
            self.sorted.append((fl[o], o))
        # rates per state
        tot = [d["tot_e"][scr], d["tot_h"][scr]]
        self.Wd = [tot[t][g.irr_of] for t in (0, 1)]                             # (N, nb)
        self.rx = rx
        self.Rx = None
        if exch_file is not None and rx:
            x = np.load(exch_file)
            self.Rx = (x["Ebins"], x["Rx_e"], x["Rx_h"])
        self.Wii = []
        for t in (0, 1):
            w = self.Wd[t].copy()
            if self.Rx is not None:
                w *= np.interp(self.Ek[t], self.Rx[0], self.Rx[1 + t])
            w[self.Ek[t] < EG] = 0.0
            # diagnostic rescalings of the ionization rate below 4.5 eV (wlo) and above 5 eV (whi) (v2, ref. A sec. 1)
            w[self.Ek[t] < 4.5] *= wlo
            w[self.Ek[t] > 5.0] *= whi
            self.Wii.append(w)
        # phonons
        ph = np.load(os.path.join(DATA, f"phonon_{phonon}.npz"))
        self.phE = ph["E"]
        self.phW, self.phL = [], []
        for t, nm in ((0, "e"), (1, "h")):
            ds = dscale if (dscale_e if t == 0 else dscale_h) is None else (dscale_e if t == 0 else dscale_h)
            Wem = ph[f"W_{nm}"] * ds          # per-carrier D^2 scale (v2: asymmetric e/h variants)
            hw = ph[f"hw_{nm}"]
            Lem = np.repeat(hw[:, None], len(self.phE), 1)
            if temp > 0:      # finite T: emission x (n+1), absorption x n into g(E + hbar w) (intervalley/optical)
                nB = 1 / np.expm1(hw / (8.617333e-5 * temp))
                # W_j(E) is proportional to g(E - hw); absorption needs g(E + hw): shift the emission table by 2 hw
                Wab = np.array([np.interp(self.phE + 2 * w, self.phE, Wj, right=0) for Wj, w in zip(Wem, hw)])
                W = np.vstack([Wem * (1 + nB[:, None]), Wab * nB[:, None], ph[f"Wac_{nm}"][None] * xiscale ** 2])
                L = np.vstack([Lem, -Lem, ph[f"lossac_{nm}"][None]])
            else:
                W = np.vstack([Wem, ph[f"Wac_{nm}"][None] * xiscale ** 2])
                L = np.vstack([Lem, ph[f"lossac_{nm}"][None]])
            if not phonons_on:
                W = W * 0
            self.phW.append(W)
            self.phL.append(L)
        self.dos = [ph["dos_e"], ph["dos_h"]]
        if hedos == "free":           # free-particle densities above E_TOP (high-energy-rule sensitivity)
            x = self.phE
            wv = x[np.flatnonzero(ph["dos_h"] > 0)[-1]]
            self.dos = [np.sqrt(x), np.sqrt(x) * (x <= wv)]
        if load_tables:
            self._tables(d)

    def _tables(self, d):
        g = self.g
        # carrier final-state CDF, rows (r, n1), columns (p, n1')
        self.cdf = []
        for t, key in ((0, "tab_e"), (1, "tab_h")):
            T = d[key].astype(np.float64)                     # (nr, nb, N, nb)
            nr, nb = T.shape[0], T.shape[1]
            T = T.reshape(nr * nb, -1)
            s = T.sum(1, keepdims=True)
            c = np.cumsum(T, axis=1) / np.where(s > 0, s, 1)
            c[s[:, 0] <= 0] = 1.0
            c = c + np.arange(nr * nb)[:, None]
            self.cdf.append((c.ravel(), nb, T.shape[1]))
            del T
        # pair tables of irreducible p
        pw, pde = d["pw"].astype(np.float64), d["pde"].astype(np.float64)    # (nI, N, ne, NV)
        nI = pw.shape[0]
        keys = (np.arange(nI)[:, None] * 100.0 + pde.reshape(nI, -1))
        order = np.argsort(keys, axis=None)
        self.pkeys = keys.ravel()[order]
        self.pcum = np.cumsum(pw.ravel()[order])
        self.porder = order                                      # flat index into (nI, N*ne*NV)
        self.pshape = pw.shape

    # ------------------------------------------------------------------ helpers
    def relabel(self, t, E, rng):
        Es, o = self.sorted[t]
        lo = np.searchsorted(Es, E - DW)
        hi = np.searchsorted(Es, E + DW)
        empty = hi <= lo
        idx = lo + np.floor(rng.random(len(E)) * np.maximum(hi - lo, 1)).astype(int)
        near = np.clip(np.searchsorted(Es, E), 0, len(Es) - 1)
        idx = np.where(empty, near, np.minimum(idx, len(Es) - 1))
        flat = o[idx]
        return flat // self.nb[t], flat % self.nb[t]

    def wph(self, t, E):
        W = self.phW[t]
        x = np.clip(E, self.phE[0], self.phE[-1])
        return np.array([np.interp(x, self.phE, w) for w in W])                 # (nmode, n)

    def sample_ii(self, t, k, b, rng):
        """final carrier label, momentum index p (full grid) for carriers of type t at labels (k, b)."""
        g = self.g
        cum, nb, ncol = self.cdf[t]
        r = g.irr_of[k]
        o = g.op_from_irr[k]
        row = r * nb + b
        pos = np.searchsorted(cum, row + rng.random(len(k)) * (1 - 1e-12))
        col = pos - row * ncol
        col = np.clip(col, 0, ncol - 1)
        p_r, b2 = col // nb, col % nb
        p = g.perm[o, p_r]
        sgn = -1 if t == 0 else 1
        k2 = g.index(g.i[k] + sgn * g.i[p])
        return k2, b2, p

    def sample_pair(self, p, omega, rng):
        g = self.g
        j = g.irr_of[p]
        o2 = g.op_from_irr[p]
        lo = np.searchsorted(self.pkeys, j * 100.0 + omega - DWP)
        hi = np.searchsorted(self.pkeys, j * 100.0 + omega + DWP)
        c0 = np.where(lo > 0, self.pcum[np.maximum(lo - 1, 0)], 0.0)
        c1 = self.pcum[np.maximum(hi - 1, 0)]
        bad = (hi <= lo) | (c1 <= c0)
        # fallback: widen window
        if bad.any():
            lo2 = np.searchsorted(self.pkeys, j[bad] * 100.0 + omega[bad] - 4 * DWP)
            hi2 = np.searchsorted(self.pkeys, j[bad] * 100.0 + omega[bad] + 4 * DWP)
            lo[bad], hi[bad] = lo2, hi2
            c0 = np.where(lo > 0, self.pcum[np.maximum(lo - 1, 0)], 0.0)
            c1 = self.pcum[np.maximum(hi - 1, 0)]
        u = c0 + rng.random(len(p)) * (c1 - c0)
        pos = np.clip(np.searchsorted(self.pcum, u), lo, np.maximum(hi - 1, lo))
        flat = self.porder[pos]
        nI, N, ne, nv = self.pshape
        jj, rest = np.divmod(flat, N * ne * nv)
        k2r, rest = np.divmod(rest, ne * nv)
        c, v = np.divmod(rest, nv)
        k2 = g.perm[o2, k2r]
        ke = g.index(g.i[k2] + g.i[p])
        return ke, c, k2, v

    def he_split(self, y, rng):
        """high-energy rule: split y among (e, e, h) with density g_e g_e g_h (rejection on the uniform simplex)."""
        out = np.zeros((len(y), 3))
        todo = np.arange(len(y))
        ge, gh = self.dos
        x = self.phE
        gmax_e, gmax_h = ge.max(), gh.max()
        while len(todo):
            u = rng.dirichlet([1, 1, 1], len(todo)) * y[todo, None]
            acc = (np.interp(u[:, 0], x, ge) * np.interp(u[:, 1], x, ge) * np.interp(u[:, 2], x, gh, right=0)
                   / (gmax_e ** 2 * gmax_h))
            ok = rng.random(len(todo)) < acc
            out[todo[ok]] = u[ok]
            todo = todo[~ok]
        return out

    # ------------------------------------------------------------------ cascade
    def run(self, seeds, rng, mode="full", maxsteps=200000):
        """seeds: dict with arrays Ee, Eh, ke, be, kh, bh (n events). Returns N, Eph, Eres per event."""
        n = len(seeds["Ee"])
        E = np.concatenate([seeds["Ee"], seeds["Eh"]]).astype(float)
        t = np.concatenate([np.zeros(n, int), np.ones(n, int)])
        k = np.concatenate([seeds["ke"], seeds["kh"]]).astype(int)
        b = np.concatenate([seeds["be"], seeds["bh"]]).astype(int)
        ev = np.concatenate([np.arange(n), np.arange(n)])
        N = np.ones(n, int)
        Eph = np.zeros(n)
        Eres = np.zeros(n)
        nfirst = np.zeros(n)          # diagnostics: II by first-generation (fresh) carriers
        fresh = np.ones(2 * n, bool)
        if mode == "eo":
            for tt in (0, 1):
                m = t == tt
                if m.any():
                    k[m], b[m] = self.relabel(tt, E[m], rng)
        for step in range(maxsteps):
            done = E < EG
            if done.any():
                np.add.at(Eres, ev[done], E[done])
                keep = ~done
                E, t, k, b, ev, fresh = E[keep], t[keep], k[keep], b[keep], ev[keep], fresh[keep]
            if len(E) == 0:
                break
            new = []
            for tt in (0, 1):
                m = np.flatnonzero(t == tt)
                if len(m) == 0:
                    continue
                Em = E[m]
                if tt == 0:
                    he = Em > E_TOP
                else:
                    he = np.zeros(len(m), bool)
                lo_ = ~he
                ml = m[lo_]
                if mode == "eo" and len(ml):
                    k[ml], b[ml] = self.relabel(tt, E[ml], rng)
                    fresh[ml] = False
                if len(ml):
                    Wii = self.Wii[tt][k[ml], b[ml]]
                    Wm = self.wph(tt, E[ml])
                    Wp = Wm.sum(0)
                    tot = Wii + Wp
                    stuck = tot <= 0
                    if stuck.any():                     # no channel open (phonons switched off): terminal
                        np.add.at(Eres, ev[ml[stuck]], E[ml[stuck]])
                        E[ml[stuck]] = -1.0
                    u = rng.random(len(ml)) * np.where(tot > 0, tot, 1)
                    isii = (u < Wii) & ~stuck
                    isph = ~isii & ~stuck
                    # ---- phonon emission
                    mp_ = ml[isph]
                    if len(mp_):
                        cw = np.cumsum(Wm[:, isph], axis=0)
                        uu = rng.random(len(mp_)) * cw[-1]
                        j = (uu[None, :] > cw).sum(0)
                        j = np.minimum(j, cw.shape[0] - 1)
                        x = np.clip(E[mp_], self.phE[0], self.phE[-1])
                        loss = np.array([np.interp(x[i], self.phE, self.phL[tt][j[i]]) for i in range(len(mp_))]) \
                            if False else self.phL[tt][j, np.clip(np.searchsorted(self.phE, x), 0, len(self.phE) - 1)]
                        loss = np.minimum(loss, E[mp_])          # (absorption: negative loss)
                        E[mp_] -= loss
                        np.add.at(Eph, ev[mp_], loss)
                        acn = j == (cw.shape[0] - 1)
                        rel = ~acn | (np.abs(self.Ek[tt][k[mp_], b[mp_]] - E[mp_]) > DW_AC)
                        rr = mp_[rel & (E[mp_] >= EG)]
                        if len(rr):
                            k[rr], b[rr] = self.relabel(tt, E[rr], rng)
                            fresh[rr] = False
                    # ---- impact ionization
                    mi = ml[isii]
                    if len(mi):
                        k2, b2, p = self.sample_ii(tt, k[mi], b[mi], rng)
                        if tt == 0:
                            om = self.E[k[mi], NV + b[mi]] - self.E[k2, NV + b2]
                        else:
                            om = self.E[k2, b2] - self.E[k[mi], b[mi]]
                        ke, c, kh, v = self.sample_pair(p, om, rng)
                        E1 = self.Ek[tt][k2, b2]
                        Ee = self.Ek[0][ke, c]
                        Eh = self.Ek[1][kh, v]
                        y = E[mi] - EG
                        s = np.maximum(E1 + Ee + Eh, 1e-12)
                        f = y / s
                        E[mi] = E1 * f
                        k[mi], b[mi] = k2, b2
                        np.add.at(nfirst, ev[mi[fresh[mi]]], 1)
                        fresh[mi] = True
                        np.add.at(N, ev[mi], 1)
                        new.append((Ee * f, np.zeros(len(mi), int), ke, c, ev[mi]))
                        new.append((Eh * f, np.ones(len(mi), int), kh, v, ev[mi]))
                # ---- high-energy electrons
                mh = m[he]
                if len(mh):
                    y = E[mh] - EG
                    xs = self.he_split(y, rng)
                    E[mh] = xs[:, 0]
                    np.add.at(N, ev[mh], 1)
                    lab = E[mh] <= E_TOP
                    if lab.any():
                        k[mh[lab]], b[mh[lab]] = self.relabel(0, E[mh[lab]], rng)
                    for col, tp in ((1, 0), (2, 1)):
                        Ex = xs[:, col]
                        kk = np.zeros(len(mh), int)
                        bb = np.zeros(len(mh), int)
                        okl = (Ex <= (E_TOP if tp == 0 else 99)) & (Ex >= 0)
                        if okl.any():
                            kk[okl], bb[okl] = self.relabel(tp, Ex[okl], rng)
                        new.append((Ex, np.full(len(mh), tp), kk, bb, ev[mh]))
            E = np.where(E < 0, -1.0, E)
            gone = E < 0
            if gone.any():
                keep = ~gone
                E, t, k, b, ev, fresh = E[keep], t[keep], k[keep], b[keep], ev[keep], fresh[keep]
            if new:
                E = np.concatenate([E] + [x[0] for x in new])
                t = np.concatenate([t] + [x[1] for x in new])
                k = np.concatenate([k] + [x[2] for x in new])
                b = np.concatenate([b] + [x[3] for x in new])
                ev = np.concatenate([ev] + [x[4] for x in new])
                fresh = np.concatenate([fresh] + [np.ones(len(x[0]), bool) for x in new])
        return dict(N=N, Eph=Eph, Eres=Eres, nfirst=nfirst)


def pn(N, nmax=40):
    return np.bincount(N, minlength=nmax)[:nmax] / len(N)


def tv(P, Q):
    m = max(len(P), len(Q))
    return 0.5 * np.abs(np.pad(P, (0, m - len(P))) - np.pad(Q, (0, m - len(Q)))).sum()
