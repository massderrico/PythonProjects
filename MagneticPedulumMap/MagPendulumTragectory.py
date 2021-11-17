"""
Motion of a magnetic pendulum

Author (python): A. Stewart
Author (java): J.-F. Briere
Current version written: March 2020
Description: Calculates the motion of a magnetic pendulum moving in a plane with 3 fixed magnets.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

#Declare constants
DT = 1e-3 #Time step (in seconds)
TMAX = 60 #Total time of simulation (in seconds)
K = 0.50 #Restoring constant (in N/m/kg)
B = 0.15 #Drag constant (in Ns/m/kg)
J = 1.0 #Magnet constant (in N m^2/kg)
Z = 0.25 #Vertical position of pendulum (in m)

#x and y positions of the fixed magnets
MX = np.array([1,-0.5,-0.5]) 
MY = np.array([0,math.sqrt(3)/2,-math.sqrt(3)/2])

#Total number of time steps
N = int(TMAX/DT)

#Declare main arrays
t = np.empty(N) #Time array
x = np.empty(N) #x position array
y = np.empty(N) #y position array
vx = np.empty(N) #x velocity array
vy = np.empty(N) #y velocity array

#Method to find the x acceleration
def aX(x,y,vx):
  #Initialize
  grav = 0
  drag = 0
  mag = 0

  #Contribution from gravity
  grav = -K*x  

  #Contribution from drag
  drag = -B*vx

  #Contribution from the 3 fixed magnets
  for i in range(3):
      mag += (MX[i]-x)/((MX[i]-x)**2+ (MY[i]-y)**2 + Z**2)**(3/2)

  return grav + drag +J*mag

#Method to find the y acceleration
def aY(x,y,vy):
  #Initialize
  grav = 0
  drag = 0
  mag = 0

  #Contribution from gravity
  grav = -K*y

  #Contribution from drag
  drag = -B*vy

  #Contribution from the 3 fixed magnets
  for i in range(3):
      mag += (MY[i]-y)/((MX[i]-x)**2+ (MY[i]-y)**2 + Z**2)**(3/2)
  
  return grav + drag +J*mag
    
#Initial conditions (start with no velocity)
t[0] = 0 #Initial time (in sec)
x[0] = 2.0 #Initial x position (in m)
y[0] = 1.0 #Initial y position (in m)
vx[0] = 0 #Initial x velocity (in m/s)
vy[0] = 0 #Initial y velocity (in m/s)

#Do one step of Euler's method to get the next values
t[1] = t[0] + DT

x[1] = x[0] + vx[0] * DT
y[1] = y[0] + vy[0] * DT

vx[1] = vx[0] + aX(x[0],y[0],vx[0]) * DT
vy[1] = vy[0] + aY(x[0],y[0],vy[0]) * DT

#Loop to calculate the quantities at all other time steps
for i in range(1,N-1):
  t[i+1] = t[i] + DT
    
  #Verlet's method to find positions
  
  x[i+1]=  2*x[i] + aX(x[i], y[i],vx[i])*DT**2-x[i-1]
  y[i+1]=  2*y[i] + aY(x[i], y[i],vy[i])*DT**2-y[i-1]
  #Euler's method to find velocities
  vx[i+1] = vx[i] + aX(x[i],y[i],vx[i]) * DT
  vy[i+1] = vy[i] + aY(x[i],y[i],vy[i]) * DT

#Plot the trajectory
plt.plot(x,y,zorder=1,color='magenta')
plt.scatter(MX,MY,color='black',zorder=2,label='Fixed magnets')
plt.scatter(x[0],y[0],color='magenta',zorder=3)
title = 'Trajectory for initial position ('+str(x[0])+','+str(y[0])+')'
plt.title(title)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.show()
