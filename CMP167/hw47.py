g = input("Enter the file name:")
infile = open(g,'r').read().splitlines()

lulu = [float(j) for i in infile for j in i.split(',')]

coo = sum(lulu)

print("The sum of your numbers is " + str(coo) + ".")
