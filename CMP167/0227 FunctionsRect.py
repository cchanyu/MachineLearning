import math

def areaOfRect(length, width):
    area = length * width
    return area

l = float(input("Enter a length:"))
w = float(input("Enter a width:"))
a = areaOfRect(l,w)
print("The area of the rectangle is",a)
