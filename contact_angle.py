import matplotlib.pyplot as plt
import numpy as np
from D2Q9 import *
from pathlib import Path

def contactangle(nx, ny, nsteps, tau, rho, rho_wall, g, post, outfreq, experiment = True):
    f = np.zeros((nx, ny, ni))

    for i, w in zip(ei, ws):
        f[:, :, i] = rho * w
    
    feq = np.zeros_like(f)

        
    X, Y = np.meshgrid(range(nx),range(ny),indexing='ij')
    solid = Y < 2
    solid += Y > ny-2 

    if(post):
        Path("./contactangle").mkdir(parents=True, exist_ok=True)
        fig, ax = plt.subplots(figsize=(10,10))

    for t in range(nsteps + 1):
        #compute rho
        rho = np.sum(f,2)

        #compute ux & uy
        ux = np.sum(f* exs, 2)/ rho
        uy = np.sum(f* eys, 2)/ rho

        #computing shan chen forces
        psi = 1 - np.exp(-rho)
        psi[solid] = 1 - np.exp(-rho_wall) 
        force = np.zeros((nx, ny, 2))
        for w, ex, ey in zip(ws, exs, eys):
            force[:,:, 0] += w*np.roll(np.roll(psi[:,:], ex, axis=0), ey, axis=1)*(-ex)
            force[:,:, 1] += w*np.roll(np.roll(psi[:,:], ex, axis=0), ey, axis=1)*(-ey)
        force[:,:,0] = np.multiply(-g*psi[:,:],force[:,:, 0])
        force[:,:,1] = np.multiply(-g*psi[:,:],force[:,:, 1])

        #apply forces to velocity terms
        ueqx = ux + np.divide(tau*force[:,:,0],rho[:,:])
        ueqy = uy + np.divide(tau*force[:,:,1],rho[:,:])

        #compute eq local PDF
        for i, ex, ey, w in zip(ei, exs, eys, ws):
            feq[:,:,i] = rho * w * ( 1 + 3*(ex*ueqx+ey*ueqy) + 9*(ex*ueqx+ey*ueqy)**2/2-3*(ueqx**2+ueqy**2)/2)
        
        #collision 
        fnew =  f -(1.0/tau) * (f-feq)

        #simple bounce back
        boundaryf = f[solid,:]
        boundaryf = boundaryf[:,[0,3,4,1,2,7,8,5,6]]
        fnew[solid,:] = boundaryf

        f = fnew
        #streaming step
        for i, ex, ey in zip(ei, exs, eys):
            f[:,:,i] = np.roll(f[:,:,i], ex, axis=0)
            f[:,:,i] = np.roll(f[:,:,i], ey, axis=1)
        
        if((t % outfreq) == 0 or t == nsteps) and (post):
            plt.cla()
            ax = plt.gca()
            im = ax.imshow(rho.T)
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            ax.set_title('Iteration ='+str(t))
            ax.invert_yaxis()
            plt.savefig('./contactangle/Iteration_'+str(t))
            print('./contactangle/Iteration_'+str(t)+' of '+ str(nsteps))
        else:
            print(str(t)+"of"+str(nsteps))    
        
        if(experiment):
            np.save("./nparrref/iter_"+str(t)+".npy", rho)
            
    rho = np.sum(f, 2)
    u = np.zeros((nx,ny,2))
    u[:,:,0] = np.sum(f*exs,2) / rho + force[:,:,0]/(2*rho)
    u[:,:,1] = np.sum(f*eys,2) / rho + force[:,:,1]/(2*rho)
    rho[solid] = 0
    return (rho, u)
    
