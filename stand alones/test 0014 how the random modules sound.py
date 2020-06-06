print("random module demonstration, by 56independent")

from winsound import Beep
from random import randint
from secrets import randbelow
from time import sleep

def randommod():
    tone = randint(0,1000)
    if tone<300:
        pass
    else:
        Beep(tone,50)
def secretsmod():
    tone = randbelow(1000)
    if tone<300:
        pass
    else:
        Beep(tone,50)
        
exits = False
loop = True
while not exits == True:
    mode = input("so you want to hear the (s)ecrets module first or the"
                 "(r)andom module first?(exit is e)")
    if mode == "s":
        for i in range(100):
            secretsmod()
        print("now lets play the random module")
        sleep(2)
        for i in range(100):
            randommod()
    if mode == "r":
        for i in range(100):
            randommod()
        print ("now lets play the secrets module")
        sleep(2)
        for i in range(100):
            secretsmod()
    if mode == "e":
        exits = False