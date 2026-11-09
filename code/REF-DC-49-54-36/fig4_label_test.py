"""Referee: does Fig.4 decide which Fig.3 label is wrong? sigma_lim ratio heavy/light at 1 keV must equal sqrt(R456_light/R456_heavy) because N ~ sigma^2 R for both mediators.
Raster limit curves read by colour on the embedded image; R_Z bin heights from the vector path of Fig.3 right."""
import numpy as np, subprocess, tempfile, os, svgtools as t, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
T='/home/ytc/paer-work/lit/dc54/2401.11971/tex/'; S=sys.argv[1]
def curve(pdf,top,bot,xl,xr,ytop,ybot):
    pass
out={}
for name in ('heavy_limit_reply2','light_limit_reply2'):
    png=S+name+'-r300'
    subprocess.run(['pdftocairo','-png','-r','300','-singlefile',T+name+'.pdf',png],check=True)
    im=np.asarray(Image.open(png+'.png').convert('RGB')).astype(int); out[name]=im; print(name,im.shape)
    # axes frame: dark columns/rows
    dark=(im.sum(2)<150)
    cols=np.where(dark.mean(0)>.5)[0]; rows=np.where(dark.mean(1)>.5)[0]
    print(' frame cols',cols[:3],cols[-3:],'rows',rows[:3],rows[-3:])
    x0,x1=cols[0],cols[-1]; y0,y1=rows[0],rows[-1]
    R=(im[:,:,0]>190)&(im[:,:,1]<70)&(im[:,:,2]<70)   # solid red line (214,39,40)
    dec=(-27,-36) if 'heavy' in name else (-26,-32)
    res=[]
    for mk in (1.2,1.5,2):
        x=int(x0+(x1-x0)*np.log10(mk)/3); ys=np.where(R[y0:y1,x-1:x+2].any(1))[0]+y0
        if len(ys)==0: res.append((mk,None)); continue
        yc=np.median(ys); val=10**(dec[0]+(dec[1]-dec[0])*(yc-y0)/(y1-y0)); res.append((mk,val))
    print(' limit(m[keV]):',res)
    m=np.array([a for a,b in res if b]); v=np.array([b for a,b in res if b]); c=np.polyfit(np.log10(m),np.log10(v),1); out[name+'_1keV']=10**np.polyval(c,0); print(' extrapolated to 1 keV: %.3e'%out[name+'_1keV'])
ps=t.load(S+'dRdQ_reply.svg')
EX={3:57.71,4:63.03,5:65.56,6:67.73}
H={}
for lab,col in (('light','12.156677'),('heavy','83.920288')):
    q=[p for p in ps if p['stroke'] and col in p['stroke'] and len(p['pts'])>5][0]['pts']
    # step path: bin Z spans x in [Z-.5,Z+.5]; x calibration: 10 units/...; 94.93->Z=1? use 40.52 per 5?
    xs=q[:,0]; ys=q[:,1]; Rz={}
    for Z in range(1,12):
        xz=94.93+(Z-1)*40.52   # major ticks 94.93,135.45,175.96 are Z=1,2,3
        i=np.where((xs[:-1]<xz)&(xs[1:]>=xz))[0]
        if len(i): Rz[Z]=10**(-(ys[i[0]]-93.18)/123.04)
    H[lab]=Rz; print(lab,{k:round(v,4) for k,v in Rz.items()})
e=lambda R:sum(R[z]*EX[z] for z in (4,5,6))
rL,rH=e(H['light']),e(H['heavy'])
print('sum_Z heavy (display)',sum(H['heavy'].values()),' sum_Z light',sum(H['light'].values()))
pub=out['heavy_limit_reply2_1keV']/out['light_limit_reply2_1keV']
for lab,sc in (('x10^2 as printed',100),('x10^1',10)):
    print(lab,'predicted sigma_H/sigma_L = %.2f ; published %.2f'%(np.sqrt(rL/(rH/sc)),pub))
