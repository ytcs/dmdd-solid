import re,sys,numpy as np
def parse(f):
    t=open(f).read().split('End of band structure calculation')[1].split('Writing')[0]
    parts=re.split(r'\n\s*k =',t)[1:]
    K=[];E=[]
    for p in parts:
        head,rest=p.split('\n',1)
        nums=re.findall(r'-?\d+\.\d+',head.split('(')[0].replace('-',' -'))
        K.append([float(x) for x in nums[:3]]); E.append([float(x) for x in re.findall(r'-?\d+\.\d+',rest.replace('-',' -'))])
    n=min(len(e) for e in E); return np.array(K),np.array([e[:n] for e in E])
if __name__=='__main__':
    K,E=parse(sys.argv[1]); nv=int(sys.argv[2])
    vbm=E[:,nv-1].max(); ic=E[:,nv].argmin()
    print('nk',len(K),'VBM',vbm,'at',K[E[:,nv-1].argmax()],'CBM',E[ic,nv],'at',K[ic],'Eg',round(E[ic,nv]-vbm,4))
    for lab,k in [('G',[0,0,0]),('X',[1,0,0]),('L',[.5,.5,.5])]:
        i=np.where(np.all(abs(K-k)<1e-4,1))[0]
        if len(i): i=i[0]; print(lab,'c-VBM',np.round(E[i,nv:nv+3]-vbm,4),'v',np.round(E[i,nv-3:nv]-vbm,4))
