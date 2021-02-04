import turtle


win = turtle.Screen()
tic = turtle.Turtle()
tic.speed(10)
win.setworldcoordinates(-0.5,-0.5,3.5, 3.5)

for i in range(4+1):
   tic.penup()
   tic.goto(0,i*.5)
   tic.pendown()
   tic.forward(2)

tic.left(90)  
for i in range(4+1):
   tic.penup()
   tic.goto(i*.5,0)
   tic.pendown()
   tic.forward(2)

tic.penup()               

for i in range(4):
   x,y = eval(input("Please enter coordinates: "))
   tic.goto(x+.08,y+.08)
   tic.write("2",font=('Arial', 90, 'normal'))
#Need repeat function
#Acceptable Number: 0, 0.5, 1, 1.5

win.exitonclick()
