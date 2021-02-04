import math

def letters(x2):
    x3 = str()
    for i in range(x2):
        x3 = str(input("Enter a letter:"))+str(x3)
    return x3 

def main():
    x = int(input("How many letters will you enter?"))
    x9 = letters(x)
    print("Your string backwards is",x9+".")

if __name__=="__main__":
    main()
