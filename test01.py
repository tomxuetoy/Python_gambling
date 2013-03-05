# can play once

import random

computer = random.randint(1,4)
user = int(raw_input('Please input a number (1-4) ====> :'))

if user == 1 :
    if computer == 2 :
        print "The Winner is computer!!"
    elif computer == 4 :
        print "The winner is user !!"
    else :
        print "Draw!!"

elif user == 2 :
    if computer == 3:
        print "The winner is computer!!"
    elif computer == 1:
        print "The winner is user !!"
    else:
        print "Draw!!"

elif user == 3 :
    if computer == 4:
        print "The winner is computer!!"
    elif computer == 2:
        print "The winner is user!!"
    else:
        print "Draw!!"

elif user == 4 :
    if computer == 1:
        print "The winner is computer!!"
    elif computer == 3:
        print "The winner is user!!"
    else :
        print "Draw!!"
else :
    print "Sorry! your input is Wrong!!"
