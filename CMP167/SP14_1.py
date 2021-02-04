s = "FridaysSaturdaysSundays"
num = s.count("s")
days = s[:-1].split("s")
print("There are", num, "fun days in a week")
print("Two of them are",days[0], days[-1])
result = ""
for i in range(len(days[0])):
    if i > 2:
        result = result + days[0][i]
print("My favorite", result, "is Saturday.")
