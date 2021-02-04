def calculate_tax(income):
    inc = int(income)
    tax = 0
    if inc <= 200000:
        tax = inc * .25

    else:
        go = inc - 200000
        goo = go * .5
        print(goo)
        tax = (200000 * .25) + (goo)
        print(tax)
    return tax

def main():
    incc = int(input("enter a num"))
    caca = calculate_tax(incc)
    print(caca)

main()
