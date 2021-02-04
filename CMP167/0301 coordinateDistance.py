#write a function that takes 4 ints representing 2 coordinates in the plane
#returns the Euclidean distance between them.
#distance = sqrt(x2-x1)^2+(y2-y1)^2
import math

def formula(x,y,xx,yy):
    distance = math.sqrt(((xx-x)**2+(yy-y)**2))
    return distance

def main():
    x1, y1 = eval(input("Enter X1 and Y1 coordinates:"))
    x2, y2 = eval(input("Enter X2 and Y2 coordinates:"))
    d = formula(x1,y1,x2,y2)
    print("The distance between two coordinate is:",d)

if __name__ == "__main__":
    main()
