import turtle
win = turtle.Screen()
tic = turtle.Turtle()
tic.speed(100)
win.setworldcoordinates(-0.5,-0.5,3.5,3.5)

for i in range(9+1):
   tic.penup()
   tic.goto(0,i*.2)
   tic.pendown()
   tic.forward(1.8)
   
tic.left(90)
for i in range(9+1):
   tic.penup()
   tic.goto(i*.2,0)
   tic.pendown()
   tic.forward(1.8)

tic.penup()

win.exitonclick()
