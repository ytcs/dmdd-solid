"""Vector extraction of 2401.11971 Fig. 2 (flux) and Fig. 3 (dR/domega, R_Z) from the arXiv source PDFs."""
import sys, re, numpy as np, svgcurves as S
F=sys.argv[1].rstrip('/')+'/'
BLUE='rgb(12.156677%, 46.665955%, 70.587158%)'; RED='rgb(83.920288%, 15.293884%, 15.686035%)'

def save(svg,fx,fy,sel,name,hdr):
    ps=S.paths(F+svg+'.svg')
    for lab,col,dash in sel:
        q=[p for p in ps if p['color']==col and p['dash']==dash and len(p['pts'])>2][0]['pts']
        np.savetxt(f'data/pub_{name}_{lab}.csv',np.c_[fx(q[:,0]),fy(q[:,1])],delimiter=',',header=hdr)
fx=lambda x:10**(-7+(x-84.59)/63.691); fy=lambda y:10**(2-(y-14.39)/23.73)
save('CRDM_flux_reply2',fx,fy,[('light_1keV',BLUE,None),('light_10keV',BLUE,'7.4 3.2'),('light_me',BLUE,'12.8 3.2 2 3.2'),
     ('heavy_1keV',RED,None),('heavy_10keV',RED,'7.4 3.2'),('heavy_me',RED,'12.8 3.2 2 3.2')],'flux','T_chi[GeV], T dPhi/dT [cm^-2 s^-1] (Fig 2, sigma=1e-34)')
fx=lambda x:(x-66.25)/8.9174; fy=lambda y:(346.4-y)/474.64
save('dRdomega_reply',fx,fy,[('light',BLUE,None),('heavy_x100',RED,None)],'dRdw','omega[eV], dR/domega [kg^-1 yr^-1 eV^-1] (Fig 3 left, m=1keV, sigma=1e-34)')
