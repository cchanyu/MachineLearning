g = input("Enter a file name:")
infile = open(g,'r')
print("The first letters fo the lines in your file are:")
for i in infile:
    gg = str(i[0])
    print(gg)
