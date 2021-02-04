import turtle
import random

win = turtle.Screen()
taa = turtle.Turtle()

taa.speed(10)
taa.color("red")
taa.pensize(3)
taa.shape("turtle")

x = int(3)

def flower():
    for i in range (8):
        taa.color("red")
        taa.forward(50)
        taa.left(45)
    return

def branch():
    taa.color("green")
    taa.left(90)
    taa.forward(100)

def brend():
    taa.color("green")
    taa.right(180)
    taa.forward(100)
    taa.left(90)

def walk():
    taa.forward(200)
    return

def main():
    for i in range (x):
        branch()
        flower()
        brend()
        walk()

main()
