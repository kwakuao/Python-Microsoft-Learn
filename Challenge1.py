print("Today's Date is: ")
Date = input()
print("Breakfast calories eaten?")
Breakfast = int(input())
print("Lunch calories eaten?")
Lunch = int(input())
print("Dinner calories eaten?")
Dinner = int(input())
print("Snack calories eaten?")
Snack = int(input())
sum = Breakfast + Lunch + Dinner + Snack
print("Total calorie count for " + Date + " is: " + str(sum))
