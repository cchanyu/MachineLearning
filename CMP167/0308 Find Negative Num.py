'''
asks user for 5 numbers
and prints out how many are negative numbers
'''
y = 0
for i in range(5):
    x = int(input("Enter a number: "))
    if x < 0:
        y = y + 1
    print("You've entered",y,"Negative numbers.")
print("There were total of",y,"Negative numbers.")
