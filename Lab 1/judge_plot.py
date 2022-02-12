# H.P.L. - A Primer on Scientific Programming with Python
# Ex 5.29

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# plot cos(18*pi*x) for 20 points
x = np.linspace(0, 2, 20)
y = np.cos(18 * np.pi * x)

plt.plot(x, y, label="20 points")

# plot the function for 1000 points
x = np.linspace(0, 2, 1000)
y = np.cos(18 * np.pi * x)

plt.plot(x, y, label="1000 points")

plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.title("y = cos(18*pi*x)")
plt.show()