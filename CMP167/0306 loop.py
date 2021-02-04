
runningTotal = 0
numOfNums = int(input("How many number do you want to be asked? "))

#adds up the numbers
for i in range(numOfNums):
    num = int(input("Enter a number:"))
    runningTotal = runningTotal + num
    print("So far, runningTotal is",runningTotal)

print("The sum of your numbers is", runningTotal)

#adds up the words
wordOfWord = str()
for i in range(numOfNums):
    word = str(input("Enter a word:"))
    wordOfWord = str(wordOfWord) + " " + str(word)
    print("So far, your word is",str(wordOfWord), len(wordOfWord))
    
print(str(wordOfWord), len(wordOfWord))
