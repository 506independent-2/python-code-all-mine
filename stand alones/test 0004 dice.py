#makes sure i can select a random number
from random import randint
def prin():
    print ("your number was")
    #outputs the number
    print (number)
print ("this program is a dice, where you can choose the maximum and minimum numbers. have to choose a restraunt item? givethem numbers and"
       " choose a random one")
print ("also, dont crash the program by making the higest number lower then the lowest.")#havent fixed that. just dont do it.
cancel = 0
mode = 1
number = 3
#executes a loop, that only exits when you have decided you have had enough.
while not cancel == "y":
    mode = int(input("choose your mode, dice (1-6)(6), 10 (0-10)(10), choose(1), or exit (90)."))
    # the if segements make sure your mode works, and then skips the rest. also since the exit function wouldnt work, i had to
    #put the print functions inside a def statement.
    if mode == 6:
        number = randint (1,6)
        prin()
    if mode == 10:
        number = randint (0,10)
        prin()
    if mode == 1:
        #asks you for your numbers
        lowest = int(input("whats the lowest number?"))
        highest = int(input("whats the highest number?"))
        number = randint(lowest, highest)
        prin()
    if mode == 90:
        cancel = "y"
#thank you for looking at my code!   
print ("thank you for taking the time to use the dice!")