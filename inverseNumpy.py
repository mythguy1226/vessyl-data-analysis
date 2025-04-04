import numpy as np
import matplotlib.pyplot as plt

# Generate data with a linear relationship
x = np.linspace(1, 10, 100)
y = -2 * x + 20  # Inverse linear relationship

# Add some random noise to the data to simulate real-world data
noise = np.random.normal(0, 2, 100)
y_noisy = y + noise

# Create the scatter plot
plt.scatter(x, y_noisy, label='Data Points')

# Plot the original inverse linear function without noise
plt.plot(x, y, color='red', label='Inverse Linear Function')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Inverse Linear Scatter Plot')

# Add legend
plt.legend()

# Show the plot
plt.show()