import numpy as np

def intgame ():
    integer = int(input())
    intarray = np.array([integer])
    zero = np.array([])
    pos = np.array([])
    neg = np.array([])
    if integer < 0:
        np.append(neg, integer)
    elif integer > 0:
        np.append(intarray, pos)
    else:
        np.append(zero, integer)
    print(pos)




a = np.array([3])
b = np.append(a, [5])
print(b)
