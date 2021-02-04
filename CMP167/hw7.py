import turtle
win = turtle.Screen()
timmy = turtle.Turtle()

timmy.speed(1)
timmy.color("red")
timmy.shape("arrow")
timmy.pensize(3)

timmy.write("Hello", font=("Arial",50,"italic"))
for i in range(4):
    timmy.forward(200)
    timmy.left(90)
