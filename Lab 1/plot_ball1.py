# H.P.L. - A Primer on Scientific Programming with Python
# Ex 5.9

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

v0 = 10
g = 9.81
# create 1000 points between 0 and 2v0/g
t_points = np.linspace(0, (2 * v0 / g), 1000)

# create a function to compute y(t) as the problem
def y(t):
  return v0 * t - 0.5 * g * t ** 2

# generate the y(t) values from the t_points
y_points = y(t_points)

# plot the y_points vs t_points curve
plt.plot(t_points, y_points)
plt.xlabel("time (s)")
plt.ylabel("height (m)")
plt.xlim([t_points[0], t_points[-1]])
plt.ylim([y_points.min(), y_points.max()])
plt.title("Simple Trajectory for a Ball Thrown Upwards with V0=10m/s")
plt.show()