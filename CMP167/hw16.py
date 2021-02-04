import turtle
import random

win = turtle.Screen()
taa = turtle.Turtle()

taa.speed(10)
taa.color("red")
taa.pensize(3)
taa.shape("turtle")

def square(sideLength):
    for i in range (4):
        taa.forward(sideLength)
        taa.right(90)
    return

def main():
    x = int(input("Enter a length: "))
    s = square(x)

main()

'''Write a program that asks the user for a length and
uses the turtle to draw a square with sides of that length.  

There should be a function for drawing the square that takes the
length of the sides as a parameter.'''
