# Write your code here
print("Earned Amount: ")
bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80

print("Bubblegum: $" + str(bubblegum))
print("Toffee: $" + str(toffee))
print("Ice cream: $" + str(ice_cream))
print("Milk chocolate: $" + str(milk_chocolate))
print("Doughnut: $" + str(doughnut))
print("Pancake: $" + str(pancake))

income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake
print()
print("Income: $" + str(income) + ".0")

print("Staff expenses: ")
staff_expenses = int(input())
print("Other expenses: ")
other_expenses = int(input())

net_income = income - staff_expenses - other_expenses
print("Net Income: $" + str(net_income))