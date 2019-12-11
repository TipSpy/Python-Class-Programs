#StadiumSeats

# Global constants for stadium seating
CLASS_A_SEATS = 20
CLASS_B_SEATS = 15
CLASS_C_SEATS = 10

# main module
def main():
    #Local Variables
    countAseats = 0
    countBseats = 0
    countCseats = 0
    incomeAseats = 0.0
    incomeBseats = 0.0
    incomeCseats = 0.0

    # Get A count
    countAseats = int(input('Enter count of A seats: '))

    # Get B count
    countBseats = int(input('Enter count of B seats: '))

    # Get C count
    countCseats = int(input('Enter count of C seats: '))

    # Calculate A income
    incomeAseats = countAseats * CLASS_A_SEATS

    # Calculate B income
    incomeBseats = countBseats * CLASS_B_SEATS

    # Calculate C income
    incomeCseats = countCseats * CLASS_C_SEATS

    # Print Income
    showIncome(incomeAseats, incomeBseats, incomeCseats)

# The showIncome function accepts the income from class
# A, B, and C seats and displays the total income.
def showIncome(incomeAseats, incomeBseats, incomeCseats):
    # Local variable
    totalIncome = 0.0
    
    #Calculate total income
    totalIncome = incomeAseats + incomeBseats + incomeCseats

    # Show Results
    print('Income from class A seats: $', \
          format(incomeAseats, '.2f'))
    print('Income from class B seats: $', \
          format(incomeBseats, '.2f'))
    print('Income from class C seats: $', \
          format(incomeCseats, '.2f'))
    print('Total Income: $', \
          format(totalIncome, '.2f'))

#Call the main function
main()
