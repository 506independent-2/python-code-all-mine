print ("heart monitor, by 56 independent")
from time import sleep
from winsound import *
exits = False
while not exits == True:
    bpm = int(input("what is the bpm?"))
    dec = input("do you want the heart rate to (i)ncrease, (s)tay the same, or (d)ecrease")
    die = input ("do you want to DIE? (y/n)")
    #now its time to set the bpm!
    #the bpm needs to be converted to sleep() seconds
    heartbeat = bpm/60
    pitch = 650
    while not frat == True:
        reapeats += 1
        for i in range(60):
            Beep(pitch,20)
            sleep(heartbeat)
        if dec == "i":
            heartbeat += 0.1
        if dec == "d":
            heartbeat += -0.1
        if die == "y" and repeats == 60:
            beep(pitch,1000000000000000000000000000)