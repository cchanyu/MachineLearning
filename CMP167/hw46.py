g = input("Enter a file name:")
p = input("Enter a output name:")
infile = open(g,'r')
outfile = open(p, 'w')
counter=1

for f in infile:
    c = str(counter) + "\t" + str(f)
    print(counter, f)
    outfile.write(c)
    counter = counter+1
    
infile.close()
outfile.close()
