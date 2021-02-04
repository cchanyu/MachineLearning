from turtle import *

def nN():
    return int(input("Enter the size of the checkered flag:"))

def scren(cc):
    for i in range(0,4,3):
        cc.up()
        cc.goto(0,i)
        cc.down()
        cc.forward(3)

    cc.left(90)    
    for i in range(0,4,3):
        cc.up()
        cc.goto(i,0)
        cc.down()
        cc.forward(3)

def fillSquare(rw,cl,clr):
    return

def main():
    win = Screen()
    cc = Turtle()
    cc.speed(10)
    win.setworldcoordinates(-0.5,-0.5,3.5, 3.5)
    
    n = nN()
    scr = scren(cc)

    for i in range(n):
        row = i // n
        offset = row % 2
        col = (i % n) + offset
        fillSquare(row,col,"black")

    win.exitonclick()

if __name__ == "__main__":
    main()
