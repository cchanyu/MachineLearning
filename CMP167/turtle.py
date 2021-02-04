from turtle import *

# Ask the user for the size of the checkered flag (n).
def getSize():
    size = eval(input('Please enter the size of the checkered flag: '))
    return size

# Draw an n x n grid to the screen.
def drawGrid(turtle, n):
    for i in range(0, n+1):
        turtle.up()
        turtle.goto(0, i)
        turtle.down()
        turtle.forward(n)
    turtle.left(90)
    for i in range(0, n+1):
        turtle.up()
        turtle.goto(i, 0)
        turtle.down()
        turtle.forward(n)

# Fill the square in the given row and column.
def fillSquare(turtle, row, col):
    turtle.up()
    turtle.goto(col, row)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(1)
        turtle.right(90)
    turtle.end_fill()

def main():
    # Get the user's input.
    n = getSize()

    # Set up the drawing coordinates.
    win = Screen()
    win.setworldcoordinates(-1, -1, 10, 10)

    # Make a turtle object for use in drawing. Maximize its speed.
    turtle = Turtle()        
    turtle.speed('fastest')
    turtle.hideturtle()      

    # Draw the checkered flag.
    drawGrid(turtle, n)
    for i in range(0, n*n, 2):
        row = i // n
        offset = ~(n % 2) & (row % 2)
        col = i % n + offset
        fillSquare(turtle, row, col)

main()
