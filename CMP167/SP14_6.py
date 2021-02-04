from turtle import *

def mystery(t, n, d):
    for i in range(n):
        if d == "r":
            t.right(360/n)
        else:
            t.left(360/n)
        t.forward(50)

def draw(t, n):
    t.forward(100)
    mystery(t, n, "r")
    mystery(t, n, "l")
    
t = Turtle()
draw(t, 4)
