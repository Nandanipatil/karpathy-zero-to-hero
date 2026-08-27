import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 3*x**2 - 4*x + 5


# Test the function
print(f(3.0))


# Create x values
xs = np.arange(-5, 5, 0.25)

# Calculate y values
ys = f(xs)


# Plot the function
plt.plot(xs, ys)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) = 3x² - 4x + 5")
plt.grid()
plt.show()

