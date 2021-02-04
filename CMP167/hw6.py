days = int(input("Enter the number of days:"))
calc = int(days/365)
years = calc
left = days%365
print("That is",years,"years and",left,"days.")
