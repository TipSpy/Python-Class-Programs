# This is the Counter and Accumulator demo program
#This program uses 3 variables
#The user inputs how many numbers will be entered for the program to use to calculate the total
#The loop runs once to get each number
#The grand total is calculated and printed onscreen

Counter = 0 #This counter variable counts how many times the loop is executing
Total = 0 #This accumulator variable keeps the running total that changes as numbers are entered
NewValue = 0 #This variable recieves a number from the user each time the loop executes
Iterations = int(input("How many times should the loop execute? "))
while Counter < Iterations:

    NewValue = int(input("Enter a new number: "))
    Total = Total + NewValue
    Counter = Counter + 1
    print("Counter is now at", Counter)

print("The loop's accumulated total is", Total)