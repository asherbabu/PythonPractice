#Guess the number
import random
a = int(input("Enter a number between 1-10: "))
if a>10:
    print("invalid input")
num = [1, 2, 3, 4, 5, 6, 7, 8, 10]
rand = random.choice(num)
print("your choice: ", a)
print("number: ", rand)
if rand == a:
    print("congratulations, you won")
else:
    print("better luck next time")