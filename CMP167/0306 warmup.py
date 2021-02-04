#1. no input -> function1 -> hello!
#2. number -> function2 -> number+5
#3. string -> function3 -> no return
def welcome():
    print("Hello!")

def calc(x2):
    calc3 = (x2+5)
    return calc3

def word(y2):
    word3 = y2
    return

def main():
    welcome()
    x = float(input("Enter a number: "))
    calc2 = calc(x)
    print("Returned value:",calc2)
    y = str(input("Enter a word: "))
    word2 = word(y)
    print("Function:",word2,"Regular: ",y)

def func1():
    s = "I love Python!"
    x= 7
    return s
func1()

main()
