import random #Generates random number
x = int(input("Enter a number:"))

for i in range(x):
    #print(int(random.random()*50+50)) #Generates random number between
                                      #0(inclusive) and 100 (exclusive)
    print(random.randrange(1,x+1))   #randrange 

#TypeError = it should be a one type, but should be another
