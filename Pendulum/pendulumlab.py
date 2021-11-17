"""
Motion of a pendulum and variation in period as a function of amplitude.

Author (python): A. Stewart
Author (java): J.-F. Briere
Current version written: March 2020
Description: Calculates the motion of a pendulum as a function of time and extract the period from the data.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

# Declare constants
DT = 0.01  # Time step (in seconds)
TMAX = 20  # Total time of simulation (in seconds)
G = 9.8  # Acceleration due to gravity (in m/s/s)
L = 1.0  # Length of pendulum (in meters)
THETAMAX = math.pi / 3  # Angular amplitude (in rad)
OMEGAINITIAL = 0  # Initial angular velocity (in rad/s)

plotAngleVsTime = True;  # When set to "True" a plot of angle vs time will be generated

amp_values = np.empty(100) #holds
per_values = np.empty(100)

# Method to find the period from the angular position data (DO NOT EDIT THIS)
def findPeriod(time, angle):
    k = 0
    lastTime = 0
    for j in range(0, N - 1):
        # Check if the sign of the angular position changes (passing through zero)
        if angle[j] * angle[j + 1] < 0:
            # Record the time when the pendulum was closest to zero
            if abs(angle[j]) < abs(angle[j + 1]):
                lastTime = time[j]
            else:
                lastTime = time[j + 1]

            # Count how many times the pendulum passes through zero
            k = k + 1

    # Determines the period based on the count and the last time recorded
    period = 4 * lastTime / (2 * k - 1)

    # Return the period
    return period


# Total number of time steps
N = int(TMAX / DT)

# Declare main arrays
t = np.empty(N)  # Time array
theta = np.empty(N)  # Angular position array

for n in range(100):

    amplitude = (math.pi-0.0001)/100 * (n+1)
    # Initial conditions
    t[0] = 0  # Initial time (in sec)
    theta[0] = amplitude# Initial angular position (in rad)

    # One step of Euler's method
    t[1] = t[0] + DT
    theta[1] = theta[0] + OMEGAINITIAL * DT

    # Verlet's method to calculate angular positon at each time step
    for i in range(1, N - 1):
        t[i + 1] = t[i] + DT
        theta[i + 1] = 2*theta[i]- (G/L*math.sin(theta[i])*DT**2)- theta[i-1]

    per_values[n] = findPeriod(t, theta)
    amp_values[n] = amplitude


print(amp_values)
print(per_values)

# Make a plot of angle versus time if desired
if plotAngleVsTime:
    plt.plot(amp_values, per_values, label='angular position')
    plt.title('Angular position vs. time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Angular position (radians)')
    plt.show()
