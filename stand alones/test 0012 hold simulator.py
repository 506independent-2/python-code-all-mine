print ("hold simulator, 56 independent")
#allows me to get all the funtions i need; delay, random number. just
#everything.
from winsound import Beep
from time import sleep
from random import randint
exits = False
while not exits == True:
    queue = randint(500, 1000)
    phone_number = int(input ("enter a phone number"))
    num = randint(0,1)
    if num == 0:
        print ("wrong phone number,try again!")
        sleep(0.2)
    if num == 1:
        print (f"welcome to THE companies help phone number at"
               f" {phone_number}.we value your call")
        sleep(0.75)
        print (f"your place in the queue: {queue}")
        sleep(0.5)
        music = input ("would you like music?(y/n)")
        if music == "n":
            print ("too bad, we're playing music anyways!")
            sleep (0.75)
            music = "y"
        while music == "y":
            for i in range (randint(10,50)):
                note = randint(300,1000)
                duration = randint (10,600)
                Beep (note,duration)
            if queue>100:
                queue = queue - randint (10,100)
            elif queue>49:
                queue = queue - randint (10,30)
            elif queue<50:
                queue = queue - randint (1,10)
            elif queue<10:
                queue = queue - randint (1,5)
            if queue<0:
                queue = 0
            sleep(0.5)
            print (f"your place in the queue: {queue}")
            sleep (0.5)
            if queue == 0 or queue<0:
                operator = randint(1,5)
                if operator == 1:
                    operator = "steve"
                if operator == 2:
                    operator = "darren"
#50th line, whoohoo!
                if operator == 3:
                    operator = "cheryl"
                if operator == 4:
                    operator = "wayne"
                if operator == 5:
                    operator = "macy"
                input (f"{operator}: how can i help?")
                sleep (0.75)
                print (f"{operator}: ok, forwading you to that part of the team")
                sleep (0.75)
                for i in range (randint(5,20)):
                    note = randint(300,1000)
                    duration = randint (10,600)
                    Beep (note,duration)
                operator = randint(1,5)
                if operator == 1:
                    operator = "steve"
                if operator == 2:
                    operator = "darren"
                if operator == 3:
                    operator = "cheryl"
                if operator == 4:
                    operator = "wayne"
                if operator == 5:
                    operator = "macy"
                print(f"{operator}: ok, do this and that")
                sleep (0.75)
                solve = input (f"{operator}: did that solve your problem (y/n)?")
                sleep (0.75)
                if solve == "y":
                    print (f"{operator}: alrighty")
                    music = "n"
                    sleep(0.75)
                    exits = input (f"{operator}: do you wish to hang up? (y/n)")
                    if exits == "y":
                        exits = True
                    if exits == "n":
                        exits = False