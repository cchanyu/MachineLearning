import math
import random

num = int(input("Enter the number of dice to roll:"))
x = 0
y = 0

for i in range(num):
    x = random.randrange(1,6+1)
    y = y + x

print("The sum of",num,"dice roll is",str(y)+".")
