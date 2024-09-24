import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize lists for storing data
itercountcont = []
cangle = []

# Function to calculate contact angle at each iteration
def cangle_plot(iter):
    fname = "./nparrref/iter_" + str(iter) + ".npy"
    rho = np.load(fname)[:, 3:-1]
    nx, ny = rho.shape
    sliceh = rho[nx // 2, :][nx // 2::-1]
    
    targenden = 0.5 * (np.max(sliceh) + np.min(sliceh))
    h = len(sliceh) - np.interp(targenden, sliceh, np.arange(len(sliceh)))
    
    sliceb = rho[:nx // 2, 0]
    b_half = (nx // 2) - np.interp(targenden, sliceb, np.arange(len(sliceb)))
    
    r = (4 * (h**2) + (2 * b_half)**2) / (8 * h)
    canng = np.rad2deg(np.pi - np.arcsin(b_half / r))
    
    itercountcont.append(iter)
    cangle.append(canng)
    rho_transposed_flipped = np.transpose(rho)
    
    return rho_transposed_flipped  # Return the rho array for plotting

# List to store all the `rho` arrays for animation
rho_frames = []

# Loop over the iterations and compute contact angles and load `rho` arrays
for i in range(0, 5000 + 1, 100):
    rho_frames.append(cangle_plot(i))

# Create a figure and axis for plotting
fig, ax = plt.subplots()

# Display the first frame of the rho array
img = ax.imshow(rho_frames[0], origin='lower')
fig.colorbar(img, ax=ax, label = r'$\rho_\alpha [\Delta m]$')
ax.axis('off')
ax.set_title(f"Iteration: {itercountcont[0]} | Contact Angle: {cangle[0]:.2f}°")

# Function to update the plot for each frame
def update_frame(frame_index):
    img.set_array(rho_frames[frame_index])
    # Update the title with the current iteration and contact angle
    ax.set_title(f"Iteration: {itercountcont[frame_index]} | Contact Angle: {cangle[frame_index]:.2f}°")
    return [img]

# Create the animation
ani = animation.FuncAnimation(fig, update_frame, frames=len(rho_frames), blit=True)

# Save the animation as a GIF
ani.save('./rho_evolution_animation_with_angle.gif', writer='imagemagick', fps=10)

#plt.show()
