#Profit

# Variables to hold the sales total and the profit
salesTotal = 0.0
profit = 0.0

# Get the amount of projected sales.
salesTotal = float(input("Enter the projected sales: "))

# Calculate the projected profit.
profit = salesTotal * 0.23

# Print the projected profit.
print("The projected profit is ", format(profit, '.2f'))