# H.P.L. - A Primer on Scientific Programming with Python
# Ex 5.30

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# initialise A, B, C and T
A = 2.414 * 10 ** -5
B = 247.8
C = 140
T = np.linspace(273.15, 373.15, 1000)

# create u(T) as given in the problem
def u(T):
    return A * 10 ** (B / (T - C))

# generate y_points from function u(T)
y_points = u(T)

# plot the viscosity vs temperature curve
plt.plot(T, y_points)
plt.xlabel("temperature (C)")
plt.ylabel("viscosity (Pa s)")
plt.title("Water Viscosity With Respect to Temperature")
plt.show()