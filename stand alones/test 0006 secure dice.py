from secrets import *
print ("secure random generator, a 506independent program")
#makes the variables
canc = False
high = 2
num = 0
while canc == False:
    choice = input("what do you want to generate? a single random number"
                   " in the range you choose (s), as many"
                   "separate secure random numbers as you want, in a"
                   " range you choose (3), make a hex with as many bytes "
                   "as you choose(h)"
                   "or generate a token with as many bytes as you"
                   " choose (t). you can also see about, (a). maybe you"
                   " want to enter the DICE LOOP (dl)")
    #ensures your choice is processed
    if choice == "s":
        high = int(input("what will be the highest number?"))
        num = randbelow (high)
        print (num)
    if choice == "t":
        high = int(input("how many bytes is your token?"))
        num = token_bytes (high)
        print (num)
    if choice == "h":
        high = int(input("how many bytes is your hex?"))
        num = token_hex(high)
        print (num)
    if choice == "3":
        rang = int(input("how many random numbers do YOU want to"
                         " GENERATE?"))
        choice = input("do you want to choose the cap for all the "
                       "numbers at once(a), or meet them induvidually(i)?")
        if choice == "a":
            high = int(input(" what is the cap?"))
        for i in range(rang):
            if choice == "i":
                high = int(input("what is the cap for this number?"))
                num = randbelow (high)
                print (num)
            else:
                num = randbelow (high)
                print (num)
                #changing the choice is essantial, otherwise it will play the about page
                choice = "d"
    if choice == "a":
        print ("this dice was designed as a secure dice, for when you need secure random generation.")
        print ("imagine this. you're playing a board game, and someone decided to bring a cheat dice. you then lose.")
    if choice == "dl":
        #makes the variables befor they are used
        mode = "fill"
        enter = "fill"
        mode = int(input(" what mode do you want? 10, 8, 6, 5, 2 or choose(1)?"))
        enter = input("you have decided to enter the DICE LOOP. to enter, just enter the word in, and you are in. otherwise,"
                      "you will be kicked out")
        if enter == "in":
            print ("you poor soul, you ahve entered the loop! e to exit if you got here by accident!")
            if mode == 10:
                while not enter == "e":
                    num = randbelow (10)
                    print (num)
                    enter = input("press enter when you are ready to re-roll")
            if mode == 8:
                while not enter == "e":
                    num = randbelow (8)
                    print (num)
                    enter = input("press enter when you are ready to re-roll")
            if mode == 6:
                while not enter == "e":
                    num = randbelow (6)
                    print (num)
                    enter = input("press enter when you are ready to re-roll")
            if mode == 5:
                while not enter == "e":
                    num = randbelow (5)
                    print (num)
                    enter = input("press enter when you are ready to re-roll")
            if mode == 2:
                while not enter == "e":
                    num = randbelow (2)
                    print (num)
                    enter = input("press enter when you are ready to re-roll")
            if mode == 1:
                high = int(input("what is the cap number?"))
                while not enter == "e":
                    num = randbelow (high)
                    print (num)
                    enter = input("press enter when you are ready to re-roll")           
        else:
            pass
    #turns the canc into python readable Trues and Falses.
    canc = input("again(y/n)")
    if canc == "y":
        canc = False
#hundredth line?!
    if canc == "Y":
        can = False
    if canc == "n":
        canc = True
    if canc == "N":
        canc = True
#when you use the python runthing, then this wont close the runthing instantly. stops when you hit enter.
input("thanks for trying my second dice!")