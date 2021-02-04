#we can write our own functions:
#area of circle
#radius -> compute the area of a circle -> area
import math

def welcomeMessage():
    print("Welcome to my program!")
    print("It computes the area of a circle from the raidus")

def areaOfCircle(radius):
    area = radius * radius * math.pi
    return area

welcomeMessage()
r = float(input("Enter a radius:"))
a = areaOfCircle(r)
print("The area of the circle is",a)

#def function.name(parameters/arguments):
#statements
#return return_value
