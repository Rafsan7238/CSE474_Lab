# H.P.L. - A Primer on Scientific Programming with Python
# Ex 5.13

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import sys

g = 9.81

# take in values of y0, theta and v0 from the command line
if len(sys.argv) == 4:
    y0, theta, v0 = np.array(sys.argv[1:], dtype=float)
    theta = theta * np.pi / 180

else:
    print("Please provide the required parameters!!")
    sys.exit(1)

# create a function f(x) as given in problem
def f(x):
    return (x * np.tan(theta)) -  1 / (2 * v0 ** 2) * ((g * x ** 2) / (np.cos(theta) ** 2)) + y0

# define initial horizontal and vertical velocities
v_hor = v0 * np.cos(theta)
v_ver = v0 * np.sin(theta)

# calculate time for the ball to land using (u + gt)^2 = u^2 + 2gs
t = (v_ver + np.sqrt(v_ver ** 2 + 2 * g * y0)) / g

# final x value = v_hor * t
x_points = np.linspace(0, t * v_hor, 1000)
y_points = f(x_points)

# plot the height vs horizontal distance curve
plt.plot(x_points, y_points)
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")
plt.xlim([0, x_points[-1]])
plt.ylim([0, y_points.max()])
plt.title("Complex Trajectory for a Ball Thrown Upwards With Respect to Horizontal Distance")
plt.show()