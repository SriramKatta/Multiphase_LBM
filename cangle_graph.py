import numpy as np
import matplotlib.pyplot as plt

itercountcont = []
cangle = []

def cangle_plot(iter):
    fname = "./nparrref/iter_"+str(iter)+".npy"
    rho = np.load(fname)[:, 3:-1]
    nx, ny = rho.shape
    sliceh = rho[ nx//2 , : ][nx//2::-1]
    #print(sliceh)
    targenden = 0.5 * (np.max(sliceh) + np.min(sliceh))
    h = len(sliceh) - np.interp(targenden, sliceh, np.arange(len(sliceh)))
    sliceb = rho[:nx//2, 0]
    b_half = (nx//2) - np.interp(targenden, sliceb, np.arange(len(sliceb)))
    r = (4*(h**2) + (2*b_half)**2) / (8 * h)
    canng = np.rad2deg(np.pi - np.arcsin(b_half/r))
    #print("h : ", h, " b_half : ",b_half, " radius : ", r, " c angle : ", canng)
    #plt.imshow(rho, cmap='gray')
    #plt.show()
    itercountcont.append(iter)
    cangle.append(canng)

def cangleplotter(nsteps):
    for i in range(0,nsteps+1, 100):
        cangle_plot(i)
    fig, ax = plt.subplots()
    ax.plot(itercountcont, cangle)
    ax.set_xlabel("dimensionless time")
    ax.set_ylabel("contact angle(degress)")
    ax.set_title("contact anglev/s dimensionless time")
    fig.savefig("./contactangle/contact angle versus dimensionless time")