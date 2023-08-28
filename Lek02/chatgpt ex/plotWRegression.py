import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate data
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Create a scatter plot of data points
plt.scatter(X, y, label='Data Points')

# Fit linear regression model
regressor = LinearRegression()
regressor.fit(X, y)

# Predict y values using the model
y_pred = regressor.predict(X)

# Plot the linear regression line
plt.plot(X, y_pred, color='red', label='Linear Regression Line')

# Add labels and title
plt.xlabel('X')
plt.ylabel('y')
plt.title('Scatter Plot with Linear Regression Line')
plt.legend()

# Display the plot
plt.show()