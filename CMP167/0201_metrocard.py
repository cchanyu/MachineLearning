#What's your starting metrocard balance?
#How many trips did you make? (-2.75 for ea.)
#How much money did you add?
#your current balance is...
balance = float(input("What's your starting metrocard balance?"))
trips = int(input("How many trips did you make?"))
balance = balance - (trips * 2.75)
extra = float(input("How much money did you add?"))
balance = balance + extra
print("Your current balance is",str(balance)+".")

