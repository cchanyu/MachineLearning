g = input("Enter a file name:")
infile = open(g,'r')
for i in infile:
    gg = str.upper(i)
    print(gg)
