#################################################
########### SNAKE WATER AND GUN GAME ############
#################################################

import random

def gamewin(computer, you):
    if computer == you:
        return None
    elif computer == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif computer == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
    elif computer == "g":
        if you == "s":
            return False
        elif you == "w":
            return True
print("############## GAME MODE ON ##############")
print("Computer Turn : Snake(s) Water(w) or Gun(g)?\n")
randomNo = random.randint(1,3)
if randomNo == 1:
    computer = 's'
elif randomNo ==2:
    computer = 'w'
elif randomNo == 3:
    computer = 'g'

you = input("Your Turn : Choose (s) for Snake, (W) for Water or (g) for Gun? : ")
game = gamewin(computer, you)

print("\nComputer choosen : ", computer)
print("You choosen : ", you)
print("\n############## Game Result ##############\n")

if game == None:
    print("The game is a tie!\n")
elif game:
    print("You Win!\n")
else:
    print("You Lose!\n")