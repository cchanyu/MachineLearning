import math
x = int(input("Enter the max radius:"))
print("Radius Area of circle")
for i in range (1,x+1):
    print(i, math.pi*i*i)
