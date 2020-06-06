print ("the 56 independent number guessing game. try to guess the number"
       ", in a given range.")
from random import *
win = False
while not exit == True:
    win = False
    lives = int(input("how many goes do you wish to have?"))
    rang = int(input ("what is your range (0- your number)"))
    number = randint(0, rang)
    while not win == True:
        guess = int(input ("your guess"))
        if lives == 0:
            print("you ran out of lives, sorry!")
            input()
        else:
            if guess>number:
                print("lower!")
                lives = lives-1
            if guess<number:
                print ("higher!")
                lives= lives-1
            if guess==number:
                print("correct, well done!")
                print(f"you won with {lives} goes left.")
                win = True