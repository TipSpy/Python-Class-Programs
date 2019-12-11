# Loan Qualifier
# This program determines whether a bank customer
# qualifies for a loan.

min_salary = 30000.0 # The minimum accual salary
min_years = 2        # The minimum years on the job

# Get the customer's annual salary
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job
years_on_job = float(input('Enter the number of ' \
                           'years employed: '))

# Determine whether the customer qualifies.
if salary >= min_salary:
    if years_on_job >= min_years:
        print('You qualify for the loan.')
    else:
        print('You must have been employed', \
              'for at least', min_years, \
              'years to qualify.')
else:
    print('You must earn at least $', \
          format(min_salary, '.2f'), \
          'years to qualify.')


# Name Sorter
# This program compares strings with the < operator
# Get two names from the user
name1 = input('Enter a name (last name first): ')
name2 = input('Enter another name (last name first): ')

# Display the names in alphabetical order
print('Here are the names, listed alphabetically.')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)


# Payroll
# This is a payroll program that calculates pay
# Variables to represent the base hours and
# tho overtime multiplier
base_hours = 40        # Base hours per week
ot_multiplier = 1.5    # Overtime multiplier

# Get the hours worked and the hourly pay rate
hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

# Calculate and display the gross pay
if hours > base_hours:
    # calculate the gross pay with overtime
    # First, get the number of overtime hours worked.
    overtime_hours = hours - base_hours

    # calculate the amount of overtime pay
    overtime_pay = overtime_hours * pay_rate * ot_multiplier

    # calculate the gross pay
    gross_pay = base_hours * pay_rate + overtime_pay
else:
    # Calculate the gross pay without overtime
    gross_pay = hours * pay_rate
#Display the gross pay
print('The gross pay is $', format(gross_pay, '.2f'))