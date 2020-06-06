print ("ghost communicator, 506independent")
from random import randint
from time import sleep
exit = False
while exit == False:
    mode: str = input("choose your mode.(y)es or (n)o, y(e)s or no (e)xtended, (s)peak to the ghosts or n(o)pe! to exit.")
    
    if mode == "y" or mode == "n":
        print ("you have entered the yes or no loop, x to exit")
        while not mode == "x":
            mode = input ("y/n")
            sleep(5)
            choice = randint(1,4)
            if choice == 1:
                print ("yes")
            if choice == 2:
                print ("no")
            if choice == 3:
                print ("no answer available")
            if choice == 4:
                print ("i dont know / maybe")
                
    if mode == "e":
        print ("you have entered the yes no loop - exteneded. to exit, Answer x!")
        while not mode == "x":
            mode = input("y/n")
            if not mode == "x":
                sleep(5)
                choice = randint(1,9)
                if choice == 2 or choice == 4:
                    print ("yes")
                if choice == 1 or choice == 3:
                    print ("no")
                if choice == 5:
                    print ("definitely not!")
                if choice == 6:
                    print ("definately")
                if choice == 7:
                    print ("i dunno")
                if choice == 8:
                    print ("maybe")
                if choice == 9:
                    print("answer does not exist")
                
    if mode == "s":
        print ("you have entered the speak loop. x to exit")
        while not mode == "x":
            mode = input ("write your message")
            if not mode == "x":
                print ("your message has been sent?")
            
    if mode == "o":
        exit = True

print ("thank you for using the ghost communicator!")