def nameOrganizer():
    names = input("Enter a list of names:")
    firstname = names.split(" ")
    firstname.reverse()
    print("You entered:")
    counter = 0
    wordd = ""
    for word in firstname:
        counter = counter + 1
        if counter == 2:
            wordd = wordd + " " + word[:-1]
            print (wordd)
        else:
            wordd = wordd + " " + word[:-1]
        

nameOrganizer()
