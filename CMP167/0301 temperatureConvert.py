import math

def convert (cel):
    f = cel * (9/5) + 32
    return f

def main():
    c = float(input("Enter a Celeius: "))
    con = convert(c)
    print("Farenheit:",str(con))

main()
