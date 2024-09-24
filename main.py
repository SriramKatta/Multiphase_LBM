import numpy as np
from spinodal_decomp import spindecomp
from contact_angle import contactangle
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from cangle_graph import cangleplotter
from scipy import stats

nx = 128
ny = 128
tau = 1
g = -5.0
rad_bubble = 10

def numvalidation():
    
    #def calculatePressure(rho, g):
    #    return 1/3*rho + 1/6*g*(1-np.exp(-rho))**2 
#
    #nsteps = 25000
    #bubble_rad_range = [10,15,20,25,30]
    #p_diff = []
    #rad_out = []
    #for i in bubble_rad_range:
    #    rho = np.full((nx,ny), 0.5)
    #    X, Y = np.meshgrid(range(nx), range(ny), indexing='ij')
    #    bubble = (X - nx/2)**2 + (Y - ny/2)**2 <= i**2
    #    rho[bubble] = 1.5
    #    rho = gaussian_filter(rho, sigma=2)
    #    (rho, _) = spindecomp(nx,ny, nsteps, tau, rho, g, False, 10, False)
    #    P = calculatePressure(rho[:, ny//2], g)
    #    p_diff.append(P[nx//2] - P[0])
    #    rad_out.append((nx/2) - np.interp(0.5*(np.max(rho)+np.min(rho)), rho[0:nx//2,ny//2], range(nx//2)))

    rad_out = np.load("rad.npy")[0]
    p_diff = np.load("pdiff.npy")[0]
    invrad = 1/rad_out
    res = stats.linregress(invrad, p_diff)
    print("surface tension = ", res.slope)
    print("accuracy = ", res.rvalue)

    #np.save("./rad.npy",np.array([rad_out]))
    #np.save("./pdiff.npy", np.array([p_diff]))

    plt.figure()
    plt.plot(invrad, p_diff, 'o-', label='surface tension = '+str(res.slope))
    plt.xlabel('1/radius')
    plt.ylabel('pressure diff.')
    plt.savefig('valid.png')
    plt.legend()
    plt.show()
    


def mainspin():
    nsteps = 4000
    rho = np.random.normal(1.0, 1e-1, nx*ny).reshape(nx,ny)
    (rho, u) = spindecomp(nx, ny, nsteps, tau, rho, g, True, 100, True)

def contangle():
    nsteps = 5000
    rho = np.full((nx,ny),0.2)
    rho_wall = 0.5
    X, Y = np.meshgrid(range(nx),range(ny),indexing='ij')
    rad_bubble = 30
    bubble = (X-nx/2)**2 + (Y-1)**2 <= rad_bubble**2
    rho[bubble] = 1.9
    rho = gaussian_filter(rho,sigma = 2)
    (rho, u) = contactangle(nx, ny, nsteps, tau, rho , rho_wall, g, True,100)
    cangleplotter(nsteps)



if __name__ == "__main__":
    numvalidation()
    #mainspin()
    #contangle()