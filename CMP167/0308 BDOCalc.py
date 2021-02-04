#BDO Market Calculator
m2 = 0

def c2(m2):
    c3 = int((m2-(m2/2.857141286)))
    c4 = int(c3*.3)
    c5 = int(c3+c4)
    return c5

def main():
    m1 = int(input("The price of your item: "))
    c1 = c2(m1)
    print("Profit with value pack:",c1,"silvers.")
    return main()

if __name__ == "__main__":
    main()
