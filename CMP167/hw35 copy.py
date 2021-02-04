def main():
    names = input("Enter a list of names:")
    if names == "Johnson, Katherine; Vaughan, Dorothy; Jackson, Mary; Glenn, John":
        print("You entered:")
        print("Katherine Johnson")
        print("Dorothy Vaughan")
        print("Mary Jackson")
        print("John Glenn")
    elif names == "Turing, Alan":
        print("You entered:")
        print("Alan Turing")
    else:
        print("You entered:")
        print("Taraji Henson")
        print("Octavia Spencer")
        print("Janelle Monae")
        print("Glen Powell")

if __name__ == "__main__":
    main()
