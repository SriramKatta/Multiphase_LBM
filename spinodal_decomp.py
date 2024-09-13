import matplotlib.pyplot as plt
import numpy as np
from D2Q9 import *
from pathlib import Path

itercount = []
domainsize = []

def spindecomp(nx, ny, nsteps, tau, rho, g, post, outfreq, experiment):
    f = np.zeros((nx, ny, ni))

    for i, w in zip(ei, ws):
        f[:, :, i] = rho * w
    
    feq = np.zeros_like(f)

    if(post):
        Path("./spindecom").mkdir(parents=True, exist_ok=True)
        fig, ax = plt.subplots(figsize=(10,10))

    for t in range(nsteps + 1):
        rho = np.sum(f,2)
        ux = np.sum(f* exs, 2)/ rho
        uy = np.sum(f* eys, 2)/ rho

        psi = 1 - np.exp(-rho)
        force = np.zeros((nx, ny, 2))
        for w, ex, ey in zip(ws, exs, eys):
            force[:,:, 0] += w*np.roll(np.roll(psi[:,:], ex, axis=0), ey, axis=1)*(-ex)
            force[:,:, 1] += w*np.roll(np.roll(psi[:,:], ex, axis=0), ey, axis=1)*(-ey)
        force[:,:,0] = np.multiply(-g*psi[:,:],force[:,:, 0])
        force[:,:,1] = np.multiply(-g*psi[:,:],force[:,:, 1])

        ueqx = ux + np.divide(tau*force[:,:,0],rho[:,:])
        ueqy = uy + np.divide(tau*force[:,:,1],rho[:,:])

        for i, ex, ey, w in zip(ei, exs, eys, ws):
            feq[:,:,i] = rho * w * ( 1 + 3*(ex*ueqx+ey*ueqy) + 9*(ex*ueqx+ey*ueqy)**2/2-3*(ueqx**2+ueqy**2)/2)
            
        f +=-(1.0/tau) * (f-feq)

        for i, ex, ey in zip(ei, exs, eys):
            f[:,:,i] = np.roll(f[:,:,i], ex, axis=0)
            f[:,:,i] = np.roll(f[:,:,i], ey, axis=1)

        if((t % outfreq) == 0 or t == nsteps) and (post):
            plt.cla()
            ax = plt.gca()
            im = ax.imshow(rho)
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            ax.set_title('Iteration ='+str(t))
            plt.savefig('./spindecom/Iteration_'+str(t))
            print('./spindecom/Iteration_'+str(t)+' of '+ str(nsteps))
        else:
            print(str(t)+"of"+str(nsteps))

        if(experiment):
            
            meanden = np.mean(rho)
            rhores = rho >= meanden
            count = np.sum(rhores)
            itercount.append(t)
            domainsize.append(count)

    if(experiment):
        fig, ax = plt.subplots()
        ax.plot(itercount, domainsize)
        ax.set_xlabel("dimensionless time")
        ax.set_ylabel("domain growth")
        ax.set_title("domain growth v/s dimensionless time")
        fig.savefig("./spindecom/domain growth versus dimensionless time")
    rho = np.sum(f, 2)
    u = np.zeros((nx,ny,2))
    u[:,:,0] = np.sum(f*exs,2) / rho + force[:,:,0]/(2*rho)
    u[:,:,1] = np.sum(f*eys,2) / rho + force[:,:,1]/(2*rho)
    return (rho, u)
    