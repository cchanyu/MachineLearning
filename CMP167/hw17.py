import math

def getNumTrips(baln):
    cst = 2.75
    balan = int(baln/cst)
    return balan

def main():
    balance = float(input("Enter your Metrocard balance:"))
    calcc = getNumTrips(balance)
    print("You can take",str(calcc)+" more trips on the subway.")

if __name__ == "__main__":
    main()
