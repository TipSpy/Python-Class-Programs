#Prime

# main function
def main():

    # Local variable
    number = 0

    # Get number
    number = int(input('Enter an integer: '))

    # Display information regarding whether the number is prime
    if is_prime(number):
        print('The number you entered is a prime number.')
    else:
        print('The number you entered is not a prime number.')

#The is_prime function recieves a number as an argument,
# and returns True if number is prime, False otherwise
def is_prime(number):
    #Local Variables
    half = int(number / 2)
    status = True

    for count in range(2, half + 1):
        if number % count == 0:
            status = False

    return status

# Call the main function
main()