"""Coherent zero-phonon Migdal response with the full RPA local-field matrix (EPM model of offdiag12.py),
against the incoherent forms (i) full single-site and (ii) diagonal (book form).
Weight for kick Q = k + G0 (k in mesh, G0 reciprocal vector), electron momenta p = k + G:
  W_coh = 3 (Qh.ph)(Qh.p'h) Z(p)Z(p') * 0.5*A_G A_G',  A_G = 2 cos((G-G0).tau)   (both atoms, coherent, DW = 1)
L_coh(Q,w) = (1/Omega) sum W_coh Sp(k,w);  incoherent L = (1/(N_k Omega)) sum_k sum W Sp  (offdiag12 convention).
"""
import os, sys, time, numpy as np
sys.path.insert(0, '/home/user/dmdd-solid/book/figscripts/ch12')
import offdiag12 as O
MG = O.MG
G0LIST = [np.array(v, float) for v in
          [(i, j, k) for i in range(-4, 5) for j in range(-4, 5) for k in range(-4, 5)]
          if (np.array(v)%2==0).all() or (np.array(v)%2==1).all()]   # fcc reciprocal lattice in 2pi/a units (all even or all odd)
G0LIST = [g for g in G0LIST if (g**2).sum() <= 16 + 1e-9]
wsel = O.WGRID >= O.EG_T
w4 = O.WGRID[wsel]**4

def analyse_coh(kvec, Mres, Mant):
    w = O.WGRID / O.HA; eta = O.ETA / O.HA; Eb = O.EB / O.HA
    P = kvec[None, :] + O.GL
    vC = 4*np.pi/((P**2).sum(1)*O.tpa**2); sv = np.sqrt(vC)
    pn = np.linalg.norm(P, axis=1); ph = P/pn[:, None]
    Z = MG.z_ion(pn*O.unit_eV)
    I = np.eye(O.NG)
    Ws = []; Qs = []
    for G0 in G0LIST:
        Q = kvec + G0
        Qn = np.linalg.norm(Q)
        if Qn < 1e-9: continue
        c = (ph @ (Q/Qn))*Z
        A = 2*np.cos(2*np.pi*((O.GL - G0) @ np.ones(3)/8.0))
        v = c*A
        Ws.append(3*0.5*np.outer(v, v)); Qs.append(Qn*O.unit_eV)
    Ws = np.array(Ws)
    # incoherent forms
    Wd, _, _ = O.weights(kvec)
    out_coh = np.zeros((len(Ws), len(w)))
    out_i = np.zeros(len(w)); out_ii = np.zeros(len(w)); head = np.zeros(len(w))
    for s in range(0, len(w), 120):
        ws = w[s:s+120]
        g_res = 1.0/(ws[:, None]-Eb[None, :]+1j*eta)
        g_ant = 1.0/(ws[:, None]+Eb[None, :]+1j*eta)
        R0 = (g_res @ Mres - g_ant @ Mant).reshape(len(ws), O.NG, O.NG)
        et = I[None] - sv[None, :, None]*R0*sv[None, None, :]
        E = np.linalg.inv(et)
        Sp = -(E - np.conj(np.swapaxes(E, 1, 2)))/2j
        out_coh[:, s:s+len(ws)] = np.real(np.einsum('qgh,wgh->qw', Ws, Sp))
        ip_ = np.real(np.einsum('gh,wgh->w', Wd['full_p'], Sp)); im_ = np.real(np.einsum('gh,wgh->w', Wd['full_m'], Sp))
        out_i[s:s+len(ws)] = 0.5*(ip_+im_)
        out_ii[s:s+len(ws)] = np.real(np.einsum('wgg->wg', Sp)*Z[None]**2).sum(1)
        head[s:s+len(ws)] = np.real(Sp[:, 0, 0])
    return np.array(Qs), out_coh, out_i, out_ii, head

def main():
    reps, wts = O.irreducible()
    t0 = time.time()
    rows = []
    acc_i = np.zeros(len(O.WGRID)); acc_ii = np.zeros(len(O.WGRID))
    for n, (iq, wq) in enumerate(zip(reps, wts)):
        kv = O.kpts[iq].copy(); onmesh = True
        if np.allclose(kv, 0):
            d = np.array([1.0, 0.37, 0.21]); kv = O.QG0*d/np.linalg.norm(d); onmesh = False
        Mr, Ma = O.chi0(kv, onmesh)
        Qs, oc, oi, oii, head = analyse_coh(kv, Mr, Ma)
        acc_i += wq*oi; acc_ii += wq*oii
        for Qn, o in zip(Qs, oc):
            rows.append((Qn, wq, o))
        np.save('cohrpa_head_%d.npy' % n, np.r_[np.linalg.norm(kv)*O.unit_eV, head])
        print(f'k {n+1}/{len(reps)} |k|={np.linalg.norm(kv)*O.unit_eV:.0f} eV w={wq} t={time.time()-t0:.0f}s', flush=True)
    Qn = np.array([r[0] for r in rows]); wq = np.array([r[1] for r in rows]); oc = np.array([r[2] for r in rows])
    np.savez('cohrpa_NK%d_GM%d.npz' % (O.NK, int(O.GM)), Q=Qn, wq=wq, coh=oc, inc_i=acc_i/O.NKT, inc_ii=acc_ii/O.NKT, w=O.WGRID)
    print('done', time.time()-t0)

if __name__ == '__main__':
    main()
