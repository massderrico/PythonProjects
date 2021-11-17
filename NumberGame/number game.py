

import random
guesses = []
guess_number = 4
answer = random.randint(1,20)

def right_answer ():
    global guess
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == answer:
        print ("you are right ")
    elif guess < answer:
        print ("guess a higher number")
    else:
        print( "guess a lower number")

while 1<= guess_number <= 4:

    right_answer()
    guesses.append(guess)
    guess_number -= 1
    if guess == answer:
        break
    print ("you have " + str(guess_number) + " guesses left")

print (guesses)

