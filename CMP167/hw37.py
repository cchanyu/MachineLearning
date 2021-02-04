def titleList(tL):
    count = len(tL)
    xlist = []
    for i in range (count):
        x = tL[i].title()
        xlist.append(x)
    return xlist
    

def main():
    toList = input("Enter a list of strings separated by commas:")
    toDoLst = toList.split(",")
    goo = titleList(toDoLst)
    print("Your new list is",goo)

if __name__ == "__main__":
    main()
