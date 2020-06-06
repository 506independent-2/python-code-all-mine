from random import *
empty = 2
fortune = 3
print ("56 independents mystical fortune teller")
while not empty == 1:
    empty = input("this can tell your fortunes. write a y/n question.")
    fortune = randint(1,8)
    if fortune == 1:
        print ("definately")
    if fortune == 2 or fortune == 6:
        print ("yes")
    if fortune == 3:
        print ("maybe")
    if fortune == 4 or fortune == 7:
        print ("no")
    if fortune == 5:
        print ("definately not")
    if fortune == 8:
        print ("i dont know")