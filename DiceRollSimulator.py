#Dice Roll Simulator
import random
num_dice = int(input("Select the number of dice: "))
outcome = []
for i in range(1, 6*num_dice + 1):
    #print(i)
    outcome.append(i)