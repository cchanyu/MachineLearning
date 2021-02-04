#loads turtle from the library
import turtle

#creates GUI(Graphical User Interface)
win = turtle.Screen()

#make new turtle object
turtie = turtle.Turtle()

#turtie's shape
turtie.speed(1)
turtie.color("purple")
win.bgcolor("black")
turtie.pensize(3)
turtie.shape("turtle")

#turtie's movement, repeat 6 times.
turtie.color("blue")
for i in ["red","blue","yellow","green"]:
    turtie.color(i)
    turtie.forward(100)
    turtie.left(90)

win.exitonclick()
