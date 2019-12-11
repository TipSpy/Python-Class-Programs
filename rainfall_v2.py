#Rainfall
def main():

    #Local variables
    total = 0.0
    average = 0.0
    highest = 0.0
    lowest = 0.0
    month_lowest = ''
    month_highest = ''

    # List to recieve rainfall amounts
    month_rain = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    # Initialize a list with names of the months
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    #Get the amount of rainfall for each month
    for i in range(12):
        month_rain[i] = float(input('Enter the rainfall for ' + month_list[i] + ': '))

    #calculate the total
    total = sum(month_rain)

    #Calculate the average
    average = total / 12.0

    # Calculate the maximum
    highest = max(month_rain)

    # Get the index of the month with the highest rainfall
    month_highest = month_rain.index(highest)

    # Calculate the minimum
    lowest = min(month_rain)

    # Get the index of the month with the lowest rainfall
    month_lowest = month_rain.index(lowest)

    # Display results
    print('Total rainfall:', format(total, '.2f'))
    print('Average rainfall:', format(average, '.2f'))
    print('Highest rainfall:', month_list[month_highest])
    print('Lowest rainfall:', month_list[month_lowest])

# Call the main function
main()