import turtle
win = turtle.Screen()
stair = turtle.Turtle()

stair.speed(5)
win.bgcolor("white")
stair.pensize(3)
stair.shape("arrow")

stair.penup()
stair.left(135)
stair.forward(500)
stair.right(135)
stair.pendown()

for i in range(10):
    print(i)
    stair.write(i,align="right",font=(30))
    stair.forward(50)
    stair.right(90)
    stair.forward(50)
    stair.left(90)

print("This is finish.")
stair.write("This is finish.",font=(30))

#Optional:
#from turtle import *
#win = Screen()
#taz = Turtle()
