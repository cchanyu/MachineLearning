import math

def calc(x1):
    x2 = 1
    for i in range (1,x1+1):
        x2 = x2*i
        print("Number:",i,"Factorial:",x2)
    return x2

def main():
    x = int(input("Enter a number:"))

    #IF STATEMENT - eg. negative number
    if x < 0:
        print("Please enter a valid number.")
    else:
        x3 = calc(x)
        print("Factorial:",x3)
    return main()

if __name__ == "__main__":
    main()


'''
Accumulator cheat sheet
1. need variable
2. need loop
3. initalize variable
4. update variable in loop
'''
