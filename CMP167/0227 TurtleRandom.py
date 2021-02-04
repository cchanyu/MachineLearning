import turtle
import random

win = turtle.Screen()
tata= turtle.Turtle()

tata.speed(10)
tata.color("red")
tata.pensize(3)
tata.shape("turtle")
x = int(50)

for i in range (x):
    tata.forward(random.randrange(1,100+1))
    tata.right(random.randrange(1,100+1))

#randrange(START, END)<<generates random integer between start + end
