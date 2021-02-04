import turtle
win = turtle.Screen()
tera = turtle.Turtle()

tera.speed(1)
win.bgcolor("white")
tera.pensize(3)
tera.shape("turtle")

for i in range(4):
    tera.forward(100)
    tera.color("red")
    tera.forward(100)
    tera.color("black")
    tera.left(90)

win.exitonclick()
