#Budget

# Declare variables to store the budget amount,
# amount spent, difference, and total.
budet = 0.0
difference = 0.0
spent = 1.0 #initialize for while loop
total = 0.0

# Get the budgeted amount from the user.
budget = float(input('Enter amount budgeted for the month: '))

# Get the total amount spent from the user.
while spent != 0 :
    spent = float(input('Enter an amount spent(0 to quit): '))
    #add to total
    total += spent

# Determine whether the user is over or under budget,
# and display the result
print('Budgeted: $', format(budget, '.2f'))
print('Spent: $', format(total, '.2f'))

if budget > total:
    difference = budget - total
    print('You are $', format(difference, '.2f'), \
          'under budget. WELL DONE!')
elif budget < total:
    difference = total - budget
    print('You are $', format(difference, '.2f'), \
          'over budget. PLAN BETTER NEXT TIME!')
else:
    print('Spending matches budget. GOOD PLANNING!')