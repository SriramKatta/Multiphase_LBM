import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize lists for storing data
itercountcont = []
domainsize = []

# Function to calculate contact angle at each iteration
def cangle_plot(iter):
    fname = "./nparrrefspin/iter_" + str(iter) + ".npy"
    rho = np.load(fname)
    rho_transposed_flipped = np.transpose(rho)
    meanden = np.mean(rho)
    rhores = rho >= meanden
    count = np.sum(rhores)
    itercountcont.append(iter)
    domainsize.append(count)
    
    return rho_transposed_flipped  # Return the rho array for plotting

# List to store all the `rho` arrays for animation
rho_frames = []

# Loop over the iterations and compute contact angles and load `rho` arrays
for i in range(0, 4000 + 1, 50):
    rho_frames.append(cangle_plot(i))

# Create a figure and axis for plotting
fig, ax = plt.subplots()

# Display the first frame of the rho array
img = ax.imshow(rho_frames[0], origin='lower')
fig.colorbar(img, ax=ax, label = r'$\rho_\alpha [\Delta m]$')
ax.set_title(f"Iteration: {itercountcont[0]} | Domain Size: {domainsize[0]:.2f}")
ax.axis('off')

# Function to update the plot for each frame
def update_frame(frame_index):
    img.set_array(rho_frames[frame_index])
    # Update the title with the current iteration and contact angle
    ax.set_title(f"Iteration: {itercountcont[frame_index]} | Domain Size: {domainsize[frame_index]:.2f}")
    return [img]

# Create the animation
ani = animation.FuncAnimation(fig, update_frame, frames=len(rho_frames), blit=True)

# Save the animation as a GIF
ani.save('./rho_evolution_animation_with_domain_size.gif', writer='imagemagick', fps=10)

#plt.show()
