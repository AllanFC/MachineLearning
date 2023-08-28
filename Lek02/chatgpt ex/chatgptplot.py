import numpy as np
import matplotlib.pyplot as plt

# Generate data
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Create a scatter plot
plt.scatter(X, y, label='Data Points')

# Plot the linear relationship line
plt.plot(X, 4 + 3 * X, color='red', label='True Line')

# Add labels and title
plt.xlabel('X')
plt.ylabel('y')
plt.title('Scatter Plot of Data with True Line')
plt.legend()

# Display the plot
plt.show()