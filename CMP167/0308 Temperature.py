def main():
    temp = int(input("Enter the current temperature:"))
    if (temp <= 32):
        print("It's below freezing!")
        return main()
    elif temp >= 90:
        print("It's a very hot weather!")
        return main()
    else:
        print("It's a good weather")
        return main()

if __name__ == "__main__":
    main()
