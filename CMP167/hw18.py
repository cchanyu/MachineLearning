def getNumCharacters(firstn,lastn):
    numb = len(firstn)+len(lastn)
    return numb

def main():
    first = input("Enter your first name:")
    last = input("Enter your last name:")
    number = getNumCharacters(first,last)
    print("There are",str(number),"characters in your full name.")

if __name__ == "__main__":
    main()
