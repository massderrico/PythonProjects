import numpy as np
# Q2
def get_factors(num):
    size = 0
    for i in range(1, num + 1):
        if num % i == 0:
            size += 1
    arr = np.zeros(size)
    index = 0
    for i in range(1, num + 1):
        if num % i == 0:
            arr[index] = i
            index = index+1
    return arr

# Q3
def longest_string():
    num = int(input("how many strings?"))
    array1 =[]
    longest_str = 0
    longest_index = -1
    for i in range(num):
        cur = input("input a string: ")
        array1.append(cur)
        if len(cur) > longest_str:
            longest_str = len(cur)
            longest_index = i
    print (array1[longest_index])

