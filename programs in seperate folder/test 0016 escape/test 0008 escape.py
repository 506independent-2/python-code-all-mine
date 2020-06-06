from stuff import breaker
class label(Exception): pass  # declare a label
choice2 = "frappa"
decison = "now it's defined!!"
#start
print ("escape the december by nicholas from 506independent. the numbers in bracket show which number corresponds to which"
       "choices you can choose. - eat (5) or  sleep (1). (example)")
breaker()
print ("chapter one - the hospital")
breaker()
print ("you wake up on one of those hospital beds,around you are dead people. you look at your super accurate smartwatch."
       " 30th novemember 2020. you went to sleep on april, after being diagnosed covid-19, serverely.")
choice = int(input(" what do you want to do? check the news (1), or walk and explore a seemingly abandoned hospital (2)?"))
breaker()
if choice == 1:
    print (" you try to take your phone out of your pocket. you realise that you are wearing one of those stupid "
           "hospital vests you dnt have your phone. you need to get out of bed")
    breaker()
    choice = 2
if choice == 2:
    print ("you get out of bed and explore the ward. it smells terrible. you try to avoid touching any surface, you have seen"
           " the horros of covid-19. you're probably immune, but best to be safe")
    choice = int(input(" you leave the ward, and reach the hallway. there are two ways to go, one goes up the ward numbers(6), "
                       "the one that goes down has a map, and might lead you to the exit(4)."))
    breaker()
if choice == 6:
    print ("this section of hallway is very long. when you reach the end, you are lost. the hallway  splits off into  2. in "
           "front of you is a door, that leads outside, into the car park. you can also see a sign saying reception")
    choice2 = int(input("do you go out into the car park (1) or into the reception(2)?"))
    breaker()
if choice == 4:
    print("you walk down,and pass a line of hallways. you continue, and you reach the map  the hospital is arranged in a wheel, "
          "and you are in the middle of it"
          " there are six main hallways, all radiating out from where you are. around each hallway is a ring of hallways"
          ". there are two rings in total, and one of the halllways is reserved for staff access. the hospital has three "
          "floors.")
    print ("you decide to go to the car park, to see if the world is as post-apocolyptic as you think it is")
    choice2 = 1
    breaker()
if choice2 == 2:
    print ("its a long walk into reception, and you see a map, you walk over to it.the hospital is arranged in a wheel, "
          "and you are in the middle of it"
          " there are six main hallways, all radiating out from where you are. around each hallway is a ring of hallways"
          ". there are two rings in total, and one of the halllways is reserved for staff access. the hospital has three "
          "floors.")
    print ("you decide to go to the car park, to see if the world is as post-apocolyptic as you think it is")
    breaker()
    choice2 = 1
if choice2 == 1:
    #chapter 2, where i start to get a bit more organised in my code, making it easier to read ;-)
    #yay 50th line!
    breaker()
    print ("chapter 2 - the world")
    breaker()
    print (" the car park seems normal at first. cars have been parked, the ambualnces are ready to go, and the helicopter"
           " on the roof is ready to go")
    print ("but you look again, and see that the clouds are grey, the cars are covered with bird poop, the helicopter looks"
           " unmaintained.  this place looks like its been forgotten by humanity. 2 seasons of wear and tear havent done the"
           "hospital any good. you can see all the coronavirus warnings, so the world must have ended on may."
           "you decide to walk to the main road, even quieter then in the quarantine.")
    decison = int(input("you have a decison to make. walk to the town to get info (1) or you can hide away in hospital until"
                       "someone comes (2)"))
    breaker()
if decison == 1
    if condition: raise label()  # goto label
except label:  # where to goto
    if decison == 1:
        print (" its a long walk, but eventually you reach town.")
        decison = int(input("you have another choice to make, knock on all the doors, to see if anyones alive here (5), or"
                            " go home, to research into stuff (6)"))
        breaker()
        if  decison == 5:
            print (" you go to every door, on every street. no-one answers. halfway through you decide to give up, you want to go"
               " home after  such a long walk")
            breaker()
            decison == 6
        if decison == 6:
            print ("you walk home. your door dosent unlock. you remember thet you had locked it before you went to hospital"
                   "you go through an open window in the kitchen towards the back. you"
                   " smell home after a long year out, and feel that sense of satisfaction from being home. you go to your front"
                   " door,  and see the pool of letters on your floor. the latest one was from august. you sort through them."
                   "you have bills from your wifi company, for not paying. they say that they had stopped your wifi because of"
                   " not reciving money.")
            decison = int (input("you have a choice, pay them (1), or find someones phone and use their data (2)"))
            breaker()
if decison == 2:
    print (" you go back into hospital, to see what you can do")
    decison = int(input("there are two plausabke options. go to the staff rooms to try to contact someone(3), or go to the"
                        " hospital kitchens to look for food (4)"))
    breaker()
    if decison == 3:
        print ("you go to the staff wing, where a electronically locked door allowed you through (it was fail-safe meaning"
               " that it would allow people through if electricty went out due to a fire)")
        print (" you see all the different rooms,like kitchen, staff room, and cctv room. you think staff room is the best"
               "place"
               ". you go in and look for the phone. you call the emergency number. theres no dial tone. you see its not even"
               "on! you need to find the circuit breaker.")
        print (" you go into a small room with high voltage written all over it. you find the electric meter and its over due"
               ". theres no elctricty, as indicated by no lighting works. you go to the breaker all of it had been switched off"
               " theres no need to stay here, as you wont be able to use anything. you go out to the car park once again")
    if decison == 4:
        print (" you go to the staff area, and look for the kitchen. you open its doors and a terrible smell escapes "
               "the rotting of hundreds of food items has made a  terrible smell. its enough to make the dead put their"
               " hands over their noses. you go inside, and holding your breath check all the cuboards. you find some tinned"
               " food and collect it in a plastic bag you found and continue looking for food. ")
        