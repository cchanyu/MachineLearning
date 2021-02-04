import math

num = int(input("Please enter a number: "))
squareRoot = math.sqrt(num)
print("You typed:",num,"Square Root:",squareRoot)


sinOfPi = math.sin(math.pi)
print("This is sin of Pi:",sinOfPi)

a = eval(input("Please enter a value for a: "))
b = eval(input("Please enter a value for b: "))
c = eval(input("Pkease enter a value for c: "))

# formula = "ax^2 + bx + c = 0"
# " ^ " replaces with x*x or ** or math.pow(x,2)

discriminant = b*b - 4 * a * c
x1=((-b-(math.sqrt(discriminant)))/(2*a))
x2=((-b+(math.sqrt(discriminant)))/(2*a))
print("x1 =",x1)
print("x2 =",x2)
