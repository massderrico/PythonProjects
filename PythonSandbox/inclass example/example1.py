"""Massimo D'Errico"""

Num = int(input("imput number "))
factor = int(2)

try:
    while factor <= Num:
        if Num%factor == 0:
            print(factor)
            Num = Num/factor
        else:
            factor += 1
except ValueError:
    print("error")

