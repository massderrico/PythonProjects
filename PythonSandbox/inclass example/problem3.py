"""Author: Massimo D'Errico"""
wins = 0
losses = 0
ties = 0

import random as rnd

user = input()
comp = rnd.randint(1,3)

while user != "q":
    print("enter (r)ock (p)aper (s)cissors or (q)uit")
    user = input()
    comp = rnd.randint(1,3)
    if (user == "s" and comp == 2) or (user == "p" and comp == 1) or (user == "r" and comp == 3):
        wins += 1
        print (f' wins: {wins}, losses : {losses}, ties: {ties}')
    elif (comp == 3 and user == "p") or (comp == 2 and user == "r") or (comp == 1 and user == "s"):
        losses += 1
        print (f' wins: {wins}, losses : {losses}, ties: {ties}')
    elif (comp == 2 and user == "p") or (comp == 1 and user == "r") or (comp == 3 and user == "s"):
        ties += 1
        print (f' wins: {wins}, losses : {losses}, ties: {ties}')
    elif user == "q":
        break

