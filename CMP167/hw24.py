def enter():
    counter = 0
    for i in range(10):
        word = input("Enter a word:")
        if word == "python":
            counter = counter + 1
        else:
            counter = counter + 0
    return counter

def main():
    counted = enter()
    print("You entered the word python",counted,"times.")

if __name__ == "__main__":
    main()
