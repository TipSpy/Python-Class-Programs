#Temperatures

# Declare variables to hold the temperatures
celsius = 0.0
fahrenheit = 0.0

# Get the Celsius temperature
celsius = float(input("Enter a Celsius temperature: "))

# Calculate the Fahrenheit equivalent.
fahrenheit = (9.0 / 5.0) * celsius + 32

# Display the fahrenheit temperature.
print("That is equal to", format(fahrenheit, '.2f'), "degrees Fahrenheit.")