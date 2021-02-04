import turtle
import random

win = turtle.Screen()
tata = turtle.Turtle()

tata.color("red")
tata.pensize(3)
tata.shape("turtle")
x = int(input("How many lines:"))
def square():
    for i in range (4):
        tata.forward(100)
        tata.right(90)
    return
def walk():
    tata.right(random.randrange(1,360+1))
    tata.forward(random.randrange(1,100+1))
    return

for i in range (x):
    square()
    walk()
