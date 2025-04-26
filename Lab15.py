import numpy as np
import matplotlib.pyplot as plt

# Define constants and range of theta
a = 1  # Scaling factor for the spiral
theta = np.linspace(0, 10 * np.pi, 500)  # Range of theta values

# Calculate r using Fermat's spiral formula
r = a * np.sqrt(theta)

# Convert polar coordinates (r, theta) to Cartesian coordinates (x, y)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot Fermat's spiral
plt.figure(figsize=(6, 6))
plt.plot(x, y, label="Fermat's Spiral")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Fermat's Spiral: $r = a \\sqrt{\\theta}$")
plt.legend()
plt.axis('equal')  # Ensure the aspect ratio is equal
plt.grid()
plt.show()

