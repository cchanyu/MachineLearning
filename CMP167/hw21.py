def getFine(spdLim, spd):
    getLine = 0
    if spd <= spdLim:
        getLine = 0
    elif spd < spdLim+15:
        getLine = 100
    else:
        getLine = 100 + (5*(spd-spdLim))
    return getLine

def main():
    speedLimit = int(input("Enter the speed limit in miles:"))
    actualSpeed = int(input("Enter the actual speed in miles:"))
    x = getFine(speedLimit, actualSpeed)
    print("The fine is $"+str(x)+".")

if __name__ == "__main__":
    main()
