# H.P.L. - A Primer on Scientific Programming with Python
# Ex 5.28

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# initialise x points
x_points = np.linspace(-4, 4, 1000)

# create function f(x,t) as given in the problem
def f(x, t):
    return np.exp(-(x - 3 * t) ** 2) * np.sin(3 * np.pi * (x - t))

# generate y_points from f(x,t)
y_points = f(x_points, 0)

# plot f(x,t) vs x curve with t=0
plt.plot(x_points, y_points)
plt.xlabel("x")
plt.ylabel("f(x, t)")
plt.show()