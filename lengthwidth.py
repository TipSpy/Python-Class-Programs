#LengthWidth

# Local variables
lengthA = 0.0
widthA = 0.0
areaA = 0.0
lengthB = 0.0
widthB = 0.0
areaB = 0.0

# Get Length A 
lengthA = float(input("Enter length A: "))

# Get Width A 
widthA = float(input("Enter width A: "))

# Get Length B 
lengthB = float(input("Enter length B: "))

# Get Width B 
widthB = float(input("Enter width B: "))

# Calculate area A
areaA = lengthA * widthA

# Calculate area B
areaB = lengthB * widthB

# Print area comparison
print('Area A:', format(areaA, '.2f'))
print('Area B:', format(areaB, '.2f'))
if areaA > areaB:
    print("Area A is greater than Area B")
elif areaA < areaB:
    print("Area B is greater than Area A")
else:
    print("Area A is equal to Area B")