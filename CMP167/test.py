#open a file for reading
fileref = open("myFile.txt",'r')
outfile = open("myOutfile.txt",'w')

for line in fileref:
    s = "***"+line.strip()
    print(line)
    print(s)
    if line.find("A") != -1:
        outfile.write(line)
    else:
        -1
    #outfile.write(s + "\n")

fileref.close()
outfile.close()
