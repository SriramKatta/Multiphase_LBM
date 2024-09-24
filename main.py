import numpy as np
from spinodal_decomp import spindecomp
from contact_angle import contactangle
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

nx = 32
ny = 32
tau = 1
g = -5.0
rad_bubble = 10

def numvalidation():
    nsteps = 25000
    rho = np.full((nx,ny), 0.5)
    X ,Y  = np.meshgrid(range(nx), range(ny), indexing='ij')
    sphere = (X - nx/2)**2 + (Y - ny/2)**2 <= 10**2
    rho[sphere] = 1.5
    
    rho = gaussian_filter(rho,sigma = 2)

    fig, ax = plt.subplots(figsize=(15,10))
    im = ax.imshow(rho)
    fig.colorbar(im, ax=ax, label = r'$\rho_\alpha [\Delta m]$')
    ax.set_xlabel(r'x $[\Delta x]$')
    ax.set_ylabel(r'y $[\Delta x]$')
    ax.set_title('Initial density profile')
    ax.invert_yaxis()
    plt.show()

    (rho, u) = spindecomp(nx, ny, nsteps, tau, rho, g, False, 10, False)
    
    fig, ax = plt.subplots(figsize=(15,10))
    im = ax.imshow(rho)
    fig.colorbar(im, ax=ax, label = r'$\rho_\alpha [\Delta m]$')
    ax.set_xlabel(r'x $[\Delta x]$')
    ax.set_ylabel(r'y $[\Delta x]$')
    ax.set_title('t='+str(nsteps))
    ax.invert_yaxis()
    plt.show()
    plt.close()

def mainspin():
    nsteps = 4000
    np.random.seed(3)
    rho = np.random.normal(1.0, 1e-1, nx*ny).reshape(nx,ny)
    (rho, u) = spindecomp(nx, ny, nsteps, tau, rho, g, True, 100, True)

def contangle():
    nsteps = 5000
    X, Y = np.meshgrid(range(nx),range(ny),indexing='ij')
    rad_bubble = 30
    bubble = (X-nx/2)**2 + (Y-1)**2 <= rad_bubble**2
    #air domain
    rho = np.full((nx,ny),0.2)
    #wall density
    rho_wall = 0.7
    #bubble density
    rho[bubble] = 1.9

    rho = gaussian_filter(rho,sigma = 2)

    
    (rho, u) = contactangle(nx, ny, nsteps, tau, rho , rho_wall, g, True,100)





if __name__ == "__main__":
    #numvalidation()
    mainspin()
    #contangle()