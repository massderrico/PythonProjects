"""
Magnetic pendulum map

Author (python): A. Stewart
Author (java): J.-F. Briere
Current version written: March 2020
Description: Produces a map representing the motion of a magnetic pendulum for various initial positions
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import sys

# Declare constants
DT = 1e-2  # Time step (in seconds)
TMAX = 60  # Total time of simulation (in seconds)
K = 0.50  # Restoring constant (in N/m/kg)
B = 0.15  # Drag constant (in Ns/m/kg)
J = 1.0  # Magnet constant (in N m^2/kg)
Z = 0.25  # Vertical position of pendulum (in m)

# x and y positions of the fixed magnets
MX = np.array([1, -0.5, -0.5])
MY = np.array([0, math.sqrt(3) / 2, -math.sqrt(3) / 2])

# Number of pixels per tile (horizontal and vertical) and distance step for x and y
PIXELS = 40
DX = 0.8 / PIXELS  # (in m)
DY = 0.8 / PIXELS  # (in m)

# Total number of time steps
N = int(TMAX / DT)

# Declare main arrays
x = np.empty(N)  # x position array
y = np.empty(N)  # y position array
vx = np.empty(N)  # x velocity array
vy = np.empty(N)  # y velocity array


# Method to find the x acceleration
def aX(x, y, vx):
    # Initialize
    grav = 0
    drag = 0
    mag = 0

    # Contribution from gravity
    grav = -K * x

    # Contribution from drag
    drag = -B * vx

    # Contribution from the 3 fixed magnets
    for i in range(0, 3):
        r = math.sqrt(math.pow(x - MX[i], 2) + math.pow(y - MY[i], 2) + math.pow(Z, 2))
        mag += J * (MX[i] - x) / math.pow(r, 3)

    return grav + drag + mag


# Method to find the y acceleration
def aY(x, y, vy):
    # Initialize
    grav = 0
    drag = 0
    mag = 0

    # Contribution from gravity
    grav = -K * y

    # Contribution from drag
    drag = -B * vy

    # Contribution from the 3 fixed magnets
    for i in range(0, 3):
        r = math.sqrt(math.pow(x - MX[i], 2) + math.pow(y - MY[i], 2) + math.pow(Z, 2))
        mag += J * (MY[i] - y) / math.pow(r, 3)

    return grav + drag + mag


# Method to find the pendulum trajectory
def pendulumTrajectory(xInitial, yInitial):
    # Initial conditions (start with no velocity)
    x[0] = xInitial  # Initial x position (in m)
    y[0] = yInitial  # Initial y position (in m)
    vx[0] = 0  # Initial x velocity (in m/s)
    vy[0] = 0  # Initial y velocity (in m/s)

    # Do one step of Euler's method to get the next values
    # t[1] = t[0] + DT

    x[1] = x[0] + vx[0] * DT
    y[1] = y[0] + vy[0] * DT

    vx[1] = vx[0] + aX(x[0], y[0], vx[0]) * DT
    vy[1] = vy[0] + aY(x[0], y[0], vy[0]) * DT

    # Loop to calculate the quantities at all other time steps
    for i in range(1, N - 1):
        # Verlet's method to find positions
        x[i + 1] = 2 * x[i] + aX(x[i], y[i], vx[i]) * math.pow(DT, 2) - x[i - 1]
        y[i + 1] = 2 * y[i] + aY(x[i], y[i], vy[i]) * math.pow(DT, 2) - y[i - 1]

        # Euler's method to find velocities
        vx[i + 1] = vx[i] + aX(x[i], y[i], vx[i]) * DT
        vy[i + 1] = vy[i] + aY(x[i], y[i], vy[i]) * DT

    # Check which magnet the pendulum ended closes to
    magnet = 0
    if (0.95 <= x[N-1] <= 1.05) and  (-0.05 <= y[N-1]<= 0.05):
        # Close to the fixed magnet at (1,0)
        magnet = 1
    elif ( -0.55 <= x[N-1] <= -0.45) and  (((math.sqrt(3) / 2)-0.05)<= y[N-1] <= ((math.sqrt(3) / 2)+ 0.05)):
        # Cose to the fixed magnet at (-0.5,sqrt(3)/2)
        magnet = 2
    elif (-0.55<= x[N-1] <= -0.45 ) and  (((math.sqrt(3) / -2)-0.05)<= y[N-1] <= (( math.sqrt(3) / -2)+ 0.05)):
        # Close to the fixed magnet at (-0.5,-sqrt(3)/2)
        magnet = 3
    else:
        # Not close enough to any of the fixed magnets
        magnet = 4

    return magnet;


# Set coordinate of the bottom-left corner of the tile (This should be a position ranging from (-4.8,-4.8) to (4,4) in steps of 0.8)
tileBottomLeftX = 0.8
tileBottomLeftY = 1.6

# Array to store each pixel
magnets = np.empty((PIXELS, PIXELS))

# File to output data
f = open('tileData.txt', 'w')

for i in range(0, PIXELS):
    # Initial x position of pendulum
    xInitial = tileBottomLeftX + i * DX
    for j in range(0, PIXELS):
        # Initial y position of pendulum
        yInitial = tileBottomLeftY + j * DY

        # Compute trajectory and store which fixed magnet the pendulum ends at
        magnets[i, j] = pendulumTrajectory(xInitial, yInitial)

        # Write the initial x position, initial y position, and the magnet value to a file (tab separated)
        f.write(str(xInitial)+'\t' + str(yInitial)+ '\t' + str(magnets[i,j])+ '\n')

f.close()

# Produce an image of the current tile
plt.imshow(magnets.transpose(), cmap='brg', origin='lower', zorder=1)
plt.show()
