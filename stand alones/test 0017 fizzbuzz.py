#fizzbuzz
print("fizz buzz program, by 56independent")
from time import sleep
loop = True
num = 0
#now we've made the variables, lets fine tune some settings.
term = int(input("at what number do you wish for the program to terminate"))
delay = input("do you want delay? (y/n)")
if delay == "y":
    delay = True
elif delay == "n":
    delay = False
if delay == True:
    length = float(input("how long to delay in seconds, i reccomend 0.3"))
#now we've done the settings, lets do THE LOOP
while not loop == False:
    #increase the focus number by 1
    num = num+1
    #lets check if its devisable by 7, or 3
    if num%3 == 0 and num%7 == 0:
        print ("fizzbuzz")
    elif num%3 == 0:
        print ("buzz")
    elif num%7 == 0:
        print ("fizz")
    #ok, it isnt. lets just print the number.
    else:
        print (num)
    #ok, now thats done lets terminate the program when we get to the termination number.
    if num == term or num > term:
        loop = False
    #give it a bit of delay if we want
    if delay == True:
        sleep (length)
    # we will go back to the beggining.
print("terminated")
#i want to see the result!
input("if you are using the pyhton runner, enter will close the program")
