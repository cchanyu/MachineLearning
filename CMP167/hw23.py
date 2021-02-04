transitFare = 0

def getFare(theZone,ticketType):
    if theZone <= 2:
        if ticketType == "adult":
            transitFare = 23
        else:
            transitFare = 11.5
        return transitFare
    elif ticketType == "child" and theZone < 5:
        transitFare = 23
    elif theZone == 3:
        transitFare = 34.5
    elif theZone == 4:
        transitFare = 46
    else:
        transitFare = -1
        return transitFare
    return transitFare

def main():
    tZone = int(input("What is the zone?"))
    tType = str(input("What is the ticket type (adult/child)?"))
    cost = getFare(tZone, tType)
    print("The fare is "+str(cost)+" krone.")

if __name__ == "__main__":
    main()
