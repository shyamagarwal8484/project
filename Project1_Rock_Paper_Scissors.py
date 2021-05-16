'''to build a rock, paper, scissors game
rock win over scissors
paper win over rock
scissors win over paper
'''

import random

def game(comp, you):
    
    if c=='r' or c=='s' or c=='p':
        print("You choosed: "+ c)
        print("Computer choosed: "+ comp)
        if comp == "s":
            if you == "s":
                return "Draw"
            elif you == "p":
                return "You Lose"
            else:
                return "You Win"
        elif comp == "p":
            if you == "p":
                return "Draw"
            elif you == "r":
                return "You Lose"
            else:
                return "You Win"
        else:
            if you == "r":
                return "Draw"
            elif you == "s":
                return "You Lose"
            else:
                return "You Win"
    else:
        return "Enter only r/s/p"

b = random.randint(1, 3)

if b == 1:
    comp = 's'
elif b == 2:
    comp = 'p'
else:
    comp = 'r'

c = input("Your Turn, Rock(r), Paper(p), Scissors(s): Enter r/p/s? ")

d = game(comp, c)
print(d)