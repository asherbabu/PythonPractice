#Dice Roll Simulator
import random
num_dice = int(input("Select the number of dice: "))
outcomes = []
for i in range(1, 6*num_dice + 1):
    #print(i)
    outcomes.append(i)
print(outcomes)
random.choice(outcomes)