print ("coin flip by 506independent")
from random import randint
exits = False
while not exits == True:
    coin = randint(1,2)
    if coin == 1:
        coin = "t"
    if coin == 2:
        coin = "h"
    print (coin)
    results = ()
    results.append(coin)
    mode = input ("(a)gain, or see the (l)ist?")