import itertools
import math
import turtle
from matplotlib import pyplot as plt

a = [145,2,3]
b = [1,7,5]


turtle.speed(0)
turtle.setpos(a[0], b[0])
turtle.dot()
turtle.setpos(a[1], b[1])
turtle.dot()
turtle.setpos(a[2], b[2])
turtle.dot()
turtle.goto(a[1],b[1])

"""
plt.plot(a,b, 'ro')
plt.axis([0, 10, 0, 10])
plt.show()
"""