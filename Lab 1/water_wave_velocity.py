# H.P.L. - A Primer on Scientific Programming with Python
# Ex 5.31

# import necessary libraries
from cProfile import label
from cgitb import small
import numpy as np
import matplotlib.pyplot as plt

# initialise g, s, p and h
g = 9.81
s = 7.9 * 10 ** -2
p = 1000
h = 50

# create c(l) as given in the problem
def c(l):
    return np.sqrt((g * l) / (2 * np.pi) * (1 + (s * 4 * np.pi ** 2) / (p * g * l ** 2)) * np.tanh(2 * np.pi * h / l))

# generate small_lambda_points and large_lambda_points
small_lambda_points = np.linspace(0.001, 0.1, 10000)
large_lambda_points = np.linspace(1, 2000, 10000)

# plot the c(l) vs lambda curve
plt.subplot(1,2,1)
plt.plot(small_lambda_points, c(small_lambda_points))
plt.xlabel("lambda (m)")
plt.ylabel("wave speed (m/s)")
plt.title("Small Lambda Values")

plt.subplot(1,2,2)
plt.plot(large_lambda_points, c(large_lambda_points))
plt.xlabel("lambda (m)")
plt.ylabel("wave speed (m/s)")
plt.title("Large Lambda Values")

plt.suptitle("Wave Speed of Water Surface Waves With Respect to Length of Waves")
plt.show()