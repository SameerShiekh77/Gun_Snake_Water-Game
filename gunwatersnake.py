import random
import os
import time


clear = lambda: os.system ('cls')
clear()
points = 0
total = 0
wining = 0
while(True):
    time123 = time.asctime(time.localtime(time.time()))
    print("\t\t\t", time123)
    attack = ["Gun", 'Snake', 'Water']
    comp = random.choice(attack)
    Playerscore = str(points)
    compscore = str(wining)
    total = (total)
    print("\t\t\t\t\tWe are playing Snake Gun Water\n\t\t\t\t\t\t\t\t\t\t\t Player score",Playerscore,"\n\t\t\t\t\t\t\t\t\t\t\t Computer score", compscore, "\n\t\t\t\t\t\t\t\t\t\t\t Total Match" , total)
    print("\t\t\t\t\tDeveloped By Muhammad Sameer\n")
    player = input("Choose your attack\ns for Snake\nw for Water\ng for Gun\n")
    
    if comp == 'Gun' and player == 'w':
        print("You Win!!")
        points = points + 1
    elif comp == 'Gun' and player == 's':
        print("You Loss!!")
        wining = wining + 1
    elif comp == 'Water' and player == 's':
        print("You Win!!")
        points = points + 1
    elif comp == 'Water' and player == 'g':
        print("You Loss!!")
        wining = wining + 1
    elif comp == 'Snake' and player == 'g':
        print("You Win!!")
        points = points + 1
    elif comp == 'Snake' and player == 'w':
        print("You Loss!!")
        wining = wining + 1
    elif comp == 'Water' or player == 'w' and comp =='Snake' or player == 's' and comp == 'Gun' or player == 'g':
        print("Match tie")
    else:
        print('\t\tPlease type valid attack\n')
    print('\tPlease type y for yes & n for no')
    again = input('\tWanna play again ???\n\t')
    if again == 'y' or again == 'yes':
        clear()
        total = total + 1
        continue
    elif again=='n' or again=='no':
        print('\tbye..have a nice day <3')
        break
    else:
        break