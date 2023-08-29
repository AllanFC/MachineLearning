import matplotlib.pyplot as plt
import numpy as np


def cost(a, b, X, y):
    ### Evaluate half MSE (Mean square error)
    m = len(y)
    error = a + b * X - y
    J = np.sum(error ** 2) / (2 * m)
    return J


X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])

ainterval = np.arange(1, 10, 0.05)
binterval = np.arange(0.5, 5, 0.05)

for atheta in ainterval:
    for btheta in binterval:
        print("xy: %f:%f:%f" % (atheta, btheta, cost(atheta, btheta, X, y)))

plt.plot()
plt.show()
