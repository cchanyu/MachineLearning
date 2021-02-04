def translateToPigLatin(wrd):
    wrd2 = wrd
    if wrd[0].find("a") != -1 or wrd[0].find("e") != -1 or wrd[0].find("i") != -1 or wrd[0].find("o") != -1 or wrd[0].find("u") != -1:
        wrd2 = wrd + "hay"
    elif wrd[1].find("a") != -1 or wrd[1].find("e") != -1 or wrd[1].find("i") != -1 or wrd[1].find("o") != -1 or wrd[1].find("u") != -1 or wrd[1].find("y") != -1:
        wrd2 = wrd[1:] + wrd[:1] + "ay"
    elif wrd[2].find("a") != -1 or wrd[2].find("e") != -1 or wrd[2].find("i") != -1 or wrd[2].find("o") != -1 or wrd[2].find("u") != -1 or wrd[2].find("y") != -1:
        wrd2 = wrd[2:] + wrd[:2] + "ay"
    elif wrd[3].find("a") != -1 or wrd[3].find("e") != -1 or wrd[3].find("i") != -1 or wrd[3].find("o") != -1 or wrd[3].find("u") != -1 or wrd[3].find("y") != -1:
        wrd2 = wrd[3:] + wrd[:3] + "ay"
    else:
        return -1
    return wrd2

def main():
    word = input("Enter a word:")
    ttpl = translateToPigLatin(word)
    print("Your word in Pig Latin is",str(ttpl)+".")

if __name__ == "__main__":
    main()


'''
Enter a word:elephant
Your word in Pig Latin is elephanthay.
Sample code run 2:
Enter a word:myth
Your word in Pig Latin is ythmay.
Sample code run 3:
Enter a word:tree
Your word in Pig Latin is eetray.
Sample code run 4:
Enter a word:school
Your word in Pig Latin is oolschay.
'''
