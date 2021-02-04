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
for i in [0,1,2,3,4,5,6,7]:
    turtie.forward(100)
    turtie.left(45)

win.exitonclick()
