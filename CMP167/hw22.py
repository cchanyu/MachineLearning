import turtle

tata = turtle.Turtle()
win = turtle.Screen()

tata.speed(10)
win.bgcolor("white")
tata.pensize(3)
tata.shape("turtle")

x = int(input("Enter a whole number:"))

if x % 2 == 0:
    tata.pencolor("blue")
    tata.right(180)
    tata.forward(100)
else:
    tata.pencolor("red")
    tata.forward(100)
