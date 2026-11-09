"""Extract published curves of 1910.02091 from the vector figures of the arXiv source (pdftocairo -> SVG).
Usage: extract_published.py <dir with *.svg> ; writes data/pub_*.csv (m [keV or eV], y)."""
import sys, numpy as np, svgcurves as S
F = sys.argv[1].rstrip('/')+'/'
BLUE='rgb(36.839294%, 50.67749%, 70.977783%)'; GREEN='rgb(56.015015%, 69.155884%, 19.487%)'; ORANGE='rgb(88.070679%, 61.102295%, 14.202881%)'
# axis calibration (tick positions read from the same SVGs)
def scat(q):   # x: 10 keV at 114.2, 100 at 224.3, 1000 at 334.4 ; y: 1e-36 at 18.6, 27.52/decade
    return 10**(1+(q[:,0]-114.21)/110.1), 10**(-36-(q[:,1]-18.6)/27.52)
def absn(q):   # x: 0.01 eV at 101.2 .. 10 eV at 342.1 ; y: 1e-9 at 21, 31.2/decade
    return 10**(-2+(q[:,0]-101.2)/80.3), 10**(-9-(q[:,1]-21.0)/31.22)
def get(svg,col,dash):
    ps=S.paths(F+svg+'.svg'); r=[p for p in ps if p['color']==col and len(p['pts'])>15 and (p['dash'] is not None)==dash]
    return r
for name,svg,col,dash in [('ZrTe5_th','Summary_scattering',BLUE,False),('ZrTe5_exp','Summary_scattering',BLUE,True),
                          ('BNQ','Summary_scattering',GREEN,False),('Yb','Summary_scattering',ORANGE,False)]:
    r=get(svg,col,dash); print(name,[len(p['pts']) for p in r])
    q=r[0]['pts']; x,y=scat(q); m=(y>1e-46)&(y<1e-36)
    np.savetxt(f'data/pub_scat_{name}.csv',np.c_[x[m],y[m]],header='m_chi[keV] sigma_e[cm^2] (Summary_scattering.pdf, 3 events, 1 kg yr)',delimiter=',')
    print(' ',x[m].min(),x[m].max(),y[m].min())
for name,col,dash in [('ZrTe5_th',BLUE,False),('ZrTe5_exp',BLUE,True),('BNQ',GREEN,False),('Yb',ORANGE,False)]:
    r=get('Summary_absorption',col,dash); q=r[0]['pts']; x,y=absn(q)
    np.savetxt(f'data/pub_abs_{name}.csv',np.c_[x,y],header='m_A[eV] eps (Summary_absorption.pdf, 3 events, 1 kg yr)',delimiter=',')
    print(name,len(x),x.min(),x.max(),y.min())
