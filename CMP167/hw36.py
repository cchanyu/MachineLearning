def toDoList():

    toList = input("Enter a list of things to do (separated by commas):")
    toDoLst = toList.split(",")
    counter=0
    for i in toDoLst:
        counter=counter+1
        print(str(counter)+". "+str(i))

toDoList()
